import os
from typing import Any

try:
    from supabase import Client, create_client
except ImportError:  # pragma: no cover
    Client = Any
    create_client = None


class DatabaseService:
    """Camada de acesso ao banco de dados em nuvem via Supabase.

    A aplicação usa Supabase quando as variáveis de ambiente ``SUPABASE_URL`` e
    ``SUPABASE_ANON_KEY`` estão configuradas. Em ambientes de desenvolvimento ou
    teste sem credenciais, a classe permanece indisponível de forma explícita,
    permitindo que a camada de aplicação use armazenamento local apenas como
    fallback controlado.
    """

    def __init__(self, table_name: str = "medications") -> None:
        self.table_name = table_name
        self.url = os.environ.get("SUPABASE_URL", "").strip()
        self.key = (
            os.environ.get("SUPABASE_ANON_KEY", "").strip()
            or os.environ.get("SUPABASE_KEY", "").strip()
        )
        self.client: Client | None = None
        self.last_error: str | None = None

        if self.is_configured and create_client is not None:
            try:
                self.client = create_client(self.url, self.key)
            except Exception as exc:  # pragma: no cover - depende do serviço externo
                self.last_error = str(exc)
                self.client = None

    @property
    def is_configured(self) -> bool:
        """Indica se as credenciais mínimas do Supabase foram informadas."""
        return bool(self.url and self.key)

    @property
    def is_available(self) -> bool:
        """Indica se o cliente Supabase está pronto para uso."""
        return self.client is not None

    def add_medication(self, medication_data: dict[str, Any]) -> dict[str, Any] | None:
        """Insere um medicamento no Supabase e retorna o registro criado."""
        if not self.is_available:
            return None

        try:
            result = (
                self.client.table(self.table_name)
                .insert(medication_data)
                .execute()
            )
            return result.data[0] if result.data else None
        except Exception as exc:  # pragma: no cover - depende do serviço externo
            self.last_error = str(exc)
            return None

    def get_all_medications(self) -> list[dict[str, Any]]:
        """Lista os medicamentos cadastrados no Supabase."""
        if not self.is_available:
            return []

        try:
            result = (
                self.client.table(self.table_name)
                .select("id,name,dosage,time,created_at")
                .order("time")
                .execute()
            )
            return list(result.data or [])
        except Exception as exc:  # pragma: no cover - depende do serviço externo
            self.last_error = str(exc)
            return []

    def remove_medication(self, medication_id: int) -> bool:
        """Remove um medicamento pelo ID no Supabase."""
        if not self.is_available:
            return False

        try:
            result = (
                self.client.table(self.table_name)
                .delete()
                .eq("id", medication_id)
                .execute()
            )
            return bool(result.data)
        except Exception as exc:  # pragma: no cover - depende do serviço externo
            self.last_error = str(exc)
            return False

    def clear_all(self) -> bool:
        """Remove todos os registros da tabela de medicamentos.

        Método usado apenas em testes ou manutenção controlada. A condição
        ``id > 0`` evita uma exclusão sem filtro, que o Supabase rejeita por
        segurança.
        """
        if not self.is_available:
            return False

        try:
            self.client.table(self.table_name).delete().gt("id", 0).execute()
            return True
        except Exception as exc:  # pragma: no cover - depende do serviço externo
            self.last_error = str(exc)
            return False
