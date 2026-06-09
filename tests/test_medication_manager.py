import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from medication_manager import MedicationManager


class FakeDatabaseService:
    def __init__(self, available=False):
        self.is_available = available
        self.records = []

    def get_all_medications(self):
        return list(self.records)

    def add_medication(self, medication_data):
        medication = {"id": len(self.records) + 1, **medication_data}
        self.records.append(medication)
        return medication

    def remove_medication(self, medication_id):
        initial_count = len(self.records)
        self.records = [
            record for record in self.records if record["id"] != medication_id
        ]
        return len(self.records) < initial_count

    def clear_all(self):
        self.records = []
        return True


@pytest.fixture
def manager(tmp_path):
    test_file = tmp_path / "test_medications.json"
    return MedicationManager(
        storage_file=str(test_file),
        database_service=FakeDatabaseService(available=False),
    )


def test_add_medication_success(manager):
    med = manager.add_medication("Paracetamol", "500mg", "08:00")

    assert med["id"] == 1
    assert med["name"] == "Paracetamol"
    assert med["dosage"] == "500mg"
    assert med["time"] == "08:00"
    assert len(manager.list_medications()) == 1


def test_add_medication_invalid_time(manager):
    with pytest.raises(ValueError, match="O horário deve estar no formato HH:MM."):
        manager.add_medication("Aspirina", "100mg", "8 da manhã")


def test_remove_non_existent_medication(manager):
    manager.add_medication("Vitamina C", "1g", "10:00")

    result = manager.remove_medication(999)

    assert result is False
    assert len(manager.list_medications()) == 1


def test_add_medication_missing_fields(manager):
    with pytest.raises(ValueError, match="Nome, dosagem e horário são obrigatórios."):
        manager.add_medication("", "500mg", "08:00")


def test_clear_all_medications(manager):
    manager.add_medication("Remédio 1", "10mg", "08:00")
    manager.add_medication("Remédio 2", "20mg", "20:00")

    assert len(manager.list_medications()) == 2

    manager.clear_all()

    assert len(manager.list_medications()) == 0


def test_cloud_mode_uses_database_service(tmp_path):
    database = FakeDatabaseService(available=True)
    manager = MedicationManager(
        storage_file=str(tmp_path / "unused.json"),
        database_service=database,
    )

    created = manager.add_medication("Losartana", "50mg", "07:30")

    assert manager.storage_mode == "Supabase"
    assert created["id"] == 1
    assert manager.list_medications() == [created]
    assert manager.remove_medication(1) is True
    assert manager.list_medications() == []
