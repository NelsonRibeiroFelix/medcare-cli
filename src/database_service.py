import os
from supabase import create_client, Client

class DatabaseService:
    """
    Serviço para gerenciar a conexão e operações com o banco de dados Supabase.
    """
    def __init__(self):
        # Em um ambiente real, estas chaves viriam de variáveis de ambiente
        # Para fins acadêmicos, usaremos placeholders que podem ser configurados
        self.url = os.environ.get("SUPABASE_URL", "https://your-project.supabase.co")
        self.key = os.environ.get("SUPABASE_KEY", "your-anon-key")
        
        try:
            self.client: Client = create_client(self.url, self.key)
        except Exception:
            self.client = None

    def add_medication(self, medication_data):
        """Adiciona um medicamento ao banco de dados."""
        if not self.client:
            return False
        try:
            result = self.client.table("medications").insert(medication_data).execute()
            return len(result.data) > 0
        except Exception:
            return False

    def get_all_medications(self):
        """Recupera todos os medicamentos do banco de dados."""
        if not self.client:
            return []
        try:
            result = self.client.table("medications").select("*").execute()
            return result.data
        except Exception:
            return []

    def remove_medication(self, medication_id):
        """Remove um medicamento pelo ID."""
        if not self.client:
            return False
        try:
            result = self.client.table("medications").delete().eq("id", medication_id).execute()
            return len(result.data) > 0
        except Exception:
            return False
