import tkinter as tk

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Filmes e Séries")
        self.geometry("700x500")

        # Barra de Navegação
        self.nav_frame = tk.Frame(self, bg="#333", pady=10)
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_usuarios = tk.Button(self.nav_frame, text="Usuários", width=15)
        self.btn_usuarios.pack(side=tk.LEFT, padx=10)

        self.btn_buscar = tk.Button(self.nav_frame, text="Buscar Títulos", width=15)
        self.btn_buscar.pack(side=tk.LEFT, padx=10)

        self.btn_lista = tk.Button(self.nav_frame, text="Minha Lista", width=15)
        self.btn_lista.pack(side=tk.LEFT, padx=10)

        # Contêiner onde as telas vão aparecer
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=20)