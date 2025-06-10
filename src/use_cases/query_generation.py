from adapters.openai_adapter import generate_sql_from_question

def generate_query(question: str, schema: dict, prompt_context: dict) -> str:
    return generate_sql_from_question(question, schema, prompt_context)
