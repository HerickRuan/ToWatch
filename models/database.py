import sqlite3

class Database:
    def __init__(self, db_name="midia.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        # Tabela de Usuários
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)
        # Tabela de Mídias Salvas (Relaciona usuário e título)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS minha_lista (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                id_api_titulo TEXT,
                titulo TEXT,
                status TEXT, -- 'assistir_depois' ou 'assistido'
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
            )
        """)
        self.conn.commit()