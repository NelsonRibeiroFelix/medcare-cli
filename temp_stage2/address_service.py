import requests


class AddressService:
    """
    Serviço para integração com a API pública do ViaCEP.
    Permite validar endereços e buscar informações de localização.
    """
    BASE_URL = "https://viacep.com.br/ws"

    @staticmethod
    def get_address_by_cep(cep):
        """
        Busca informações de endereço a partir de um CEP.
        """
        # Remove caracteres não numéricos
        cep = "".join(filter(str.isdigit, cep))
        
        if len(cep) != 8:
            return {"error": "CEP inválido. Deve conter 8 dígitos."}

        try:
            url = f"{AddressService.BASE_URL}/{cep}/json/"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if "erro" in data:
                return {"error": "CEP não encontrado."}
            
            return {
                "logradouro": data.get("logradouro"),
                "bairro": data.get("bairro"),
                "localidade": data.get("localidade"),
                "uf": data.get("uf")
            }
        except requests.RequestException:
            return {"error": "Erro ao conectar com o serviço de CEP."}
