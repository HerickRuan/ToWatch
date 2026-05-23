from models.database import Database
from views.main_view import MainView
import requests as rq

class MainController:
    def __init__(self):
        self.db = Database()
        self.view = MainView()
        
        # Conecta os botões da View aos métodos do Controller
        self.view.btn_usuarios.config(command=self.abrir_usuarios)
        self.view.btn_buscar.config(command=self.abrir_busca)
        self.view.btn_lista.config(command=self.abrir_lista)

    def abrir_usuarios(self):
        self.view.mostrar_mensagem("Usuários", "Aqui será aberta a janela de CRUD de Usuários.")
        # Lógica para abrir nova View de usuários aqui

    def abrir_busca(self):
        self.view.mostrar_mensagem("Busca API", "Aqui faremos a requisição GET para a API do TMDb.")
        # Lógica de integração com requests aqui

    def abrir_lista(self):
        self.view.mostrar_mensagem("Minha Lista", "Aqui listaremos os filmes do SQLite (Assistidos/Para Assistir).")
        # Lógica de consulta ao banco aqui

    def iniciar(self):
        self.view.mainloop()