import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox


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
    palavra = entry_palavra.get()
    chave = int(entry_chave.get())
    cifra = combobox_cifra.get()
    modo = 'cifrar'
    if cifra == 'Cifra de César':
        palavra_cifrada = cifra_de_cesar(palavra, chave, modo)
    elif cifra == 'Cifra de substituição':
        palavra_cifrada = cifra_de_substituicao(palavra, chave, modo)
    else:
        messagebox.showerror("Erro", "Opção inválida.")
        return
    lbl_palavra_original.configure(text=f"Palavra original: {palavra}")
    lbl_palavra_cifrada.configure(text=f"Palavra criptografada: {palavra_cifrada}")


def decriptar_palavra():
    palavra_cifrada = entry_palavra_cifrada.get()
    chave = int(entry_chave.get())
    cifra = combobox_cifra.get()
    modo = 'decifrar'
    if cifra == 'Cifra de César':
        palavra_decifrada = cifra_de_cesar(palavra_cifrada, chave, modo)
    elif cifra == 'Cifra de substituição':
        palavra_decifrada = cifra_de_substituicao(palavra_cifrada, chave, modo)
    else:
        messagebox.showerror("Erro", "Opção inválida.")
        return
    lbl_palavra_cifrada.configure(text=f"Palavra criptografada: {palavra_cifrada}")
    lbl_palavra_original.configure(text=f"Palavra original: {palavra_decifrada}")


def encriptar_texto():
    texto = text_original.get('1.0', tk.END)
    chave = int(entry_chave.get())
    cifra = combobox_cifra.get


def encriptar_arquivo():
caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo a ser criptografado")
chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
cifra = simpledialog.askstring(title="Escolha a cifra", prompt="'C' para cifra de César ou 'S' para cifra de substituição")
modo = 'cifrar'
if cifra.upper() == 'C':
with open(caminho_arquivo, 'r') as arquivo:
texto = arquivo.read()
texto_cifrado = cifra_de_cesar(texto, chave, modo)
elif cifra.upper() == 'S':
with open(caminho_arquivo, 'r') as arquivo:
texto = arquivo.read()
texto_cifrado = cifra_de_substituicao(texto, chave, modo)
else:
messagebox.showerror("Opção inválida", "Opção inválida.")
return
novo_caminho = filedialog.asksaveasfilename(title="Salvar arquivo criptografado", defaultextension=".txt")
with open(novo_caminho, 'w') as arquivo:
arquivo.write(texto_cifrado)
messagebox.showinfo("Arquivo criptografado", "O arquivo foi criptografado com sucesso.")

def decriptar_arquivo():
caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo criptografado")
chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
cifra = simpledialog.askstring(title="Escolha a cifra", prompt="'C' para cifra de César ou 'S' para cifra de substituição")
modo = 'decifrar'
if cifra.upper() == 'C':
with open(caminho_arquivo, 'r') as arquivo:
texto_cifrado = arquivo.read()
texto_decifrado = cifra_de_cesar(texto_cifrado, chave, modo)
elif cifra.upper() == 'S':
with open(caminho_arquivo, 'r') as arquivo:
texto_cifrado = arquivo.read()
texto_decifrado = cifra_de_substituicao(texto_cifrado, chave, modo)
else:
messagebox.showerror("Opção inválida", "Opção inválida.")
return
novo_caminho = filedialog.asksaveasfilename(title="Salvar arquivo descriptografado", defaultextension=".txt")
with open(novo_caminho, 'w') as arquivo:
arquivo.write(texto_decifrado)
messagebox.showinfo("Arquivo descriptografado", "O arquivo foi descriptografado com sucesso.")

import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

root = tk.Tk()
root.title("Criptografia")

def encriptar_palavra_gui():
palavra = simpledialog.askstring(title="Encriptação de palavra", prompt="Digite a palavra a ser criptografada:")
chave = int(simpledialog.askstring(title="Encriptação de palavra", prompt="Digite a chave de deslocamento ou a chave de substituição:"))
cifra = simpledialog.askstring(title="Escolha a cifra", prompt="'C' para cifra de César ou 'S' para cifra de substituição")
modo = 'c