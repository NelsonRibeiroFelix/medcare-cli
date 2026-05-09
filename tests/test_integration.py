import os
import sys
from unittest.mock import patch

# Adiciona o diretório src ao path para importação
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from address_service import AddressService


def test_get_address_by_cep_success():
    """
    Teste de integração (mockado): Valida se a aplicação processa corretamente
    uma resposta de sucesso da API ViaCEP.
    """
    mock_response = {
        "logradouro": "Praça da Sé",
        "bairro": "Sé",
        "localidade": "São Paulo",
        "uf": "SP"
    }
    
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "cep": "01001-000",
            "logradouro": "Praça da Sé",
            "complemento": "lado ímpar",
            "bairro": "Sé",
            "localidade": "São Paulo",
            "uf": "SP",
            "ibge": "3550308",
            "gia": "1004",
            "ddd": "11",
            "siafi": "7107"
        }
        
        result = AddressService.get_address_by_cep("01001000")
        
        assert result == mock_response
        mock_get.assert_called_once()

def test_get_address_by_cep_not_found():
    """
    Teste de integração (mockado): Valida o comportamento quando o CEP não existe.
    """
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"erro": "true"}
        
        result = AddressService.get_address_by_cep("99999999")
        
        assert result == {"error": "CEP não encontrado."}

def test_get_address_by_cep_invalid_format():
    """
    Teste de unidade/integração: Valida se o sistema rejeita CEPs com formato errado.
    """
    result = AddressService.get_address_by_cep("123")
    assert result == {"error": "CEP inválido. Deve conter 8 dígitos."}
