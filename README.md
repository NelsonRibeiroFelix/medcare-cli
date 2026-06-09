# MedCare-CLI

**Autor:** Nelson Ribeiro Felix  
**Repositório público:** [github.com/NelsonRibeiroFelix/medcare-cli](https://github.com/NelsonRibeiroFelix/medcare-cli)  
**Deploy demonstrativo:** [Executar Online via Google Colab](https://colab.research.google.com/github/NelsonRibeiroFelix/medcare-cli/blob/main/notebooks/medcare_demo.ipynb)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/NelsonRibeiroFelix/medcare-cli/ci.yml?branch=main)
![Version](https://img.shields.io/badge/version-1.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

O **MedCare-CLI** é uma aplicação de linha de comando desenvolvida em Python para apoiar cuidadores, familiares e pessoas em tratamento contínuo no controle de horários de medicamentos. A versão atual mantém a simplicidade da interface em terminal, mas evolui a persistência para integração com **Supabase**, permitindo que os registros sejam armazenados em um banco PostgreSQL hospedado em nuvem quando as credenciais do serviço estão configuradas.[1]

## Objetivo do Projeto

A proposta do projeto é oferecer uma solução prática para registrar, consultar e remover medicamentos, reduzindo falhas de organização em rotinas de cuidado. O sistema também inclui consulta de endereço por CEP usando a API pública ViaCEP, recurso útil para complementar cadastros e validações de localização.[2]

## Funcionalidades

| Funcionalidade | Descrição | Persistência |
|---|---|---|
| Cadastro de medicamento | Registra nome, dosagem e horário no formato `HH:MM`. | Supabase quando configurado; fallback local para desenvolvimento. |
| Listagem de medicamentos | Exibe os registros em tabela no terminal. | Consulta a tabela `medications` no Supabase. |
| Remoção de medicamento | Exclui um medicamento pelo identificador numérico. | Remove o registro correspondente no banco em nuvem. |
| Consulta de CEP | Busca logradouro, bairro, cidade e UF. | Consome a API ViaCEP em tempo de execução. |
| Testes e qualidade | Executa testes automatizados e lint. | Validado via `pytest`, `ruff` e GitHub Actions.[3] |

## Tecnologias Utilizadas

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.11+ |
| Interface | CLI com `tabulate` |
| Banco em nuvem | Supabase com PostgreSQL |
| API externa | ViaCEP |
| Testes | `pytest` |
| Qualidade de código | `ruff` |
| Integração contínua | GitHub Actions |
| Deploy demonstrativo | Google Colab |

## Estrutura do Projeto

```text
medcare-cli/
├── .github/workflows/ci.yml
├── notebooks/medcare_demo.ipynb
├── src/
│   ├── address_service.py
│   ├── database_service.py
│   ├── main.py
│   └── medication_manager.py
├── supabase/schema.sql
├── tests/
│   ├── test_integration.py
│   └── test_medication_manager.py
├── .env.example
├── pyproject.toml
└── README.md
```

## Configuração do Banco de Dados em Nuvem

O projeto está preparado para usar Supabase. Para configurar o banco, crie um projeto no Supabase, abra o editor SQL e execute o arquivo `supabase/schema.sql`. Em seguida, copie `.env.example` para `.env` e informe os dados do seu projeto.

```bash
cp .env.example .env
```

```bash
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_ANON_KEY=sua-chave-anon-publica
```

> Em ambiente sem essas variáveis, a aplicação usa um arquivo local apenas como fallback de desenvolvimento e testes. Para a entrega final, recomenda-se executar com Supabase configurado, pois o requisito acadêmico exige leitura e escrita em banco hospedado em nuvem.

## Como Instalar e Executar

Clone o repositório, crie um ambiente virtual e instale as dependências declaradas no `pyproject.toml`.

```bash
git clone https://github.com/NelsonRibeiroFelix/medcare-cli.git
cd medcare-cli
python -m venv venv
source venv/bin/activate
pip install .
python src/main.py
```

No Windows, a ativação do ambiente virtual pode ser feita com `venv\Scripts\activate`.

## Executando Testes e Lint

Os testes verificam a regra de negócio do cadastro de medicamentos, o fallback local controlado, o fluxo de banco simulado e a integração com a API ViaCEP por meio de mocks. Para validar o projeto localmente, execute:

```bash
pip install ".[dev]"
pytest
ruff check src/ tests/
```

## Integração Contínua

O workflow `.github/workflows/ci.yml` executa automaticamente instalação de dependências, testes e lint em pushes e Pull Requests direcionados à branch `main`. Esse fluxo ajuda a impedir que alterações sejam mescladas sem validação mínima de qualidade.[3]

## Colaboração e Pull Requests

A entrega colaborativa deve ser feita com issues, branches e Pull Requests reais no GitHub. Cada integrante precisa abrir pelo menos um Pull Request com commits próprios, e outro integrante deve revisar e aprovar antes do merge. Esse histórico não deve ser simulado: ele precisa refletir contribuições efetivas registradas na aba de Pull Requests.

## Autor

**Nelson Ribeiro Felix**  
Estudante de Análise e Desenvolvimento de Sistemas

## Licença

Este projeto está licenciado sob os termos da licença MIT disponível no arquivo `LICENSE`.

## Referências

[1]: https://supabase.com/docs "Supabase Documentation"  
[2]: https://viacep.com.br "ViaCEP"  
[3]: https://docs.github.com/actions "GitHub Actions Documentation"
