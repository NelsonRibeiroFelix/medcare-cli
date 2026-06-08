import json
import os
from datetime import datetime
from src.database_service import DatabaseService

class MedicationManager:
    """
    Classe responsável por gerenciar a lógica de armazenamento e manipulação
    dos dados de medicamentos, agora integrada com banco de dados na nuvem.
    """

    def __init__(self, storage_file="medications.json"):
        self.storage_file = storage_file
        self.db = DatabaseService()
        self.medications = self._load_data()

    def _load_data(self):
        # Tenta carregar do banco de dados primeiro
        db_data = self.db.get_all_medications()
        if db_data:
            return db_data

        # Fallback para o arquivo JSON local
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def _save_data(self):
        # Salva a lista atual de medicamentos no arquivo JSON (backup local)
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(self.medications, f, indent=4, ensure_ascii=False)

    def add_medication(self, name, dosage, time):
        # Validação simples de campos obrigatórios
        if not name or not dosage or not time:
            raise ValueError("Nome, dosagem e horário são obrigatórios.")

        # Validação do formato de hora (HH:MM)
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("O horário deve estar no formato HH:MM.")

        # Cria o dicionário do medicamento
        medication = {
            "name": name,
            "dosage": dosage,
            "time": time,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Tenta salvar no banco de dados
        self.db.add_medication(medication)

        # Atualiza lista local para feedback imediato e backup
        medication["id"] = len(self.medications) + 1
        self.medications.append(medication)
        self._save_data()
        return medication

    def list_medications(self):
        # Recarrega para garantir sincronia com o banco
        self.medications = self._load_data()
        return self.medications

    def remove_medication(self, med_id):
        # Tenta remover do banco
        self.db.remove_medication(med_id)

        # Remove o medicamento pelo ID localmente e atualiza o backup
        initial_count = len(self.medications)
        self.medications = [m for m in self.medications if m.get("id") != med_id]
        if len(self.medications) < initial_count:
            self._save_data()
            return True
        return False

    def clear_all(self):
        # Limpa todos os dados locais
        self.medications = []
        if os.path.exists(self.storage_file):
            os.remove(self.storage_file)
