import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Filmes e Séries")
        self.geometry("500x400")

        # Container Principal
        self.frame = tk.Frame(self)
        self.frame.pack(pady=20)

        # Label de Título
        tk.Label(self.frame, text="Gerenciador de Mídia", font=("Arial", 16, "bold")).pack(pady=10)

        # Botões da Interface
        self.btn_usuarios = tk.Button(self.frame, text="Gerenciar Usuários", width=25)
        self.btn_usuarios.pack(pady=5)

        self.btn_buscar = tk.Button(self.frame, text="Buscar Títulos (API)", width=25)
        self.btn_buscar.pack(pady=5)

        self.btn_lista = tk.Button(self.frame, text="Minha Lista", width=25)
        self.btn_lista.pack(pady=5)

    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)