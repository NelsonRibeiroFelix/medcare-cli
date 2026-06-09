# MedCare-CLI

**Link do Deploy:** [Executar Online (via Google Colab)](https://colab.research.google.com/github/NelsonRibeiroFelix/medcare-cli/blob/main/notebooks/medcare_demo.ipynb)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/NelsonRibeiroFelix/medcare-cli/ci.yml?branch=main)
![Version](https://img.shields.io/badge/version-1.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

O **MedCare-CLI** é uma aplicação de linha de comando (CLI) que desenvolvi em Python como parte do meu BootCamp de Análise e Desenvolvimento de Sistemas (ADS). O objetivo é auxiliar cuidadores, familiares e idosos no controle e organização de horários de medicamentos, abordando um problema social relevante com uma solução prática.

## O Problema Social Abordado

Com o envelhecimento da população, a gestão de múltiplos medicamentos para idosos se torna um desafio crescente. O esquecimento de doses ou a confusão de horários podem comprometer a eficácia do tratamento e a saúde do paciente. Minha motivação para este projeto foi criar uma ferramenta simples que pudesse mitigar esses riscos, oferecendo um controle mais eficiente e acessível.

## A Solução Proposta: MedCare-CLI

O MedCare-CLI foi concebido para ser uma ferramenta intuitiva e de fácil uso, mesmo para quem não tem familiaridade com computadores. Através de uma interface de linha de comando, é possível registrar, listar e remover medicamentos, com suas respectivas dosagens e horários. A persistência dos dados agora suporta armazenamento em nuvem (Supabase) ou local (JSON), garantindo que as informações estejam sempre seguras e disponíveis.

## Público-Alvo

- **Cuidadores de idosos:** Para organizar a rotina de medicação de seus pacientes.
- **Familiares:** Para auxiliar no tratamento de parentes idosos.
- **Indivíduos em tratamento contínuo:** Pessoas que precisam gerenciar múltiplos medicamentos e buscam uma forma simples de registro.

## Funcionalidades Implementadas

- **Adicionar Medicamento:** Permite o cadastro de novos medicamentos, informando nome, dosagem e horário (formato HH:MM).
- **Listar Medicamentos:** Exibe todos os medicamentos cadastrados em uma tabela organizada.
- **Remover Medicamento:** Possibilita a exclusão de um medicamento específico utilizando seu ID.
- **Persistência em Nuvem:** Integração com banco de dados PostgreSQL via Supabase para armazenamento remoto.
- **Fallback Local:** Sistema de segurança que armazena dados em `medications.json` caso a conexão com a nuvem não esteja disponível.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Banco de Dados:** Supabase (PostgreSQL em nuvem)
- **Bibliotecas:** `tabulate`, `requests`
- **Testes:** `pytest` (para garantir a confiabilidade do código)
- **Qualidade de Código:** `ruff` (para linting e formatação)
- **Integração Contínua (CI):** GitHub Actions (automação de testes e validação)

## Como Instalar e Executar

Para utilizar o MedCare-CLI, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/NelsonRibeiroFelix/medcare-cli.git
    cd medcare-cli
    ```

2.  **Instale as dependências:**
    ```bash
    pip install .
    ```

3.  **Configuração (Opcional):**
    Para usar o banco em nuvem, renomeie o arquivo `.env.example` para `.env` e preencha suas credenciais do Supabase.

## Como Usar

Após a instalação, execute a aplicação com o comando:

```bash
python src/main.py
```

## Executando os Testes

```bash
pytest
```

## Autor

**Nelson Ribeiro Felix**
Estudante de Análise e Desenvolvimento de Sistemas (ADS)

## Repositório Público

[https://github.com/NelsonRibeiroFelix/medcare-cli](https://github.com/NelsonRibeiroFelix/medcare-cli)
