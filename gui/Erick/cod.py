# Importando a biblioteca Tkinter
import tkinter as tk
import sqlite3

def criar_banco_de_dados():
    conexao = sqlite3.connect("lista_de_presenca")
    conexao.close()
    print("Banco de dados criado")


# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Aplicação")
janela.geometry("320x100+800+300")
janela.configure(bg="#004445")


# Adicionando um rótulo
rotulo = tk.Label(janela, text="aaaaaaaaaaa")
rotulo.pack() 

# Adicionando um botão
botao = tk.Button(janela, text="Criar banco de dados", command=criar_banco_de_dados)
botao.pack()

# Iniciando o loop principal da aplicação
janela.mainloop()