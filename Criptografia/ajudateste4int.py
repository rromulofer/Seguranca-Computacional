from tkinter import *
from tkinter import messagebox

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
    resultado_text.delete(1.0, END)
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
    resultado_text.delete(1.0, END)
    resultado_text.insert(END, f"Palavra criptografada: {palavra_cifrada}\nPalavra original: {palavra_decifrada}")


def encriptar_texto():
    texto = texto_entry.get("1.0", END)
    chave = int(chave_entry.get())
    cifra = cifra_entry.get()
    modo = 'cifrar'
    if cifra.upper() == 'C':
        texto_cif








import tkinter as tk

def encriptar_texto():
    def cifrar():
        texto = texto_original.get('1.0', tk.END).strip()
        chave = int(entry_chave.get())
        cifra = var_cifra.get()
        modo = 'cifrar'
        if cifra == 'Cifra de César':
            texto_cifrado = cifra_de_cesar(texto, chave, modo)
        elif cifra == 'Cifra de Substituição':
            texto_cifrado = cifra_de_substituicao(texto, chave, modo)
        else:
            label_resultado.config(text='Opção inválida.', fg='red')
            return
        texto_cifrado = f'Texto criptografado:\n{texto_cifrado}'
        label_resultado.config(text=texto_cifrado, fg='black')

    window = tk.Tk()
    window.title('Encriptar Texto')

    label_instrucoes = tk.Label(window, text='Insira o texto, a chave e selecione o tipo de cifra.')
    label_instrucoes.pack()

    label_texto = tk.Label(window, text='Texto:')
    label_texto.pack()
    texto_original = tk.Text(window, height=5, width=30)
    texto_original.pack()

    label_chave = tk.Label(window, text='Chave:')
    label_chave.pack()
    entry_chave = tk.Entry(window)
    entry_chave.pack()

    var_cifra = tk.StringVar(value='Cifra de César')
    label_cifra = tk.Label(window, text='Tipo de Cifra:')
    label_cifra.pack()
    opcoes_cifra = ['Cifra de César', 'Cifra de Substituição']
    menu_cifra = tk.OptionMenu(window, var_cifra, *opcoes_cifra)
    menu_cifra.pack()

    botao_cifrar = tk.Button(window, text='Cifrar', command=cifrar)
    botao_cifrar.pack()

    label_resultado = tk.Label(window, text='', fg='black')
    label_resultado.pack()

    window.mainloop()









# Para utilizar a interface gráfica Tkinter para inserção de dados, você precisa substituir as chamadas para a função input() por widgets gráficos fornecidos pelo Tkinter, como Entry, Label, Button, etc.

# Além disso, você precisa criar uma janela usando a classe Tk e organizar os widgets usando gerenciadores de layout, como pack, grid ou place.

# Aqui está um exemplo de como você poderia criar uma interface gráfica básica para a função encriptar_palavra():

import tkinter as tk
from functools import partial

def encriptar_palavra():
    palavra = palavra_entry.get()
    chave = int(chave_entry.get())
    cifra = cifra_var.get()
    modo = 'cifrar'
    if cifra == 'Cifra de César':
        palavra_cifrada = cifra_de_cesar(palavra, chave, modo)
    elif cifra == 'Cifra de Substituição':
        palavra_cifrada = cifra_de_substituicao(palavra, chave, modo)
    else:
        print("Opção inválida.")
        return
    resultado_label.config(text=f"Palavra original: {palavra}\nPalavra criptografada: {palavra_cifrada}")

root = tk.Tk()
root.title("Criptografia")

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

# Organização dos widgets na janela usando o gerenciador de layout grid
palavra_label.grid(row=0, column=0, sticky="w")
palavra_entry.grid(row=1, column=0)
chave_label.grid(row=2, column=0, sticky="w")
chave_entry.grid(row=3, column=0)
cifra_label.grid(row=4, column=0, sticky="w")
cifra_cesar.grid(row=5, column=0, sticky="w")
cifra_substituicao.grid(row=6, column=0, sticky="w")
encriptar_button.grid(row=7, column=0)
resultado_label.grid(row=8, column=0)

root.mainloop()


# Este código cria uma janela com um formulário para inserir uma palavra, uma chave e selecionar o tipo de cifra (Cifra de César ou Cifra de Substituição). Quando o botão "Criptografar" é clicado, a função encriptar_palavra()











import tkinter as tk
import os


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
        resultado_label.config(text='Opção inválida.')
        return
    resultado_label.config(text=f'Palavra original: {palavra}\nPalavra criptografada: {palavra_cifrada}')


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
        resultado_label.config(text='Opção inválida.')
        return
    resultado_label.config(text=f'Palavra criptografada: {palavra_cifrada}\nPalavra original: {palavra_decifrada}')


def encriptar_texto():
    texto = texto_entry.get('1.0', tk.END)
    chave = int(chave_entry.get())
    cifra = cifra_entry.get()
    modo = 'cifrar'
    if cifra.upper() == 'C':
        texto_cifrado = cifra_de_cesar(texto, chave, modo)
    elif cifra.upper() == 'S':
        texto_cifrado = cifra_de_substituicao(texto_cifrado = cifra_de_substituicao(texto, chave, modo)
    else:
        print("Opção inválida.")
        return

    print("Texto original:\n", texto)
    print("Texto criptografado:\n", texto_cifrado)

def decriptar_arquivo():
    caminho_arquivo = input("Digite o caminho do arquivo: ")
    chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
    cifra = input("Digite 'C' para cifra de César ou 'S' para cifra de substituição: ")
    modo = 'decifrar'
    try:
    with open(caminho_arquivo, 'r') as arquivo:
    texto_cifrado = arquivo.read()
    except FileNotFoundError:
    print("Arquivo não encontrado.")
    return

if cifra.upper() == 'C':
    texto_decifrado = cifra_de_cesar(texto_cifrado, chave, modo)
elif cifra.upper() == 'S':
    texto_decifrado = cifra_de_substituicao(texto_cifrado, chave, modo)
else:
    print("Opção inválida.")
    return

print("Texto criptografado:\n", texto_cifrado)
print("Texto original:\n", texto_decifrado)
