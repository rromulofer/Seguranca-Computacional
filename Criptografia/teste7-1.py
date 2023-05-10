import tkinter as tk
from tkinter import messagebox, filedialog

# Caesar cipher encryption and decryption functions


def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char.lower()) - ord('a') + key
            cipherchar = chr((shift % 26) + ord('a'))
            if char.isupper():
                cipherchar = cipherchar.upper()
        else:
            cipherchar = char
        ciphertext += cipherchar
    return ciphertext


def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char.lower()) - ord('a') - key
            plainchar = chr((shift % 26) + ord('a'))
            if char.isupper():
                plainchar = plainchar.upper()
        else:
            plainchar = char
        plaintext += plainchar
    return plaintext

# Vigenère cipher encryption and decryption functions


def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    keypos = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[keypos % len(key)].lower()) - ord('a')
            shift += ord(char.lower()) - ord('a')
            cipherchar = chr((shift % 26) + ord('a'))
            if char.isupper():
                cipherchar = cipherchar.upper()
            keypos += 1
        else:
            cipherchar = char
        ciphertext += cipherchar
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    keypos = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char.lower()) - ord(key[keypos % len(key)].lower())
            plainchar = chr((shift % 26) + ord('a'))
            if char.isupper():
                plainchar = plainchar.upper()
            keypos += 1
        else:
            plainchar = char
        plaintext += plainchar
    return plaintext

# Functions for GUI windows


def word_encrypt_window():
    def encrypt():
        plaintext = plaintext_entry.get()
        caesar_key = int(caesar_key_entry.get())
        vigenere_key = vigenere_key_entry.get()
        caesar_ciphertext = caesar_encrypt(plaintext, caesar_key)
        vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
        results_window(caesar_ciphertext, vigenere_ciphertext, plaintext)

    window = tk.Toplevel()
    window.title("Encrypt a Word")

    plaintext_label = tk.Label(window, text="Enter the word to encrypt:")
    plaintext_entry = tk.Entry(window)

    caesar_key_label = tk.Label(window, text="Enter the Caesar cipher key:")
    caesar_key_entry = tk.Entry(window)

    vigenere_key_label = tk.Label(
        window, text="Enter the Vigenère cipher key:")
    vigenere_key_entry = tk.Entry(window)

    encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)

    plaintext_label.pack()
    plaintext_entry.pack()
    caesar_key_label.pack()
    caesar_key_entry.pack()
    vigenere_key_label.pack()
    vigenere_key_entry.pack()
    encrypt_button.pack


root = tk.Tk()
root.title("Encryption Tool")

frame1 = tk.Frame(root)
frame1.pack(padx=20, pady=10)

frame2 = tk.Frame(root)
frame2.pack(padx=20, pady=10)

title_label = tk.Label(frame1, text="Select an option:")
title_label.pack()

word_button = tk.Button(frame1, text="Encrypt a word", command=encrypt_word)
word_button.pack(pady=5)

text_button = tk.Button(frame1, text="Encrypt a text", command=encrypt_text)
text_button.pack(pady=5)

file_button = tk.Button(frame1, text="Encrypt a file", command=encrypt_file)
file_button.pack(pady=5)

exit_button = tk.Button(frame1, text="Exit", command=root.destroy)
exit_button.pack(pady=5)


def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char.lower()) - ord('a') + key
            cipherchar = chr((shift % 26) + ord('a'))
        if char.isupper():
            cipherchar = cipherchar.upper()
        else:
            cipherchar = char
            ciphertext += cipherchar
    return ciphertext


def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
        shift = ord(char.lower()) - ord('a') - key
        plainchar = chr((shift % 26) + ord('a'))
        if char.isupper():
            plainchar = plainchar.upper()
        else:
            plainchar = char
            plaintext += plainchar
    return plaintext

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    keypos = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[keypos % len(key)].lower()) - ord('a')
            shift += ord(char.lower()) - ord('a')
            cipherchar = chr((shift % 26) + ord('a'))
        if char.isupper():
            cipherchar = cipherchar.upper()
            keypos += 1
        else:
            cipherchar = char
            ciphertext += cipherchar
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    keypos = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char.lower()) - ord(key[keypos % len(key)].lower())
            plainchar = chr((shift % 26) + ord('a'))
        if char.isupper():
            plainchar = plainchar.upper()
            keypos += 1
        else:
            plainchar = char
            plaintext += plainchar
    return plaintext    

def encrypt_word():
    word_window = tk.Toplevel(root)
    word_window.title("Encrypt a Word")
    word_label = tk.Label(word_window, text="Enter the word to encrypt:")
    word_label.pack(pady=5)

    word_entry = tk.Entry(word_window, width=30)
    word_entry.pack(pady=5)

    caesar_key_label = tk.Label(word_window, text="Enter the Caesar cipher key:")
    caesar_key_label.pack(pady=5)

    caesar_key_entry = tk.Entry(word_window, width=10)
    caesar_key_entry.pack(pady=5)

    vigenere_key_label =

def encrypt_word():
    plaintext = word_entry.get()
    caesar_key = int(caesar_key_entry.get())
    vigenere_key = vigenere_key_entry.get()
    caesar_ciphertext = caesar_encrypt(plaintext, caesar_key)
    vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
    result_label.config(text=f"Plaintext: {plaintext}\nCaesar ciphertext: {caesar_ciphertext}\nVigenère ciphertext: {vigenere_ciphertext}")

def encrypt_text():
    plaintext = text_entry.get("1.0", "end-1c")
    caesar_key = int(caesar_key_entry.get())
    vigenere_key = vigenere_key_entry.get()
    caesar_ciphertext = caesar_encrypt(plaintext, caesar_key)
    vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
    result_label.config(text=f"Plaintext: {plaintext}\nCaesar ciphertext: {caesar_ciphertext}\nVigenère ciphertext: {vigenere_ciphertext}")

def encrypt_file():
    filename = filedialog.askopenfilename(initialdir="./", title="Select a file to encrypt")
    with open(filename, "r") as f:
        plaintext = f.read()
    caesar_key = int(caesar_key_entry.get())
    vigenere_key = vigenere_key_entry.get()
    caesar_ciphertext = caesar_encrypt(plaintext, caesar_key)
    vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
    result_label.config(text=f"Plaintext:\n{plaintext}\nCaesar ciphertext:\n{caesar_ciphertext}\nVigenère ciphertext:\n{vigenere_ciphertext}")
    with open("caesar_" + filename.split("/")[-1], "w") as f:
        f.write(caesar_ciphertext)
    with open("vigenere_" + filename.split("/")[-1], "w") as f:
        f.write(vigenere_ciphertext)
    tk.messagebox.showinfo(title="Encryption Completed", message="The file has been encrypted and saved as 'caesar_filename' and 'vigenere_filename'.")

word_label = tk.Label(root, text="Enter the word to encrypt:")
word_entry = tk.Entry(root, width=30)
caesar_key_label = tk.Label(root, text="Enter the Caesar cipher key:")
caesar_key_entry = tk.Entry(root, width=10)
vigenere_key_label = tk.Label(root, text="Enter the Vigenère cipher key:")
vigenere_key_entry = tk.Entry(root, width=30)
text_label = tk.Label(root, text="Enter the text to encrypt:")
text_entry = tk.Text(root, width=40, height=5)
encrypt_word_button = tk.Button(root, text="Encrypt Word", command=encrypt_word)
encrypt_text_button = tk.Button(root, text="Encrypt Text", command=encrypt_text)
encrypt_file_button = tk.Button(root, text="Encrypt File", command=encrypt_file)
result_label = tk.Label(root, text="")

window = tk.Toplevel(root)
window.title("Encrypt a word")

# Create widgets
input_label = tk.Label(window, text="Enter the word to encrypt:")
input_text = tk.Entry(window)
caesar_key_label = tk.Label(window, text="Enter the Caesar cipher key:")
caesar_key_entry = tk.Entry(window)
vigenere_key_label = tk.Label(window, text="Enter the Vigenère cipher key:")
vigenere_key_entry = tk.Entry(window)
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
output_label = tk.Label(window, text="Output:")
output_text = tk.Text(window)

# Place widgets
input_label.grid(row=0, column=0, sticky="w")
input_text.grid(row=0, column

input_label = tk.Label(window, text="Enter the word to encrypt:")
input_text = tk.Entry(window, width=30)
key_label = tk.Label(window, text="Enter the Vigenère cipher key:")
key_text = tk.Entry(window, width=30)
encrypt_button = tk.Button(window, text="Encrypt", command=lambda: perform_encryption(input_text.get(), key_text.get()))
decrypt_button = tk.Button(window, text="Decrypt", command=lambda: perform_decryption(input_text.get(), key_text.get()))

input_label.grid(row=0, column=0, padx=5, pady=5)
input_text.grid(row=0, column=1, padx=5, pady=5)
key_label.grid(row=1, column=0, padx=5, pady=5)
key_text.grid(row=1, column=1, padx=5, pady=5)
encrypt_button.grid(row=2, column=0, padx=5, pady=5)
decrypt_button.grid(row=2, column=1, padx=5, pady=5)
