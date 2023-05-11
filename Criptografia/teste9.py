import tkinter as tk

# Função para criptografar um texto usando a Cifra de César
def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Função para descriptografar um texto usando a Cifra de César
def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)

# Função para criptografar um texto usando a Cifra de Substituição
def encrypt_substitution(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            index = (ord(char) - ascii_offset) % 26
            encrypted_char = key[index] if char.isupper() else key[index].lower()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Função para descriptografar um texto usando a Cifra de Substituição
def decrypt_substitution(text, key):
    decrypted_key = "".join([chr((ord(char) - 65) % 26 + 65) for char in key])
    return encrypt_substitution(text, decrypted_key)

# Função para lidar com a criptografia de uma palavra
def encrypt_word():
    word = word_entry.get()
    shift = int(shift_entry.get())
    substitution_key = key_entry.get()

    caesar_encrypted = encrypt_caesar(word, shift)
    substitution_encrypted = encrypt_substitution(word, substitution_key)

    caesar_encrypted_label.config(text="Cifra de César: " + caesar_encrypted)
    substitution_encrypted_label.config(text="Cifra de Substituição: " + substitution_encrypted)

# Função para lidar com a descriptografia de uma palavra
def decrypt_word():
    word = word_entry.get()
    shift = int(shift_entry.get())
    substitution_key = key_entry.get()

    caesar_decrypted = decrypt_caesar(word, shift)
    substitution_decrypted = decrypt_substitution(word, substitution_key)

    caesar_decrypted_label.config(text="Cifra de César: " + caesar_decrypted)
    substitution_decrypted_label.config(text="Cifra de Substituição: " + substitution_decrypted)

# Criação da janela principal
window = tk.Tk()
window.title("Sistema de Criptografia")

# Componentes da interface
word_label = tk.Label(window, text="Palavra:")
word_label.pack()
word_entry = tk.Entry(window)
word_entry.pack()

shift_label = tk.Label(window, text="Deslocamento:")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

key_label = tk.Label(window, text="Chave de Substituição:")
key_label.pack()
key_entry = tk.Entry(window)
key_entry.pack()

encrypt_button = tk.Button(window, text="Criptografar", command=encrypt_word)
encrypt_button.pack()

decrypt_button = tk.Button(window, text="Descriptografar", command=decrypt_word)
decrypt_button.pack()

caesar_encrypted_label = tk.Label(window, text="Cifra de César: ")
caesar_encrypted_label.pack()

substitution_encrypted_label = tk.Label(window, text="Cifra de Substituição: ")
substitution_encrypted_label.pack()

caesar_decrypted_label = tk.Label(window, text="Cifra de César: ")
caesar_decrypted_label.pack()

substitution_decrypted_label = tk.Label(window, text="Cifra de Substituição: ")
substitution_decrypted_label.pack()

window.mainloop()

