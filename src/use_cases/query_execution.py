from adapters.db_adapter import SQLServerAdapter


def get_database_schema():
    db = SQLServerAdapter()
    return db.get_schema()

def run_query(query: str):
    db = SQLServerAdapter()
    return db.execute_query(query)
