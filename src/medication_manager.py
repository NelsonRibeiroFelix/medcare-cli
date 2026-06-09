import json
import os
from datetime import datetime
from typing import Any

from database_service import DatabaseService


class MedicationManager:
    """Gerencia validação e persistência dos medicamentos cadastrados."""

    def __init__(
        self,
        storage_file: str = "medications.json",
        database_service: DatabaseService | None = None,
    ) -> None:
        self.storage_file = storage_file
        self.db = database_service or DatabaseService()
        self.medications = self._load_data()

    @property
    def storage_mode(self) -> str:
        """Retorna o modo de persistência em uso pela aplicação."""
        return "Supabase" if self.db.is_available else "Local"

    @property
    def cloud_ready(self) -> bool:
        """Indica se a persistência em nuvem está operacional."""
        return self.db.is_available

    def _load_local_data(self) -> list[dict[str, Any]]:
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                return []
        return []

    def _load_data(self) -> list[dict[str, Any]]:
        if self.db.is_available:
            return self.db.get_all_medications()
        return self._load_local_data()

    def _save_local_data(self) -> None:
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump(self.medications, file, indent=4, ensure_ascii=False)

    def _next_local_id(self) -> int:
        if not self.medications:
            return 1
        return max(int(medication.get("id", 0)) for medication in self.medications) + 1

    @staticmethod
    def _validate_fields(name: str, dosage: str, time: str) -> None:
        if not name or not dosage or not time:
            raise ValueError("Nome, dosagem e horário são obrigatórios.")

        try:
            datetime.strptime(time, "%H:%M")
        except ValueError as exc:
            raise ValueError("O horário deve estar no formato HH:MM.") from exc

    def add_medication(self, name: str, dosage: str, time: str) -> dict[str, Any]:
        """Cadastra um medicamento no Supabase ou no fallback local."""
        self._validate_fields(name, dosage, time)

        medication = {
            "name": name.strip(),
            "dosage": dosage.strip(),
            "time": time.strip(),
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }

        if self.db.is_available:
            inserted = self.db.add_medication(medication)
            if inserted is None:
                raise RuntimeError(
                    "Não foi possível salvar o medicamento no banco em nuvem. "
                    "Verifique as credenciais e a estrutura da tabela Supabase."
                )
            return inserted

        medication["id"] = self._next_local_id()
        self.medications.append(medication)
        self._save_local_data()
        return medication

    def list_medications(self) -> list[dict[str, Any]]:
        """Lista medicamentos a partir da fonte de persistência em uso."""
        self.medications = self._load_data()
        return self.medications

    def get_medication_by_id(self, medication_id: int) -> dict[str, Any] | None:
        """Busca um medicamento específico pelo seu identificador."""
        meds = self.list_medications()
        for med in meds:
            if int(med.get("id", 0)) == medication_id:
                return med
        return None

    def remove_medication(self, medication_id: int) -> bool:
        """Remove um medicamento do Supabase ou do fallback local."""
        if self.db.is_available:
            return self.db.remove_medication(medication_id)

        initial_count = len(self.medications)
        self.medications = [
            medication
            for medication in self.medications
            if int(medication.get("id", 0)) != medication_id
        ]
        if len(self.medications) < initial_count:
            self._save_local_data()
            return True
        return False

    def clear_all(self) -> None:
        """Limpa os dados usados em testes ou manutenção local."""
        self.medications = []
        if self.db.is_available:
            self.db.clear_all()
        if os.path.exists(self.storage_file):
            os.remove(self.storage_file)
