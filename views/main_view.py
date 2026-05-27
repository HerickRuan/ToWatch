import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Opções: "dark", "light", "system"
ctk.set_default_color_theme("blue")

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ToWatch")
        self.geometry("800x600")

        style = ttk.Style(self)
        style.theme_use("default") 
        
        # Cores do corpo da tabela 
        style.configure("Treeview",
                        background="#2b2b2b",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#2b2b2b",
                        bordercolor="#343638",
                        borderwidth=0)

        # Cor da linha quando selecionada
        style.map('Treeview', background=[('selected', '#1f538d')])

        # Cores das colunas
        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        
        style.map("Treeview.Heading", background=[('active', '#3484F0')])

        # Barra de Navegação
        self.nav_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#1f1f1f")
        self.nav_frame.pack(side="top", fill="x")

        self.btn_usuarios = ctk.CTkButton(self.nav_frame, text="Usuários", width=120)
        self.btn_usuarios.pack(side="left", padx=10, pady=10)

        self.btn_buscar = ctk.CTkButton(self.nav_frame, text="Buscar Títulos", width=120)
        self.btn_buscar.pack(side="left", padx=10, pady=10)

        self.btn_lista = ctk.CTkButton(self.nav_frame, text="Minha Lista", width=120)
        self.btn_lista.pack(side="left", padx=10, pady=10)

        # Contêiner onde as telas vão aparecer
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)