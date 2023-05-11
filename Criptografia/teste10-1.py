from tkinter import *
from tkinter import filedialog

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
    decrypted_key = ''.join(sorted(key))
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            index = decrypted_key.index(char)
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

    output_word.set(encrypted_word)

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

    output_word.set(decrypted_word)

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

    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

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

    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)

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

# Interface gráfica
root = Tk()
root.title("Sistema de Criptografia")
root.geometry("500x300")

# Entrada de palavra
input_word_label = Label(root, text="Palavra:")
input_word_label.pack()
input_word = Entry(root)
input_word.pack()

# Escolha do algoritmo
algorithm_label = Label(root, text="Algoritmo:")
algorithm_label.pack()
algorithm_choice = StringVar(root)
algorithm_choice.set("Cifra de César")
algorithm_dropdown = OptionMenu(root, algorithm_choice, "Cifra de César", "Cifra de Substituição")
algorithm_dropdown.pack()

# Deslocamento (para Cifra de César)
shift_label = Label(root, text="Deslocamento:")
shift_label.pack()
shift_entry = Entry(root)
shift_entry.pack()

# Chave (para Cifra de Substituição)
key_label = Label(root, text="Chave:")
key_label.pack()
key_entry = Entry(root)
key_entry.pack()

# Botões para criptografar e decriptografar palavras
encrypt_word_button = Button(root, text="Criptografar Palavra", command=encrypt_word)
encrypt_word_button.pack()
decrypt_word_button = Button(root, text="Decriptografar Palavra", command=decrypt_word)
decrypt_word_button.pack()

# Entrada de texto
input_text_label = Label(root, text="Texto:")
input_text_label.pack()
input_text = Text(root, height=5, width=30)
input_text.pack()

# Botões para criptografar e decriptografar textos
encrypt_text_button = Button(root, text="Criptografar Texto", command=encrypt_text)
encrypt_text_button.pack()
decrypt_text_button = Button(root, text="Decriptografar Texto", command=decrypt_text)
decrypt_text_button.pack()

# Botões para criptografar e decriptografar arquivos
encrypt_file_button = Button(root, text="Criptografar Arquivo", command=encrypt_file)
encrypt_file_button.pack()
decrypt_file_button = Button(root, text="Decriptografar Arquivo", command=decrypt_file)
decrypt_file_button.pack()

# Saída de palavra, texto ou arquivo encriptado/decriptado
output_word_label = Label(root, text="Resultado:")
output_word_label.pack()
output_word = StringVar(root)
output_word_entry = Entry(root, textvariable=output_word, state='readonly')
output_word_entry.pack()

output_text_label = Label(root, text="Resultado:")
output_text_label.pack()
output_text = Text(root, height=5, width=30)
output_text.pack()

root.mainloop()