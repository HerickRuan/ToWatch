import customtkinter as ctk
from tkinter import ttk

class UsuarioView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ctk.CTkLabel(self, text="Nome do Usuário:", font=("Arial", 14, "bold")).pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self, width=250, placeholder_text="Digite o nome...")
        self.entry_nome.pack(pady=5)
        
        self.btn_cadastrar = ctk.CTkButton(self, text="Cadastrar Usuário", fg_color="#4CAF50", hover_color="#45a049")
        self.btn_cadastrar.pack(pady=10)
        
        self.tree = ttk.Treeview(self, columns=("ID", "Nome"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.pack(pady=10, fill="both", expand=True)
        
        self.btn_deletar = ctk.CTkButton(self, text="Excluir Selecionado", fg_color="#f44336", hover_color="#d32f2f")
        self.btn_deletar.pack(pady=5)

class BuscaView(ctk.CTkFrame):
    def __init__(self, parent, usuarios):
        super().__init__(parent)
        
        ctk.CTkLabel(self, text="Usuário Ativo:", font=("Arial", 12)).pack(pady=2)
        
        valores_usuarios = [f"{u[0]} - {u[1]}" for u in usuarios]
        self.combo_usuario = ctk.CTkComboBox(self, values=valores_usuarios, width=200)
        self.combo_usuario.pack(pady=2)
        if valores_usuarios: 
            self.combo_usuario.set(valores_usuarios[0])
        
        ctk.CTkLabel(self, text="Buscar Filme, Série ou Anime:", font=("Arial", 14, "bold")).pack(pady=5)
        self.entry_busca = ctk.CTkEntry(self, width=350, placeholder_text="Ex: Breaking Bad, Naruto...")
        self.entry_busca.pack(pady=5)
        
        self.btn_buscar = ctk.CTkButton(self, text="Pesquisar", fg_color="#2196F3", hover_color="#0b7dda")
        self.btn_buscar.pack(pady=5)
        
        self.tree = ttk.Treeview(self, columns=("ID", "Título", "Tipo", "Ano"), show="headings")
        self.tree.heading("ID", text="ID API")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Ano", text="Ano")
        self.tree.pack(pady=5, fill="both", expand=True)
        
        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack(pady=10)
        
        self.btn_assistir_depois = ctk.CTkButton(frame_botoes, text="+ Assistir Depois", fg_color="#FF9800", hover_color="#e68a00")
        self.btn_assistir_depois.pack(side="left", padx=10)
        
        self.btn_assistido = ctk.CTkButton(frame_botoes, text="+ Já Assistido", fg_color="#4CAF50", hover_color="#45a049")
        self.btn_assistido.pack(side="left", padx=10)

class ListaView(ctk.CTkFrame):
    def __init__(self, parent, usuarios):
        super().__init__(parent)
        
        ctk.CTkLabel(self, text="Filtrar por Usuário:", font=("Arial", 14, "bold")).pack(pady=5)
        
        valores_usuarios = [f"{u[0]} - {u[1]}" for u in usuarios]
        self.combo_usuario = ctk.CTkComboBox(self, values=valores_usuarios, width=200)
        self.combo_usuario.pack(pady=5)
        
        self.tree = ttk.Treeview(self, columns=("ID_Item", "Título", "Status"), show="headings")
        self.tree.heading("ID_Item", text="ID Registro")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Status", text="Status")
        self.tree.pack(pady=10, fill="both", expand=True)
        
        self.btn_remover = ctk.CTkButton(self, text="Remover da Minha Lista", fg_color="#f44336", hover_color="#d32f2f")
        self.btn_remover.pack(pady=5)