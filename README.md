# Agente SQL Universal para Consultas 

Este proejto foi criado com o intuito de auxíliar desenvolvedores com a criação e manipulação de consulas SQL, independe do SGDB que utilizarem.

## Stack utilizada

**Front-end:** React, Redux, TailwindCSS

**Back-end:** Python, Express

## Guia de Instalação

📋 Pré-requisitos

* Python 3.8 ou superior
* Chave da API OpenAI
* Banco(s) de dados para conectar

**1. Clone/Baixe os arquivos**

Certifique-se de ter os seguintes arquivos:

universal_sql_agent.py (código principal)
sql_agent_config.py (configuração e exemplos)
requirements.txt (dependências)

**2. Instale as dependências**

```bash
pip install -r requirements.txt
```

**3. Configure as variáveis de ambiente**

💻 Linux/Mac:
```bash
export OPENAI_API_KEY="sua-chave-openai-aqui"
export MYSQL_PASSWORD="sua-senha-mysql"
export POSTGRES_PASSWORD="sua-senha-postgres"
```

💻 Windows:
```bash
set OPENAI_API_KEY=sua-chave-openai-aqui
set MYSQL_PASSWORD=sua-senha-mysql
set POSTGRES_PASSWORD=sua-senha-postgres
```

Ou crie um arquivo `.env`:

`OPENAI_API_KEY`=sua-chave-openai-aqui

`MYSQL_PASSWORD`=sua-senha-mysql

`POSTGRES_PASSWORD`=sua-senha-postgres

`MYSQL_CONNECTION_STRING`=mysql://user:pass@host:port/db

`POSTGRES_CONNECTION_STRING`=postgresql://user:pass@host:port/db



📦 Requirements.txt
```
openai>=1.0.0
sqlalchemy>=2.0.0
pandas>=1.5.0
python-dotenv>=1.0.0
```


## Drivers de banco de dados
```
pymysql>=1.0.2          # MySQL
psycopg2-binary>=2.9.0  # PostgreSQL
pyodbc>=4.0.0           # SQL Server
cx-Oracle>=8.0.0        # Oracle (opcional)
```

# Documentação do projeto

## Visão Geral do Projeto

`Objetivo`: Criar um agente de IA que recebe perguntas em linguagem natural, traduz para SQL e executa em qualquer banco de dados configurado.

## Levantamento de requisitos
O levantamento de requisitos aborda o mapamento das funcionalidades da aplicação. 

### 📋 Requisitos Funcionais
* RF001 - Conexão Multi-Banco

    Descrição: O sistema deve conectar-se a diferentes SGBDs
    Critério de Aceitação:

    Suportar MySQL, PostgreSQL, SQLite, SQL Server
    Validar credenciais antes da conexão
    Exibir status de conexão claramente

    Prioridade: ALTA

* RF002 - Análise de Schema

    Descrição: Extrair e analisar estrutura do banco conectado
    Critério de Aceitação:

    Listar todas as tabelas e colunas
    Identificar chaves primárias e estrangeiras
    Detectar tipos de dados e constraints
    Obter dados de exemplo (3-5 registros por tabela)


    Prioridade: ALTA

* RF003 - Tradução Natural → SQL

    Descrição: Converter perguntas em português para SQL válido
    Critério de Aceitação:

    Interpretar perguntas em linguagem natural
    Gerar SQL sintaticamente correto
    Considerar dialetos específicos de cada SGBD
    Taxa de sucesso ≥ 80% em cenários básicos


    Prioridade: ALTA

* RF004 - Execução de Consultas

    Descrição: Executar SQL gerado e retornar resultados
    Critério de Aceitação:

    Executar queries sem alterar dados (somente SELECT)
    Retornar resultados em formato estruturado
    Limitar resultados para evitar sobrecarga
    Tratar erros de execução graciosamente


    Prioridade: ALTA

*RF005 - Interface de Usuário

    Descrição: Fornecer interface amigável para interação
    Critério de Aceitação:

    Interface web responsiva
    Chat conversacional
    Visualização de resultados em tabela
    Histórico de consultas


    Prioridade: MÉDIA

* RF006 - Exportação de Dados

    Descrição: Permitir exportar resultados
    Critério de Aceitação:

    Exportar para CSV, Excel, JSON
    Manter formatação original dos dados
    Incluir metadados da consulta


    Prioridade: BAIXA

* RF007 - Sugestões Inteligentes

    Descrição: Oferecer sugestões baseadas no schema
    Critério de Aceitação:

    Sugerir perguntas baseadas nas tabelas disponíveis
    Auto-completar nomes de tabelas/colunas
    Detectar intenções ambíguas e pedir clarificação


    Prioridade: BAIXA

* RF008 - Auditoria e Logs

    Descrição: Registrar todas as operações realizadas
    Critério de Aceitação:

    Log de todas as consultas executadas
    Registro de conexões e desconexões
    Tempo de resposta de cada operação


    Prioridade: MÉDIA


### 🔧 Requisitos Não-Funcionais
* RNF001 - Performance

    Descrição: Sistema deve responder rapidamente
    Métricas:

    Tempo de resposta ≤ 5 segundos para consultas simples
    Tempo de resposta ≤ 15 segundos para consultas complexas
    Suporte a até 50 consultas simultâneas


    Prioridade: ALTA

* RNF002 - Segurança

    Descrição: Proteger credenciais e dados sensíveis
    Critérios:

    Criptografar credenciais em repouso
    Não executar comandos DDL/DML destrutivos
    Sanitizar inputs para prevenir SQL Injection
    Autenticação obrigatória para acesso


    Prioridade: ALTA

* RNF003 - Escalabilidade

    Descrição: Sistema deve escalar conforme demanda
    Critérios:

    Arquitetura modular e extensível
    Suporte a pool de conexões
    Cache de schemas para reduzir latência


    Prioridade: MÉDIA

* RNF004 - Disponibilidade

    Descrição: Sistema deve estar sempre disponível
    Métricas:

    Uptime ≥ 99.5%
    Recuperação automática de falhas
    Timeout configurável para conexões


    Prioridade: MÉDIA

* RNF005 - Usabilidade

    Descrição: Interface intuitiva para usuários não-técnicos
    Critérios:

    Interface em português brasileiro
    Mensagens de erro claras e acionáveis
    Documentação integrada
    Tutoriais interativos


    Prioridade: ALTA

* RNF006 - Compatibilidade

    Descrição: Funcionar em diferentes ambientes
    Critérios:

    Compatível com Python 3.8+
    Suporte a principais navegadores web
    Funcionamento em Windows, Linux, macOS


    Prioridade: MÉDIA

* RNF007 - Manutenibilidade

    Descrição: Código fácil de manter e evoluir
    Critérios:

    Cobertura de testes ≥ 80%
    Documentação técnica completa
    Padrões de código consistentes
    Arquitetura modular


    Prioridade: MÉDIA

## 🏗️ Arquitetura do Sistema

Arquitetura em Camadas

|CAMADA DE APRESENTAÇÃO              |
| ---------------------------------- | 
| Interface Web (React/Flask)        |
| API REST                           |
| CLI Interface                      |

|CAMADA DE NEGÓCIO                   |
| ---------------------------------- | 
| Universal SQL Agent                |
| NL to SQL Translator               |
| Query Validator                    |
| Result Formatter                   |

|CAMADA DE DADOS                     |
| ---------------------------------- | 
| Database Connectors                |
| Schema Analyzer                    |
| Connection Pool Manager            |
| Cache Layer (Redis)                |

|CAMADA DE PERSISTÊNCIA              |
| ---------------------------------- | 
| PostgreSQL                         |
| SQL Server                         |
| MySQL                              |
| SQLite                             |

## Componentes Principais
1. Universal SQL Agent (Orquestrador)

Coordena todo o fluxo de processamento
Gerencia estado das conexões
Controla timeouts e retry logic

2. NL to SQL Translator (IA)

Integração com OpenAI GPT
Processamento de linguagem natural
Geração de SQL contextualizado

3. Database Connectors (Adaptadores)

Padrão Strategy para diferentes SGBDs
Abstração de diferenças entre dialetos
Pool de conexões otimizado

4. Schema Analyzer (Metadados)

Extração de estrutura do banco
Cache de metadados
Análise de relacionamentos

5. Security Layer (Segurança)

Validação de queries
Prevenção de SQL Injection
Controle de acesso

## Padrões de Design Utilizados

* Strategy Pattern: Para conectores de banco
* Factory Pattern: Para criação de conexões
* Adapter Pattern: Para diferentes interfaces de DB
* Observer Pattern: Para logs e auditoria
* Command Pattern: Para execução de queries
