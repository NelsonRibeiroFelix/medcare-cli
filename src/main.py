import os
import sys

from tabulate import tabulate

# Adiciona o diretório src ao path para facilitar as importações locais
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from address_service import AddressService
from medication_manager import MedicationManager


def clear_screen():
    """Limpa o terminal de acordo com o sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    """Exibe o cabeçalho do sistema."""
    print("=" * 50)
    print("      MedCare-CLI - Sistema de Medicamentos")
    print("=" * 50)


def main_menu():
    """Função principal que gerencia o menu e a interação com o usuário."""
    manager = MedicationManager()

    while True:
        clear_screen()
        print_header()
        print(f"\nPersistência ativa: {manager.storage_mode}")
        print("\n[1] Adicionar Medicamento")
        print("[2] Listar Medicamentos")
        print("[3] Remover Medicamento")
        print("[4] Buscar Endereço por CEP")
        print("[5] Sair")

        opcao = input("\nSelecione uma opção: ")

        if opcao == "1":
            nome = input("Nome do remédio: ")
            dosagem = input("Dosagem (ex: 500mg): ")
            horario = input("Horário (HH:MM): ")
            try:
                manager.add_medication(nome, dosagem, horario)
                print("\nMedicamento cadastrado com sucesso!")
            except ValueError as e:
                print(f"\nErro de validação: {e}")
            except RuntimeError as e:
                print(f"\nErro de persistência: {e}")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "2":
            meds = manager.list_medications()
            if not meds:
                print("\nNenhum medicamento cadastrado no momento.")
            else:
                headers = ["ID", "Nome", "Dosagem", "Horário"]
                table_data = [
                    [
                        m.get("id", "-"),
                        m.get("name", "-"),
                        m.get("dosage", "-"),
                        m.get("time", "-"),
                    ]
                    for m in meds
                ]
                print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "3":
            meds = manager.list_medications()
            if not meds:
                print("\nNão há medicamentos para remover.")
            else:
                try:
                    med_id = int(input("Informe o ID do medicamento para remover: "))
                    if manager.remove_medication(med_id):
                        print("\nMedicamento removido com sucesso!")
                    else:
                        print("\nID não encontrado na lista.")
                except ValueError:
                    print("\nErro: O ID deve ser um número inteiro.")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "4":
            cep = input("Informe o CEP (apenas números): ")
            print("\nBuscando informações...")
            result = AddressService.get_address_by_cep(cep)

            if "error" in result:
                print(f"\nErro: {result['error']}")
            else:
                print("\nEndereço Encontrado:")
                print(f"Rua: {result['logradouro']}")
                print(f"Bairro: {result['bairro']}")
                print(f"Cidade: {result['localidade']} - {result['uf']}")
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "5":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    main_menu()
