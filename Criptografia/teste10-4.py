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
            index = ord(char.lower()) - ascii_offset
            if char.islower():
                encrypted_char = key[index % len(key)].lower()
            else:
                encrypted_char = key[index % len(key)].upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def substitution_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            index = key.find(char)
            if index != -1:
                decrypted_char = chr(index + ascii_offset)
            else:
                decrypted_char = char
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

# Interface gráfica
root = Tk()
root.title("Sistema de Criptografia")
root.geometry("300x600")

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

# Botões para criptografar e decriptografar uma palavra
encrypt_word_button = Button(root, text="Criptografar Palavra", command=encrypt_word)
encrypt_word_button.pack()
decrypt_word_button = Button(root, text="Decriptografar Palavra", command=decrypt_word)
decrypt_word_button.pack()

# Entrada de texto
input_text_label = Label(root, text="Texto:")
input_text_label.pack()
input_text = Text(root, height=5, width=30)
input_text.pack()

# Botões para criptografar e decriptografar um texto
encrypt_text_button = Button(root, text="Criptografar Texto", command=encrypt_text)
encrypt_text_button.pack()
decrypt_text_button = Button(root, text="Decriptografar Texto", command=decrypt_text)
decrypt_text_button.pack()

# Botões para criptografar e decriptografar um arquivo
encrypt_file_button = Button(root, text="Criptografar Arquivo", command=encrypt_file)
encrypt_file_button.pack()
decrypt_file_button = Button(root, text="Decriptografar Arquivo", command=decrypt_file)
decrypt_file_button.pack()

# Saída de palavra ou texto
output_word_label = Label(root, text="Saída:")
output_word_label.pack()
output_word = Entry(root, state='readonly')
output_word.pack()

output_text = Text(root, height=5, width=30, state='disabled')
output_text.pack()

root.mainloop()