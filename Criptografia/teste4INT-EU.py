import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog

def cifra_de_cesar(texto, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    tamanho_alfabeto = len(alfabeto)
    texto = texto.lower()
    texto_cifrado = ''
    for letra in texto:
        if letra in alfabeto:
            indice_letra = alfabeto.index(letra)
            if modo == 'cifrar':
                novo_indice = (indice_letra + chave) % tamanho_alfabeto
            elif modo == 'decifrar':
                novo_indice = (indice_letra - chave) % tamanho_alfabeto
            nova_letra = alfabeto[novo_indice]
            texto_cifrado += nova_letra
        else:
            texto_cifrado += letra
    return texto_cifrado


def cifra_de_substituicao(texto, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    tamanho_alfabeto = len(alfabeto)
    chave = chave.lower()
    texto = texto.lower()
    texto_cifrado = ''
    for letra in texto:
        if letra in alfabeto:
            indice_letra = alfabeto.index(letra)
            if modo == 'cifrar':
                nova_letra = chave[indice_letra]
            elif modo == 'decifrar':
                novo_indice = chave.find(letra)
                nova_letra = alfabeto[novo_indice]
            texto_cifrado += nova_letra
        else:
            texto_cifrado += letra
    return texto_cifrado


def encriptar_palavra():
    palavra = palavra_entry.get()
    chave = int(chave_entry.get())
    cifra = cifra_entry.get()
    modo = 'cifrar'
    if cifra.upper() == 'C':
        palavra_cifrada = cifra_de_cesar(palavra, chave, modo)
    elif cifra.upper() == 'S':
        palavra_cifrada = cifra_de_substituicao(palavra, chave, modo)
    else:
        messagebox.showerror("Erro", "Opção inválida.")
        return
    resultado_text.delete('1.0', END)
    resultado_text.insert(END, f"Palavra original: {palavra}\nPalavra criptografada: {palavra_cifrada}")


def decriptar_palavra():
    palavra_cifrada = palavra_entry.get()
    chave = int(chave_entry.get())
    cifra = cifra_entry.get()
    modo = 'decifrar'
    if cifra.upper() == 'C':
        palavra_decifrada = cifra_de_cesar(palavra_cifrada, chave, modo)
    elif cifra.upper() == 'S':
        palavra_decifrada = cifra_de_substituicao(palavra_cifrada, chave, modo)
    else:
        messagebox.showerror("Erro", "Opção inválida.")
        return
    resultado_text.delete('1.0', END)
    resultado_text.insert(END, f"Palavra criptografada: {palavra_cifrada}\nPalavra original: {palavra_decifrada}")


def encriptar_texto():
    texto = texto_entry.get('1.0', END)
    chave = int(chave_entry.get())
    cifra = cifra_entry.get()
    modo = 'cifrar'
    if cifra.upper() == 'C':
        texto_cifrado = cifra_de_cesar(texto, chave, modo)
    elif cifra.upper() == 'S':
        texto_cifrado = cifra_de_substituicao(texto, chave, modo)
    else:
        label_resultado.config(text='Opção inválida.', fg='red')
        return
    texto_cifrado = f'Texto criptografado:\n{texto_cifrado} \nTexto criptografado: {texto_cifrado}'
    label_resultado.config(text=texto_cifrado, fg='black')
    resultado_text.delete(1.0, END)

def decriptar_texto():
    texto_cifrado = texto_entry.get("1.0", END)
    chave = int(chave_entry.get())
    cifra = cifra_entry.get()
    modo = 'decifrar'
    if cifra.upper() == 'C':
        texto_decifrado = cifra_de_cesar(texto_cifrado, chave, modo)
    elif cifra.upper() == 'S':
        texto_decifrado = cifra_de_substituicao(texto_cifrado, chave, modo)
    else:
        label_resultado.config(text='Opção inválida.', fg='red')
        return
    resultado_text.delete(1.0, END)
    resultado_text.insert(END, f"Texto criptografado: {texto_cifrado}\nTexto original: {texto}")
    label_resultado.config(text=texto_decifrado, fg='black')

def encriptar_arquivo(caminho_arquivo):
    caminho_arquivo = arquivo_entry.get()
    chave = int(chave_entry.get())
    cifra = cifra_entry.get()
    modo = 'cifrar'
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            texto = arquivo.read()
            if cifra.upper() == 'C':
                texto_cifrado = cifra_de_cesar(texto, chave, modo)
            elif cifra.upper() == 'S':
                texto_cifrado = cifra_de_substituicao(texto, chave, modo)
            else:
                messagebox.showerror("Erro", "Opção inválida.")
                return
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(texto_cifrado)
            messagebox.showinfo("Sucesso", "Arquivo criptografado com sucesso!")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def decriptar_arquivo():
    caminho_arquivo = arquivo_entry.get()
    chave = int(chave_entry.get())
    cifra = cifra_entry.get()
    modo = 'decifrar'
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            texto_cifrado = arquivo.read()
            if cifra.upper() == 'C':
                texto_decifrado = cifra_de_cesar(texto_cifrado, chave, modo)
            elif cifra.upper() == 'S':
                texto_decifrado = cifra_de_substituicao(texto_cifrado, chave, modo)
            else:
                messagebox.showerror("Erro", "Opção inválida.")
                return
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(texto_decifrado)
            messagebox.showinfo("Sucesso", "Arquivo descriptografado com sucesso!")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def selecionar_opcao():
    opcao = int(opcao_var.get())
    if opcao == 1:
        palavra = palavra_entry.get()
        # chamar função para criptografar palavra
    elif opcao == 2:
        palavra = palavra_entry.get()
        # chamar função para descriptografar palavra
    elif opcao == 3:
        texto = texto_entry.get("1.0", "end-1c")
        # chamar função para criptografar texto
    elif opcao == 4:
        texto = texto_entry.get("1.0", "end-1c")
        # chamar função para descriptografar texto
    elif opcao == 5:
        arquivo = arquivo_entry.get()
        # chamar função para criptografar arquivo
    elif opcao == 6:
        arquivo = arquivo_entry.get()
        # chamar função para descriptografar arquivo


root = tk.Tk()
root.title("Criptografia")

# Criando as opções de seleção
opcao_var = tk.StringVar()
opcao_label = tk.Label(root, text="Selecione uma opção:")
opcao_label.pack()
opcao1 = tk.Radiobutton(root, text="1 - Criptografar uma palavra", variable=opcao_var, value=1)
opcao1.pack()
opcao2 = tk.Radiobutton(root, text="2 - Descriptografar uma palavra", variable=opcao_var, value=2)
opcao2.pack()
opcao3 = tk.Radiobutton(root, text="3 - Criptografar um texto", variable=opcao_var, value=3)
opcao3.pack()
opcao4 = tk.Radiobutton(root, text="4 - Descriptografar um texto", variable=opcao_var, value=4)
opcao4.pack()
opcao5 = tk.Radiobutton(root, text="5 - Criptografar um arquivo", variable=opcao_var, value=5)
opcao5.pack()
opcao6 = tk.Radiobutton(root, text="6 - Descriptografar um arquivo", variable=opcao_var, value=6)
opcao6.pack()

# Widget para inserir a palavra
palavra_label = tk.Label(root, text="Digite uma palavra:")
palavra_entry = tk.Entry(root)

# Widget para inserir a chave
chave_label = tk.Label(root, text="Digite a chave de deslocamento ou a chave de substituição:")
chave_entry = tk.Entry(root)

# Widgets para selecionar o tipo de cifra
cifra_label = tk.Label(root, text="Selecione o tipo de cifra:")
cifra_var = tk.StringVar(value="Cifra de César")
cifra_cesar = tk.Radiobutton(root, text="Cifra de César", variable=cifra_var, value="Cifra de César")
cifra_substituicao = tk.Radiobutton(root, text="Cifra de Substituição", variable=cifra_var, value="Cifra de Substituição")

# Botão para executar a cifragem
encriptar_button = tk.Button(root, text="Criptografar", command=encriptar_palavra)

# Widget para exibir o resultado
resultado_label = tk.Label(root)

# Entrada de dados
palavra_label = tk.Label(root, text="Palavra:")
palavra_entry = tk.Entry(root)
texto_label = tk.Label(root, text="Texto:")
texto_entry = tk.Text(root, height=5)
arquivo_label = tk.Label(root, text="Arquivo:")
arquivo_entry = tk.Entry(root)

# Botão para executar a seleção
selecionar_button = tk.Button(root, text="Selecionar", command=selecionar_opcao)

# Organização dos widgets na janela usando o gerenciador de layout grid
opcao1.grid(row=1, column=0, sticky=tk.W)
opcao2.grid(row=2, column=0, sticky=tk.W)
opcao3.grid(row=3, column=0, sticky=tk.W)
opcao4.grid(row=4, column=0, sticky=tk.W)
opcao5.grid(row=5, column=0, sticky=tk.W)
opcao6.grid(row=6, column=0, sticky=tk.W)

chave_label.grid(row=2, column=1, sticky=tk.W)
chave_entry.grid(row=2, column=2)

cifra_label.grid(row=3, column=1, sticky=tk.W)
cifra_cesar.grid(row=4, column=1, sticky=tk.W)
cifra_substituicao.grid(row=5, column=1, sticky=tk.W)

encriptar_button.grid(row=6, column=2)

resultado_label.grid(row=7, column=1, sticky=tk.W)

texto_label.grid(row=8, column=1, sticky=tk.W)
texto_entry.grid(row=9, column=1)

arquivo_label.grid(row=10, column=1, sticky=tk.W)
arquivo_entry.grid(row=11, column=1)

selecionar_button.grid(row=12, column=1, sticky=tk.W)

encriptar_palavra_button.grid(row=1, column=3)
decriptar_palavra_button.grid(row=2, column=3)
encriptar_texto_button.grid(row=9, column=3)
decriptar_texto_button.grid(row=10, column=3)
encriptar_arquivo_button.grid(row=11, column=3)
salvar_arquivo_button.grid(row=12, column=3)

root.mainloop()




# root = tk.Tk()
# root.title("Criptografia")

# # Criando as opções de seleção
# opcao_var = tk.StringVar()
# opcao_label = tk.Label(root, text="Selecione uma opção:")
# opcao_label.pack()
# opcao1 = tk.Radiobutton(root, text="1 - Criptografar uma palavra", variable=opcao_var, value=1)
# opcao1.pack()
# opcao2 = tk.Radiobutton(root, text="2 - Descriptografar uma palavra", variable=opcao_var, value=2)
# opcao2.pack()
# opcao3 = tk.Radiobutton(root, text="3 - Criptografar um texto", variable=opcao_var, value=3)
# opcao3.pack()
# opcao4 = tk.Radiobutton(root, text="4 - Descriptografar um texto", variable=opcao_var, value=4)
# opcao4.pack()
# opcao5 = tk.Radiobutton(root, text="5 - Criptografar um arquivo", variable=opcao_var, value=5)
# opcao5.pack()
# opcao6 = tk.Radiobutton(root, text="6 - Descriptografar um arquivo", variable=opcao_var, value=6)
# opcao6.pack()

# # Widget para inserir a palavra
# palavra_label = tk.Label(root, text="Digite uma palavra:")
# palavra_entry = tk.Entry(root)

# # Widget para inserir a chave
# chave_label = tk.Label(root, text="Digite a chave de deslocamento ou a chave de substituição:")
# chave_entry = tk.Entry(root)

# # Widgets para selecionar o tipo de cifra
# cifra_label = tk.Label(root, text="Selecione o tipo de cifra:")
# cifra_var = tk.StringVar(value="Cifra de César")
# cifra_cesar = tk.Radiobutton(root, text="Cifra de César", variable=cifra_var, value="Cifra de César")
# cifra_substituicao = tk.Radiobutton(root, text="Cifra de Substituição", variable=cifra_var, value="Cifra de Substituição")

# # Botão para executar a cifragem
# encriptar_button = tk.Button(root, text="Criptografar", command=encriptar_palavra)

# # Widget para exibir o resultado
# resultado_label = tk.Label(root)

# # Entrada de dados
# palavra_label = tk.Label(root, text="Palavra:")
# palavra_label.pack()
# palavra_entry = tk.Entry(root)
# palavra_entry.pack()

# texto_label = tk.Label(root, text="Texto:")
# texto_label.pack()
# texto_entry = tk.Text(root, height=5)
# texto_entry.pack()

# arquivo_label = tk.Label(root, text="Arquivo:")
# arquivo_label.pack()
# arquivo_entry = tk.Entry(root)
# arquivo_entry.pack()

# # Botão para executar a seleção
# selecionar_button = tk.Button(root, text="Selecionar", command=selecionar_opcao)
# selecionar_button.pack()

# # Organização dos widgets na janela usando o gerenciador de layout grid
# palavra_label.grid(row=0, column=0, sticky=W)
# palavra_entry.grid(row=0, column=1)
# chave_label.grid(row=1, column=0, sticky=W)
# chave_entry.grid(row=1, column=1)
# cifra_label.grid(row=2, column=0, sticky=W)
# cifra_entry.grid(row=2, column=1)
# encriptar_palavra_button.grid(row=3, column=0)
# decriptar_palavra_button.grid(row=3, column=1)
# texto_label.grid(row=4, column=0, sticky=W)
# texto_entry.grid(row=4, column=1)
# encriptar_texto_button.grid(row=5, column=0)
# decriptar_texto_button.grid(row=5, column=1)
# arquivo_label.grid(row=6, column=0, sticky=W)
# arquivo_entry.grid(row=6, column=1)
# encriptar_arquivo_button.grid(row=7, column=0)
# salvar_arquivo_button.grid(row=7, column=1)
# resultado_label.grid(row=8, column=0, sticky=W)
# resultado_text.grid(row=9, columnspan=2)
# label_resultado.grid(row=10, columnspan=2)

# root.mainloop()
