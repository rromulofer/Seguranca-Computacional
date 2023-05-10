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

# Encryption option for a word
def encrypt_word():
    plaintext = input("Enter the word to encrypt: ")
    caesar_key = int(input("Enter the Caesar cipher key: "))
    vigenere_key = input("Enter the Vigenère cipher key: ")
    caesar_ciphertext = caesar_encrypt(plaintext, caesar_key)
    vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
    print(f"Plaintext: {plaintext}")
    print(f"Caesar ciphertext: {caesar_ciphertext}")
    print(f"Vigenère ciphertext: {vigenere_ciphertext}")

# Encryption option for a text
def encrypt_text():
    plaintext = input("Enter the text to encrypt: ")
    caesar_key = int(input("Enter the Caesar cipher key: "))
    vigenere_key = input("Enter the Vigenère cipher key: ")
    caesar_ciphertext = caesar_encrypt(plaintext, caesar_key)
    vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
    print(f"Plaintext: {plaintext}")
    print(f"Caesar ciphertext: {caesar_ciphertext}")
    print(f"Vigenère ciphertext: {vigenere_ciphertext}")

# Encryption option for a file
def encrypt_file():
    filename = input("Enter the name of the file to encrypt: ")
    with open(filename, "r") as f:
        plaintext = f.read()
    caesar_key = int
    vigenere_key = input("Enter the Vigenère cipher key: ")
    caesar_ciphertext = caesar_encrypt(plaintext, caesar_key)
    vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
    print(f"Plaintext:\n{plaintext}")
    print(f"Caesar ciphertext:\n{caesar_ciphertext}")
    print(f"Vigenère ciphertext:\n{vigenere_ciphertext}")
    with open("caesar_" + filename, "w") as f:
        f.write(caesar_ciphertext)
    with open("vigenere_" + filename, "w") as f:
        f.write(vigenere_ciphertext)
    print("Encryption completed.")
    
# Main menu
while True:
    print("Select an option:")
    print("1. Encrypt a word")
    print("2. Encrypt a text")
    print("3. Encrypt a file")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        encrypt_word()
    elif choice == "2":
        encrypt_text()
    elif choice == "3":
        encrypt_file()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
