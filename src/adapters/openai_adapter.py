import openai
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_sql_from_question(question: str, schema: dict, prompt_context: dict) -> str:
    system_msg = prompt_context.get("system_message", "Você é um assistente SQL.")
    instructions = "\n- " + "\n- ".join(prompt_context.get("instructions", []))

    prompt = f"""
Sistema: {system_msg}

Instruções adicionais para gerar SQL corretamente:
{instructions}

Base de dados:
{schema}

Pergunta do usuário:
{question}

Gere uma consulta SQL correspondente:
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0
        )
        sql = response.choices[0].message.content.strip()
        return sql.replace("```sql", "").replace("```", "").strip()
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar SQL: {e}")
