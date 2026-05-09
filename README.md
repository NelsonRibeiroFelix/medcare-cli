# MedCare-CLI

**Link do Deploy:** [Executar Online (via Google Colab)](https://colab.research.google.com/github/NelsonRibeiroFelix/medcare-cli/blob/main/notebooks/medcare_demo.ipynb)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/NelsonRibeiroFelix/medcare-cli/ci.yml?branch=main)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

O **MedCare-CLI** é uma aplicação de linha de comando (CLI) que desenvolvi em Python como parte do meu BootCamp de Análise e Desenvolvimento de Sistemas (ADS). O objetivo é auxiliar cuidadores, familiares e idosos no controle e organização de horários de medicamentos, abordando um problema social relevante com uma solução prática.

## O Problema Social Abordado

Com o envelhecimento da população, a gestão de múltiplos medicamentos para idosos se torna um desafio crescente. O esquecimento de doses ou a confusão de horários podem comprometer a eficácia do tratamento e a saúde do paciente. Minha motivação para este projeto foi criar uma ferramenta simples que pudesse mitigar esses riscos, oferecendo um controle mais eficiente e acessível.

## A Solução Proposta: MedCare-CLI

O MedCare-CLI foi concebido para ser uma ferramenta intuitiva e de fácil uso, mesmo para quem não tem familiaridade com computadores. Através de uma interface de linha de comando, é possível registrar, listar e remover medicamentos, com suas respectivas dosagens e horários. A persistência dos dados em um arquivo JSON garante que as informações estejam sempre disponíveis, tornando o gerenciamento da medicação mais seguro e organizado.

## Público-Alvo

- **Cuidadores de idosos:** Para organizar a rotina de medicação de seus pacientes.
- **Familiares:** Para auxiliar no tratamento de parentes idosos.
- **Indivíduos em tratamento contínuo:** Pessoas que precisam gerenciar múltiplos medicamentos e buscam uma forma simples de registro.

## Funcionalidades Implementadas

- **Adicionar Medicamento:** Permite o cadastro de novos medicamentos, informando nome, dosagem e horário (formato HH:MM).
- **Listar Medicamentos:** Exibe todos os medicamentos cadastrados em uma tabela organizada.
- **Remover Medicamento:** Possibilita a exclusão de um medicamento específico utilizando seu ID.
- **Persistência de Dados:** Os dados são armazenados localmente em um arquivo `medications.json`, garantindo que as informações não sejam perdidas.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Bibliotecas:** `tabulate` (para formatação de tabelas no terminal)
- **Testes:** `pytest` (para garantir a confiabilidade do código)
- **Qualidade de Código:** `ruff` (para linting e formatação)
- **Integração Contínua (CI):** GitHub Actions (para automação de testes e linting)
- **Integração com API:** Consumo da API ViaCEP para validação de endereços.

## Como Instalar e Executar

Para utilizar o MedCare-CLI, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/NelsonRibeiroFelix/medcare-cli.git
    cd medcare-cli
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install .
    ```
    *O projeto utiliza o arquivo `pyproject.toml` para gerenciar as dependências de forma declarativa.*

## Como Usar

Após a instalação, execute a aplicação com o comando:

```bash
python src/main.py
```

Um menu interativo será exibido, permitindo que você gerencie os medicamentos.

## Executando os Testes

Para verificar a integridade do código e garantir que as funcionalidades estão operando como esperado, execute os testes automatizados:

```bash
pip install ".[dev]"
pytest
```

## Verificando a Qualidade do Código (Linting)

Para manter o código limpo e padronizado, utilizei o `ruff`. Para verificar:

```bash
ruff check src/ tests/
```

Para formatar automaticamente:

```bash
ruff format src/ tests/
```

## Versão Atual

A versão atual do projeto é **1.0.0**, seguindo as diretrizes de Versionamento Semântico (Semantic Versioning).

## Autor

**Nelson Ribeiro Felix**
Estudante de Análise e Desenvolvimento de Sistemas (ADS)

## Repositório Público

[https://github.com/NelsonRibeiroFelix/medcare-cli](https://github.com/NelsonRibeiroFelix/medcare-cli)
