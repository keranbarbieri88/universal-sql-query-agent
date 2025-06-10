import streamlit as st
from use_cases import query_execution, query_generation
import json

st.set_page_config(page_title="Agente IA SQL", page_icon="🤖")
st.title("🤖 Agente IA para Consultas SQL")

# Entrada de perguntas
question = st.text_input("Digite sua pergunta em linguagem natural:")

# Carregar contexto do prompt (exemplo básico)
prompt_context = {
    "system_message": "Você é um assistente que gera consultas SQL para um banco de dados MySQL.",
    "instructions": [
        "Gere SQL válido para MySQL.",
        "Não retorne comandos perigosos como DELETE ou DROP."
    ]
}

if question:
    try:
        schema = query_execution.get_database_schema()
        st.write("Schema detectado:")
        st.json(schema)

        sql = query_generation.generate_query(question, schema, prompt_context)
        st.code(sql, language="sql")

        cols, results = query_execution.run_query(sql)
        if results:
            st.write("Resultados:")
            st.dataframe([dict(zip(cols, row)) for row in results])
        else:
            st.warning("Nenhum resultado encontrado.")
    except Exception as e:
        st.error(f"Erro: {e}")
