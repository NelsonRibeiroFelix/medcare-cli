# Changelog

Todas as mudanças relevantes deste projeto são registradas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), e este projeto segue [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-06-09

### Adicionado

- Integração configurável com Supabase para persistência de medicamentos em banco PostgreSQL hospedado em nuvem.
- Arquivo `supabase/schema.sql` com a estrutura da tabela `medications` e políticas básicas de acesso.
- Arquivo `.env.example` com as variáveis necessárias para configurar o banco em nuvem sem versionar credenciais reais.
- Teste automatizado cobrindo o modo de persistência em nuvem por meio de serviço de banco simulado.

### Alterado

- Atualização do `MedicationManager` para separar claramente persistência em Supabase e fallback local de desenvolvimento.
- Atualização da interface CLI para exibir o modo real de persistência em uso.
- Correção completa do workflow do GitHub Actions para rodar em pushes e Pull Requests na branch `main`.
- Atualização do README com instruções de banco em nuvem, testes, CI, deploy demonstrativo e autoria.

### Corrigido

- Remoção de mensagem enganosa que indicava conexão com banco em nuvem mesmo quando o Supabase não estava configurado.
- Declaração das dependências runtime `requests` e `supabase` no `pyproject.toml`.

## [1.0.0] - 2026-04-12

### Adicionado

- Versão inicial do MedCare-CLI, desenvolvida como parte do BootCamp de ADS.
- Funcionalidade de adicionar, listar e remover medicamentos.
- Implementação de persistência de dados em arquivo JSON.
- Testes automatizados com `pytest` para as funcionalidades principais.
- Configuração de linting e formatação de código com `ruff`.
- Pipeline de Integração Contínua (CI) com GitHub Actions para validação automática.
- Documentação inicial do projeto.
