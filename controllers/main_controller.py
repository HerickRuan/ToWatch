import tkinter as tk

from models.database import Database
from models.api_service import TMDBService
from views.main_view import MainView
from views.secondary_views import UsuarioView, BuscaView, ListaView
from tkinter import messagebox

class MainController:
    def __init__(self):
        self.db = Database()
        self.api = TMDBService()
        self.view = MainView()
        
        self.view.btn_usuarios.configure(command=self.abrir_usuarios)
        self.view.btn_buscar.configure(command=self.abrir_busca)
        self.view.btn_lista.configure(command=self.abrir_lista)

    def iniciar(self):
        self.view.mainloop()
    
    # ALTERNAR TELAS
    def limpar_conteudo(self):
        """Destrói todos os widgets do contêiner principal"""
        for widget in self.view.content_frame.winfo_children():
            widget.destroy()

    # CONTROLE DE USUÁRIOS 
    def abrir_usuarios(self):
        self.limpar_conteudo() # Limpa a tela anterior
        self.uv = UsuarioView(self.view.content_frame) # Cria no contêiner
        self.uv.pack(fill=tk.BOTH, expand=True) # Exibe o frame

        self.uv.entry_nome.bind("<Return>", self.cadastrar_usuario) # Aperta enter para cadastrar

        self.uv.btn_cadastrar.configure(command=self.cadastrar_usuario)
        self.uv.btn_deletar.configure(command=self.deletar_usuario)
        self.atualizar_tabela_usuarios()

    def cadastrar_usuario(self, event = None):
        nome = self.uv.entry_nome.get().strip()
        if nome:
            self.db.inserir_usuario(nome)
            self.uv.entry_nome.delete(0, 'end')
            self.atualizar_tabela_usuarios()
        else:
            messagebox.showwarning("Aviso", "O nome do usuário não pode ser vazio.")

    def deletar_usuario(self):
        selecionado = self.uv.tree.selection()
        if selecionado:
            id_user = self.uv.tree.item(selecionado[0])['values'][0]
            self.db.deletar_usuario(id_user)
            self.atualizar_tabela_usuarios()
        else:
            messagebox.showwarning("Aviso", "Selecione um usuário para excluir.")

    def atualizar_tabela_usuarios(self):
        for row in self.uv.tree.get_children():
            self.uv.tree.delete(row)
        for u in self.db.listar_usuarios():
            self.uv.tree.insert("", "end", values=(u[0], u[1]))

    # CONTROLE DE BUSCA - API 
    def abrir_busca(self):
        self.limpar_conteudo()
        usuarios = self.db.listar_usuarios()
        self.bv = BuscaView(self.view.content_frame, usuarios)
        self.bv.pack(fill=tk.BOTH, expand=True)

        self.bv.entry_busca.bind("<Return>", self.buscar_na_api) # Aperta enter para pesquisar

        self.bv.btn_buscar.configure(command=self.buscar_na_api)
        self.bv.btn_assistir_depois.configure(command=lambda: self.salvar_midia("Assistir Depois"))
        self.bv.btn_assistido.configure(command=lambda: self.salvar_midia("Assistido"))

    def buscar_na_api(self, event = None):
        query = self.bv.entry_busca.get().strip()
        resultados = self.api.buscar(query)
        for row in self.bv.tree.get_children():
            self.bv.tree.delete(row)
        for item in resultados:
            self.bv.tree.insert("", "end", values=(item["id"], item["titulo"], item["tipo"], item["ano"]))

    def salvar_midia(self, status):
        u_sel = self.bv.combo_usuario.get()
        m_sel = self.bv.tree.selection()
        if not u_sel or not m_sel:
            messagebox.showwarning("Erro", "Selecione um Usuário Ativo e um Título do resultado.")
            return
        
        id_usuario = u_sel.split(" - ")[0]
        valores_midia = self.bv.tree.item(m_sel[0])['values']
        self.db.inserir_midia(id_usuario, valores_midia[0], valores_midia[1], status)
        messagebox.showinfo("Sucesso", f"'{valores_midia[1]}' salvo em sua lista como '{status}'!")

    # CONTROLE DA MINHA LISTA 
    def abrir_lista(self):
        self.limpar_conteudo()
        usuarios = self.db.listar_usuarios()
        self.lv = ListaView(self.view.content_frame, usuarios)
        self.lv.pack(fill=tk.BOTH, expand=True)

        self.lv.combo_usuario.configure(command=self.atualizar_tabela_lista)
        self.lv.btn_remover.configure(command=self.remover_da_lista)

    def atualizar_tabela_lista(self, event=None):
        u_sel = self.lv.combo_usuario.get()
        if not u_sel: return
        id_usuario = u_sel.split(" - ")[0]
        
        for row in self.lv.tree.get_children():
            self.lv.tree.delete(row)
        for m in self.db.listar_midias(id_usuario):
            self.lv.tree.insert("", "end", values=(m[0], m[3], m[4]))

    def remover_da_lista(self):
        selecionado = self.lv.tree.selection()
        if selecionado:
            id_item = self.lv.tree.item(selecionado[0])['values'][0]
            self.db.deletar_midia(id_item)
            self.atualizar_tabela_lista()
        else:
            messagebox.showwarning("Aviso", "Selecione um item da tabela para remover.")