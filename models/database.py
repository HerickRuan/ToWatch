import sqlite3

class Database:
    def __init__(self, db_name="midia.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS minha_lista (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                id_api_titulo TEXT,
                titulo TEXT,
                status TEXT, -- 'Assistir Depois' ou 'Assistido'
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
            )
        """)
        self.conn.commit()

    # CRUD usuários 
    def inserir_usuario(self, nome):
        self.cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
        self.conn.commit()

    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    def deletar_usuario(self, id_usuario):
        self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        self.conn.commit()

    # CRUD lista de mídias
    def inserir_midia(self, id_usuario, id_api, titulo, status):
        self.cursor.execute(
            "INSERT INTO minha_lista (id_usuario, id_api_titulo, titulo, status) VALUES (?, ?, ?, ?)",
            (id_usuario, id_api, titulo, status)
        )
        self.conn.commit()

    def listar_midias(self, id_usuario):
        self.cursor.execute("SELECT * FROM minha_lista WHERE id_usuario = ?", (id_usuario,))
        return self.cursor.fetchall()

    def deletar_midia(self, id_item):
        self.cursor.execute("DELETE FROM minha_lista WHERE id = ?", (id_item,))
        self.conn.commit()