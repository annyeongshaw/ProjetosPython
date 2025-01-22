import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Produtos")

        # Lista de produtos
        self.produtos = []

        # Chama a tela de listagem ao iniciar
        self.tela_listagem()

    def tela_formulario(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Título
        tk.Label(self.root, text="Cadastrar Produto", font=("Arial", 16)).pack(pady=10)

        # Campos do formulário
        tk.Label(self.root, text="Nome do Produto:").pack()
        entry_nome = tk.Entry(self.root)
        entry_nome.pack()

        tk.Label(self.root, text="Descrição do Produto:").pack()
        entry_descricao = tk.Entry(self.root)
        entry_descricao.pack()

        tk.Label(self.root, text="Valor do Produto:").pack()
        entry_valor = tk.Entry(self.root)
        entry_valor.pack()

        tk.Label(self.root, text="Disponível para Venda:").pack()
        var_disponivel = tk.StringVar(value="sim")
        tk.Radiobutton(self.root, text="Sim", variable=var_disponivel, value="sim").pack()
        tk.Radiobutton(self.root, text="Não", variable=var_disponivel, value="nao").pack()

        # Botão para salvar o produto
        def salvar_produto():
            nome = entry_nome.get()
            descricao = entry_descricao.get()
            try:
                valor = float(entry_valor.get())
            except ValueError:
                messagebox.showerror("Erro", "O valor do produto deve ser numérico.")
                return
            disponivel = var_disponivel.get() == "sim"

            # Adicionar produto à lista
            self.produtos.append({
                "nome": nome,
                "descricao": descricao,
                "valor": valor,
                "disponivel": disponivel
            })
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            self.tela_listagem()

        tk.Button(self.root, text="Salvar Produto", command=salvar_produto).pack(pady=10)
        tk.Button(self.root, text="Voltar para a Listagem", command=self.tela_listagem).pack(pady=5)

    def tela_listagem(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Título
        tk.Label(self.root, text="Listagem de Produtos", font=("Arial", 16)).pack(pady=10)

        # Ordenar os produtos por valor do menor para o maior
        produtos_ordenados = sorted(self.produtos, key=lambda x: x["valor"])

        # Tabela de produtos
        frame_tabela = tk.Frame(self.root)
        frame_tabela.pack(pady=10)

        tk.Label(frame_tabela, text="Nome", width=20, borderwidth=1, relief="solid").grid(row=0, column=0)
        tk.Label(frame_tabela, text="Valor", width=20, borderwidth=1, relief="solid").grid(row=0, column=1)

        for i, produto in enumerate(produtos_ordenados):
            tk.Label(frame_tabela, text=produto["nome"], width=20, borderwidth=1, relief="solid").grid(row=i+1, column=0)
            tk.Label(frame_tabela, text=f'R$ {produto["valor"]:.2f}', width=20, borderwidth=1, relief="solid").grid(row=i+1, column=1)

        # Botão para cadastrar novo produto
        tk.Button(self.root, text="Cadastrar Novo Produto", command=self.tela_formulario).pack(pady=10)


# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
