import tkinter as tk
from tkinter import ttk, filedialog

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
    chave_str = chave_entry.get()
    cifra = cifra_combobox.get()
    modo = 'cifrar'

    if chave_str:
        try:
            chave = int(chave_str)
        except ValueError:
            resultado_text.delete("1.0", tk.END)
            resultado_text.insert(tk.END, "Chave inválida.")
            return
    else:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Chave não informada.")
        return
    
    if cifra.upper() == 'C':
        palavra_cifrada = cifra_de_cesar(palavra, chave, modo)
    elif cifra.upper() == 'S':
        palavra_cifrada = cifra_de_substituicao(palavra, chave, modo)
    else:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Opção inválida.")
        return
    
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, "Palavra original: {}\n".format(palavra))
    resultado_text.insert(tk.END, "Palavra criptografada: {}".format(palavra_cifrada))



def decriptar_palavra():
    palavra_cifrada = palavra_entry.get()
    chave = int(chave_entry.get())
    cifra = cifra_combobox.get()
    modo = 'decifrar'
    if cifra.upper() == 'C':
        palavra_decifrada = cifra_de_cesar(palavra_cifrada, chave, modo)
    elif cifra.upper() == 'S':
        palavra_decifrada = cifra_de_substituicao(palavra_cifrada, chave, modo)
    else:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Opção inválida.")
        return
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, "Palavra criptografada: {}\n".format(palavra_cifrada))
    resultado_text.insert(tk.END, "Palavra original: {}".format(palavra_decifrada))


def encriptar_texto():
    texto = texto_entry.get("1.0", tk.END).strip()
    chave = int(chave_entry.get())
    cifra = cifra_combobox.get()
    modo = 'cifrar'

    if cifra.upper() == 'C':
        texto_cifrado = cifra_de_cesar(texto, chave, modo)
    elif cifra.upper() == 'S':
        texto_cifrado = cifra_de_substituicao(texto, chave, modo)
    else:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Opção inválida.")
        return
    
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, "Texto original:\n{}\n".format(texto))
    resultado_text.insert(tk.END, "Texto criptografado:\n{}".format(texto_cifrado))

def decriptar_texto():
    texto_cifrado = texto_entry.get("1.0", tk.END).strip()
    chave = int(chave_entry.get())
    cifra = cifra_combobox.get()
    modo = 'decifrar'

    if cifra.upper() == 'C':
        texto_decifrado = cifra_de_cesar(texto_cifrado, chave, modo)
    elif cifra.upper() == 'S':
        texto_decifrado = cifra_de_substituicao(texto_cifrado, chave, modo)
    else:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Opção inválida.")
        return

    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, "Texto criptografado:\n{}\n".format(texto_cifrado))
    resultado_text.insert(tk.END, "Texto original:\n{}".format(texto_decifrado))

def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
    arquivo_entry.delete(0, tk.END)
    arquivo_entry.insert(tk.END, arquivo)

def encriptar_arquivo():
    caminho_arquivo = arquivo_entry.get()
    chave = int(chave_entry.get())
    cifra = cifra_combobox.get()
    modo = 'cifrar'
    
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            texto = arquivo.read()
            
            if cifra.upper() == 'C':
                texto_cifrado = cifra_de_cesar(texto, chave, modo)
            elif cifra.upper() == 'S':
                texto_cifrado = cifra_de_substituicao(texto, chave, modo)
            else:
                resultado_text.delete("1.0", tk.END)
                resultado_text.insert(tk.END, "Opção inválida.")
                return
        
        caminho_arquivo_cifrado = caminho_arquivo + '.cifrado'
        
        with open(caminho_arquivo_cifrado, 'w') as arquivo_cifrado:
            arquivo_cifrado.write(texto_cifrado)
        
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Arquivo criptografado com sucesso.")
    
    except FileNotFoundError:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Arquivo não encontrado.")


def decriptar_arquivo():
    caminho_arquivo = arquivo_entry.get()
    chave = int(chave_entry.get())
    cifra = cifra_combobox.get()
    modo = 'decifrar'
    
    try:
        with open(caminho_arquivo, 'r') as arquivo_cifrado:
            texto_cifrado = arquivo_cifrado.read()
            
            if cifra.upper() == 'C':
                texto_decifrado = cifra_de_cesar(texto_cifrado, chave, modo)
            elif cifra.upper() == 'S':
                texto_decifrado = cifra_de_substituicao(texto_cifrado, chave, modo)
            else:
                resultado_text.delete("1.0", tk.END)
                resultado_text.insert(tk.END, "Opção inválida.")
                return
        
        caminho_arquivo_decifrado = caminho_arquivo[:-8]
        
        with open(caminho_arquivo_decifrado, 'w') as arquivo_decifrado:
            arquivo_decifrado.write(texto_decifrado)
        
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Arquivo descriptografado com sucesso.")
    
    except FileNotFoundError:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Arquivo não encontrado.")


def opcao_selecionada(event):
    opcao = opcao_combobox.get()
    
    if opcao == '1':
        frame_palavra.grid()
        frame_texto.grid_remove()
        frame_arquivo.grid_remove()
    elif opcao == '2':
        frame_palavra.grid()
        frame_texto.grid_remove()
        frame_arquivo.grid_remove()
    elif opcao == '3':
        frame_texto.grid()
        frame_palavra.grid_remove()
        frame_arquivo.grid_remove()
    elif opcao == '4':
        frame_texto.grid()
        frame_palavra.grid_remove()
        frame_arquivo.grid_remove()
    elif opcao == '5':
        frame_arquivo.grid()
        frame_palavra.grid_remove()
        frame_texto.grid_remove()
    elif opcao == '6':
        frame_arquivo.grid()
        frame_palavra.grid_remove()
        frame_texto.grid_remove()


root = tk.Tk()
root.title("Criptografia")
root.geometry("400x300")

opcao_label = tk.Label(root, text="Opção:")
opcao_label.grid(row=0, column=0)

opcao_combobox = tk.ttk.Combobox(root, values=["1 - Criptografar palavra", "2 - Descriptografar palavra",
"3 - Criptografar texto", "4 - Descriptografar texto",
"5 - Criptografar arquivo", "6 - Descriptografar arquivo"])
opcao_combobox.bind("<<ComboboxSelected>>", opcao_selecionada)
opcao_combobox.grid(row=0, column=1)

frame_palavra = tk.Frame(root)

palavra_label = tk.Label(frame_palavra, text="Palavra:")
palavra_label.grid(row=0, column=0)

palavra_entry = tk.Entry(frame_palavra)
palavra_entry.grid(row=0, column=1)

chave_label = tk.Label(frame_palavra, text="Chave:")
chave_label.grid(row=1, column=0)

chave_entry = tk.Entry(frame_palavra)
chave_entry.grid(row=1, column=1)

cifra_label = tk.Label(frame_palavra, text="Cifra:")
cifra_label.grid(row=2, column=0)

cifra_combobox = tk.ttk.Combobox(frame_palavra, values=["Cifra de César", "Cifra de Substituição"])
cifra_combobox.grid(row=2, column=1)

encriptar_palavra_button = tk.Button(frame_palavra, text="Criptografar", command=encriptar_palavra)
encriptar_palavra_button.grid(row=3, columnspan=2)

decriptar_palavra_button = tk.Button(frame_palavra, text="Descriptografar", command=decriptar_palavra)
decriptar_palavra_button.grid(row=4, columnspan=2)

frame_texto = tk.Frame(root)

texto_label = tk.Label(frame_texto, text="Texto:")
texto_label.grid(row=0, column=0)

texto_entry = tk.Text(frame_texto, height=4, width=30)
texto_entry.grid(row=0, column=1)

chave_label = tk.Label(frame_texto, text="Chave:")
chave_label.grid(row=1, column=0)

chave_entry = tk.Entry(frame_texto)
chave_entry.grid(row=1, column=1)

cifra_label = tk.Label(frame_texto, text="Cifra:")
cifra_label.grid(row=2, column=0)

cifra_combobox = tk.ttk.Combobox(frame_texto, values=["Cifra de César", "Cifra de Substituição"])
cifra_combobox.grid(row=2, column=1)

encriptar_texto_button = tk.Button(frame_texto, text="Criptografar", command=encriptar_texto)
encriptar_texto_button.grid(row=3, columnspan=2)

decriptar_texto_button = tk.Button(frame_texto, text="Descriptografar", command=decriptar_texto)
decriptar_texto_button.grid(row=4, columnspan=2)

frame_arquivo = tk.Frame(root)

arquivo_label = tk.Label(frame_arquivo, text="Arquivo:")
arquivo_label.grid(row=0, column=0)

arquivo_entry = tk.Entry(frame_arquivo)
arquivo_entry.grid(row=0, column=1)

selecionar_arquivo_button = tk.Button(frame_arquivo, text="Selecionar", command=selecionar_arquivo)
selecionar_arquivo_button.grid(row=0, column=2)

chave_label = tk.Label(frame_arquivo, text="Chave:")
chave_label.grid(row=1, column=0)

chave_entry = tk.Entry(frame_arquivo)
chave_entry.grid(row=1, column=1)

cifra_label = tk.Label(frame_arquivo, text="Cifra:")
cifra_label.grid(row=2, column=0)

cifra_combobox = tk.ttk.Combobox(frame_arquivo, values=["Cifra de César", "Cifra de Substituição"])
cifra_combobox.grid(row=2, column=1)

encriptar_arquivo_button = tk.Button(frame_arquivo, text="Criptografar", command=encriptar_arquivo)
encriptar_arquivo_button.grid(row=3, columnspan=2)

decriptar_arquivo_button = tk.Button(frame_arquivo, text="Descriptografar", command=decriptar_arquivo)
decriptar_arquivo_button.grid(row=4, columnspan=2)

frame_palavra.grid()

resultado_text = tk.Text(root, height=6, width=40)
resultado_text.grid(row=6, columnspan=2, padx=10, pady=10)


root.mainloop()