from tkinter import *
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
root.geometry("580x350")

# Alterar cor de fundo da janela principal
root.configure(background="black")

# Escolha do algoritmo
algorithm_label = Label(root, text="Escolha o Algoritmo:", bg="black", fg="white")
algorithm_label.pack()
algorithm_choice = StringVar(root)
algorithm_choice.set("Cifra de César")
algorithm_dropdown = OptionMenu(root, algorithm_choice, "Cifra de César", "Cifra de Substituição")
algorithm_dropdown.pack()

# Frame para a coluna "Palavra"
frame_word = Frame(root, bg="black")
frame_word.pack(side=LEFT, padx=10)

# Entrada de palavra
input_word_label = Label(frame_word, text="Palavra:", bg="black", fg="white")
input_word_label.pack()
input_word = Entry(frame_word, bg="white")
input_word.pack()

# Botões para criptografar e decriptografar palavras
encrypt_word_button = Button(frame_word, text="Criptografar Palavra", command=encrypt_word, bg="lime", fg="black")
encrypt_word_button.pack()
decrypt_word_button = Button(frame_word, text="Decriptografar Palavra", command=decrypt_word, bg="red", fg="black")
decrypt_word_button.pack()

# Saída de palavra
output_word_label = Label(frame_word, text="Resultado:", bg="black", fg="white")
output_word_label.pack()
output_word = Entry(frame_word, state='readonly', bg="white")
output_word.pack()

# Frame para a coluna "Texto"
frame_text = Frame(root, bg="black")
frame_text.pack(side=LEFT, padx=10)

# Entrada de texto
input_text_label = Label(frame_text, text="Texto:", bg="black", fg="white")
input_text_label.pack()
input_text = Text(frame_text, height=5, width=30, bg="white")
input_text.pack()

# Botões para criptografar e decriptografar textos
encrypt_text_button = Button(frame_text, text="Criptografar Texto", command=encrypt_text, bg="lime", fg="black")
encrypt_text_button.pack()
decrypt_text_button = Button(frame_text, text="Decriptografar Texto", command=decrypt_text, bg="red", fg="black")
decrypt_text_button.pack()

# Saída de texto
output_text_label = Label(frame_text, text="Resultado:", bg="black", fg="white")
output_text_label.pack()
output_text = Text(frame_text, height=5, width=30, bg="white")
output_text.pack()

# Frame para a coluna "Arquivo"
frame_file = Frame(root, bg="black")
frame_file.pack(side=LEFT, padx=10)

# Botões para criptografar e decriptografar arquivos
encrypt_file_button = Button(frame_file, text="Criptografar Arquivo", command=encrypt_file, bg="lime", fg="black")
encrypt_file_button.pack()
decrypt_file_button = Button(frame_file, text="Decriptografar Arquivo", command=decrypt_file, bg="red", fg="black")
decrypt_file_button.pack()

# Execução da interface gráfica
root.mainloop()