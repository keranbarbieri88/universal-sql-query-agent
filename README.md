# Universal SQL Query Agent 🤖

Um agente de IA que traduz perguntas em linguagem natural para consultas SQL e as executa em bancos de dados configurados.

## 🚀 Funcionalidades

- Interface web intuitiva para entrada de perguntas
- Tradução automática de linguagem natural para SQL
- Suporte a múltiplos bancos de dados (MySQL, PostgreSQL, SQL Server)
- Visualização de resultados em formato tabular
- Geração segura de queries SQL
- Interface amigável e responsiva

## 📋 Pré-requisitos

- Python 3.8+
- Google Chrome (ou outro navegador moderno)
- Conexão com banco de dados configurada
- Chave de API da OpenAI

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/universal-sql-query-agent.git
cd universal-sql-query-agent
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```env
OPENAI_API_KEY=sua_chave_api_aqui
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_DB=seu_banco
```

## 🚀 Como Executar

### Windows
Execute o arquivo `run.bat` com duplo clique ou via terminal:
```bash
.\run.bat
```

### Linux/Mac
Execute o script shell:
```bash
chmod +x run.sh
./run.sh
```

### Execução Manual
1. Inicie o servidor Streamlit:
```bash
streamlit run src/interface/app.py
```
2. Abra seu navegador e acesse: `http://localhost:8501`

## 📁 Estrutura do Projeto

```
universal-sql-query-agent/
├── src/
│   ├── adapters/         # Adaptadores para diferentes serviços
│   ├── config/           # Configurações da aplicação
│   ├── interface/        # Interface web (Streamlit)
│   └── use_cases/        # Casos de uso da aplicação
├── .env                  # Variáveis de ambiente
├── requirements.txt      # Dependências do projeto
├── run.bat              # Script de execução (Windows)
└── run.sh               # Script de execução (Linux/Mac)
```

## 💻 Como Usar

1. Acesse a interface web em `http://localhost:8501`
2. Digite sua pergunta em linguagem natural no campo de texto
3. O sistema irá:
   - Analisar sua pergunta
   - Gerar a consulta SQL correspondente
   - Executar a consulta no banco de dados
   - Exibir os resultados em formato tabular

## 🔒 Segurança

- Todas as queries são validadas antes da execução
- Comandos perigosos (DELETE, DROP, etc.) são bloqueados
- Credenciais do banco de dados são armazenadas de forma segura
- Conexões são gerenciadas com timeout

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Contato

Seu Nome - [@seu_twitter](https://twitter.com/seu_twitter) - email@exemplo.com

Link do Projeto: [https://github.com/seu-usuario/universal-sql-query-agent](https://github.com/seu-usuario/universal-sql-query-agent)


