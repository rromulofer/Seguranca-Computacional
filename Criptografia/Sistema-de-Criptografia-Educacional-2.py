from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Chave: qazwsxedcrfvtgbyhnujmikolp

# Implementação da Cifra de César
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Implementação da Cifra de Substituição
def substitution_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            index = ord(char) - ascii_offset
            encrypted_char = key[index % len(key)]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def substitution_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            index = key.index(char)
            decrypted_char = chr(index + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Função para criptografar uma palavra
def encrypt_word():
    word = input_word.get()
    algorithm = algorithm_choice.get()

    if algorithm == "Cifra de César":
        shift = int(shift_entry.get())
        encrypted_word = caesar_encrypt(word, shift)
    elif algorithm == "Cifra de Substituição":
        key = key_entry.get()
        encrypted_word = substitution_encrypt(word, key)

    output_word.config(state='normal')
    output_word.delete(0, 'end')
    output_word.insert(0, encrypted_word)
    output_word.config(state='readonly')

# Função para decriptografar uma palavra
def decrypt_word():
    word = input_word.get()
    algorithm = algorithm_choice.get()

    if algorithm == "Cifra de César":
        shift = int(shift_entry.get())
        decrypted_word = caesar_decrypt(word, shift)
    elif algorithm == "Cifra de Substituição":
        key = key_entry.get()
        decrypted_word = substitution_decrypt(word, key)

    output_word.config(state='normal')
    output_word.delete(0, 'end')
    output_word.insert(0, decrypted_word)
    output_word.config(state='readonly')

# Função para criptografar um texto
def encrypt_text():
    text = input_text.get("1.0", "end-1c")
    algorithm = algorithm_choice.get()

    if algorithm == "Cifra de César":
        shift = int(shift_entry.get())
        encrypted_text = caesar_encrypt(text, shift)
    elif algorithm == "Cifra de Substituição":
        key = key_entry.get()
        encrypted_text = substitution_encrypt(text, key)

    output_text.config(state='normal')
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)
    output_text.config(state='disabled')

# Função para decriptografar um texto
def decrypt_text():
    text = input_text.get("1.0", "end-1c")
    algorithm = algorithm_choice.get()

    if algorithm == "Cifra de César":
        shift = int(shift_entry.get())
        decrypted_text = caesar_decrypt(text, shift)
    elif algorithm == "Cifra de Substituição":
        key = key_entry.get()
        decrypted_text = substitution_decrypt(text, key)

    output_text.config(state='normal')
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)
    output_text.config(state='disabled')


# Função para criptografar um arquivo
def encrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    algorithm = algorithm_choice.get()

    if algorithm == "Cifra de César":
        shift = int(shift_entry.get())
        with open(file_path, 'r') as file:
            text = file.read()
        encrypted_text = caesar_encrypt(text, shift)
    elif algorithm == "Cifra de Substituição":
        key = key_entry.get()
        with open(file_path, 'r') as file:
            text = file.read()
        encrypted_text = substitution_encrypt(text, key)

    save_file(encrypted_text)

# Função para decriptografar um arquivo
def decrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    algorithm = algorithm_choice.get()

    if algorithm == "Cifra de César":
        shift = int(shift_entry.get())
        with open(file_path, 'r') as file:
            text = file.read()
        decrypted_text = caesar_decrypt(text, shift)
    elif algorithm == "Cifra de Substituição":
        key = key_entry.get()
        with open(file_path, 'r') as file:
            text = file.read()
        decrypted_text = substitution_decrypt(text, key)

    save_file(decrypted_text)

# Função para salvar o texto em um arquivo
def save_file(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    with open(file_path, 'w') as file:
        file.write(text)

root = Tk()
root.title("Sistema de Criptografia")
root.geometry("400x450")

# Escolha do algoritmo
algorithm_label = Label(root, text="Escolha o Algoritmo:", font=("Arial", 12, "bold"))
algorithm_label.pack()
algorithm_choice = StringVar(root)
algorithm_choice.set("Cifra de César")
algorithm_dropdown = OptionMenu(root, algorithm_choice, "Cifra de César", "Cifra de Substituição")
algorithm_dropdown.pack()

# Notebook (abas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10)

# Aba "Palavra"
frame_word = Frame(notebook)
frame_word.pack()

# Entrada de palavra
input_word_label = Label(frame_word, text="Palavra:")
input_word_label.pack()
input_word = Entry(frame_word)
input_word.pack()

# Botões para criptografar e decriptografar palavras
encrypt_word_button = Button(frame_word, text="Criptografar Palavra", command=encrypt_word)
encrypt_word_button.pack()
decrypt_word_button = Button(frame_word, text="Decriptografar Palavra", command=decrypt_word)
decrypt_word_button.pack()

# Saída de palavra
output_word_label = Label(frame_word, text="Resultado:")
output_word_label.pack()
output_word = Entry(frame_word, state='readonly')
output_word.pack()

# Adicionar a aba "Palavra" ao notebook
notebook.add(frame_word, text="Palavra")

# Aba "Texto"
frame_text = Frame(notebook)
frame_text.pack()

# Entrada de texto
input_text_label = Label(frame_text, text="Texto:")
input_text_label.pack()
input_text = Text(frame_text, height=5, width=30)
input_text.pack()

# Botões para criptografar e decriptografar textos
encrypt_text_button = Button(frame_text, text="Criptografar Texto", command=encrypt_text)
encrypt_text_button.pack()
decrypt_text_button = Button(frame_text, text="Decriptografar Texto", command=decrypt_text)
decrypt_text_button.pack()

# Saída de texto
output_text_label = Label(frame_text, text="Resultado:")
output_text_label.pack()
output_text = Text(frame_text, height=5, width=30)
output_text.pack()

# Adicionar a aba "Texto" ao notebook
notebook.add(frame_text, text="Texto")

# Aba "Arquivo"
frame_file = Frame(notebook)
frame_file.pack()

# Botões para criptografar e decriptografar arquivos
encrypt_file_button = Button(frame_file, text="Criptografar Arquivo", command=encrypt_file)
encrypt_file_button.pack()
decrypt_file_button = Button(frame_file, text="Decriptografar Arquivo", command=decrypt_file)
decrypt_file_button.pack()

# Adicionar a aba "Arquivo" ao notebook
notebook.add(frame_file, text="Arquivo")


# Aba "Deslocamento e Chave"
frame_chave = Frame(notebook)
frame_chave.pack()

# Deslocamento (para Cifra de César)
shift_label = Label(frame_chave, text="Deslocamento:")
shift_label.pack()
shift_entry = Entry(frame_chave)
shift_entry.insert(0, "5")
shift_entry.pack()

# Chave (para Cifra de Substituição)
key_label = Label(frame_chave, text="Chave:")
key_label.pack()
key_entry = Entry(frame_chave)
key_entry.insert(0, "qazwsxedcrfvtgbyhnujmikolp")
key_entry.pack()

# Adicionar a aba "Deslocamento e Chave" ao notebook
notebook.add(frame_chave, text="Deslocamento e Chave")


# Aba "Sobre"
frame_sobre = Frame(notebook)
frame_sobre.pack()

# Título
title_label = Label(frame_sobre, text="Sistema de Criptografia Educacional", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Texto
text = """Autores: 
Rômulo Souza Fernandes
Ausberto S. Castro Vera

UENF - CCT - LCMAT
Ciência da Computação
2023
"""

text_box = Text(frame_sobre, height=8, width=40, font=("Arial", 11))
text_box.insert("1.0", text)
text_box.configure(state="disabled")
text_box.pack(padx=10)

# Adicionar a aba "Sobre" ao notebook
notebook.add(frame_sobre, text="Sobre")


# Execução da interface gráfica
root.mainloop()