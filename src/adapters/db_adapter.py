import pyodbc

class SQLServerAdapter:
    def __init__(self, host, database, user, password):
        self.connection_string = (
            f'DRIVER={{ODBC Driver 18 for SQL Server}};'
            f'SERVER={host};'
            f'DATABASE={database};'
            f'UID={user};'
            f'PWD={password};'
            'Encrypt=no;'
            'TrustServerCertificate=yes;'
        )
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        try:
            results = self.cursor.fetchall()
            return results
        except pyodbc.ProgrammingError:
            return []  # no results

    def close(self):
        self.cursor.close()
        self.conn.close()
