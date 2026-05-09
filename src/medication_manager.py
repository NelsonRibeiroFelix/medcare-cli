import json
import os
from datetime import datetime


class MedicationManager:
    """
    Classe responsável por gerenciar a lógica de armazenamento e manipulação
    dos dados de medicamentos.
    """

    def __init__(self, storage_file="medications.json"):
        self.storage_file = storage_file
        self.medications = self._load_data()

    def _load_data(self):
        # Carrega os dados do arquivo JSON se ele existir
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def _save_data(self):
        # Salva a lista atual de medicamentos no arquivo JSON
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

        # Cria o dicionário do medicamento com um ID incremental simples
        medication = {
            "id": len(self.medications) + 1,
            "name": name,
            "dosage": dosage,
            "time": time,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.medications.append(medication)
        self._save_data()
        return medication

    def list_medications(self):
        return self.medications

    def remove_medication(self, med_id):
        # Remove o medicamento pelo ID e atualiza o arquivo
        initial_count = len(self.medications)
        self.medications = [m for m in self.medications if m["id"] != med_id]
        if len(self.medications) < initial_count:
            self._save_data()
            return True
        return False

    def clear_all(self):
        # Limpa todos os dados (útil para testes)
        self.medications = []
        if os.path.exists(self.storage_file):
            os.remove(self.storage_file)
