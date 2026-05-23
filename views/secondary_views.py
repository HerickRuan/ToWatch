import tkinter as tk
from tkinter import ttk

class UsuarioView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        tk.Label(self, text="Nome do Usuário:").pack(pady=5)
        self.entry_nome = tk.Entry(self, width=30)
        self.entry_nome.pack(pady=5)
        
        self.btn_cadastrar = tk.Button(self, text="Cadastrar Usuário", bg="#4CAF50", fg="white")
        self.btn_cadastrar.pack(pady=5)
        
        self.tree = ttk.Treeview(self, columns=("ID", "Nome"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.btn_deletar = tk.Button(self, text="Excluir Selecionado", bg="#f44336", fg="white")
        self.btn_deletar.pack(pady=5)

class BuscaView(tk.Frame):
    def __init__(self, parent, usuarios):
        super().__init__(parent)

        tk.Label(self, text="Usuário Ativo:").pack(pady=2)
        self.combo_usuario = ttk.Combobox(self, values=[f"{u[0]} - {u[1]}" for u in usuarios], state="readonly")
        self.combo_usuario.pack(pady=2)
        if usuarios: self.combo_usuario.current(0)
        
        tk.Label(self, text="Buscar Filme, Série ou Anime:").pack(pady=5)
        self.entry_busca = tk.Entry(self, width=40)
        self.entry_busca.pack(pady=5)
        
        self.btn_buscar = tk.Button(self, text="Pesquisar", bg="#2196F3", fg="white")
        self.btn_buscar.pack(pady=5)
        
        self.tree = ttk.Treeview(self, columns=("ID", "Título", "Tipo", "Ano"), show="headings")
        self.tree.heading("ID", text="ID API")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Ano", text="Ano")
        self.tree.pack(pady=5, fill=tk.BOTH, expand=True)
        
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        self.btn_assistir_depois = tk.Button(frame_botoes, text="+ Assistir Depois", bg="#FF9800", fg="white")
        self.btn_assistir_depois.pack(side=tk.LEFT, padx=10)
        self.btn_assistido = tk.Button(frame_botoes, text="+ Já Assistido", bg="#4CAF50", fg="white")
        self.btn_assistido.pack(side=tk.LEFT, padx=10)

class ListaView(tk.Frame):
    def __init__(self, parent, usuarios):
        super().__init__(parent)
        
        tk.Label(self, text="Usuário:").pack(pady=5)
        self.combo_usuario = ttk.Combobox(self, values=[f"{u[0]} - {u[1]}" for u in usuarios], state="readonly")
        self.combo_usuario.pack(pady=5)
        
        self.tree = ttk.Treeview(self, columns=("ID_Item", "Título", "Status"), show="headings")
        self.tree.heading("ID_Item", text="ID Registro")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Status", text="Status")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.btn_remover = tk.Button(self, text="Remover da Minha Lista", bg="#f44336", fg="white")
        self.btn_remover.pack(pady=5)