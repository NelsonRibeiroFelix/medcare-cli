import os
import sys

import pytest

# Adiciona o diretório src ao path para importação
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from medication_manager import MedicationManager


@pytest.fixture
def manager():
    test_file = "test_medications.json"
    m = MedicationManager(storage_file=test_file)
    yield m
    # Cleanup after tests
    if os.path.exists(test_file):
        os.remove(test_file)


def test_add_medication_success(manager):
    """Caminho feliz: Adicionar um medicamento corretamente."""
    med = manager.add_medication("Paracetamol", "500mg", "08:00")
    assert med["name"] == "Paracetamol"
    assert med["dosage"] == "500mg"
    assert med["time"] == "08:00"
    assert len(manager.list_medications()) == 1


def test_add_medication_invalid_time(manager):
    """Entrada inválida: Tentar adicionar com formato de hora errado."""
    with pytest.raises(ValueError, match="O horário deve estar no formato HH:MM."):
        manager.add_medication("Aspirina", "100mg", "8 da manhã")


def test_remove_non_existent_medication(manager):
    """Caso limite: Tentar remover um ID que não existe."""
    manager.add_medication("Vitamina C", "1g", "10:00")
    result = manager.remove_medication(999)  # ID inexistente
    assert result is False
    assert len(manager.list_medications()) == 1


def test_add_medication_missing_fields(manager):
    """Caso limite: Tentar adicionar sem campos obrigatórios."""
    with pytest.raises(ValueError, match="Nome, dosagem e horário são obrigatórios."):
        manager.add_medication("", "500mg", "08:00")


def test_clear_all_medications(manager):
    """Funcionalidade extra: Limpar todos os medicamentos."""
    manager.add_medication("Remédio 1", "10mg", "08:00")
    manager.add_medication("Remédio 2", "20mg", "20:00")
    assert len(manager.list_medications()) == 2
    manager.clear_all()
    assert len(manager.list_medications()) == 0
