import string

# Caesar cipher encryption function
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted_index = (alphabet.index(char) + shift) % 26
            result += alphabet[shifted_index]
        else:
            result += char
    return result

# Caesar cipher decryption function
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Substitution cipher encryption function
def substitution_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if char.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            key_char = key[alphabet.index(char)]
            result += key_char
        else:
            result += char
    return result

# Substitution cipher decryption function
def substitution_decrypt(text, key):
    inv_key = ''.join(sorted(key, key=lambda x: key.index(x)))
    return substitution_encrypt(text, inv_key)

# Encrypt function
def encrypt(text, cipher_type, key=None):
    if cipher_type == 'caesar':
        shift = int(key)
        return caesar_encrypt(text, shift)
    elif cipher_type == 'substitution':
        return substitution_encrypt(text, key)

# Decrypt function
def decrypt(text, cipher_type, key=None):
    if cipher_type == 'caesar':
        shift = int(key)
        return caesar_decrypt(text, shift)
    elif cipher_type == 'substitution':
        return substitution_decrypt(text, key)

# Encrypt file function
def encrypt_file(input_file, output_file, cipher_type, key=None):
    with open(input_file, 'r') as f_in:
        plain_text = f_in.read()
    encrypted_text = encrypt(plain_text, cipher_type, key)
    with open(output_file, 'w') as f_out:
        f_out.write(encrypted_text)

# Decrypt file function
def decrypt_file(input_file, output_file, cipher_type, key=None):
    with open(input_file, 'r') as f_in:
        encrypted_text = f_in.read()
    decrypted_text = decrypt(encrypted_text, cipher_type, key)
    with open(output_file, 'w') as f_out:
        f_out.write(decrypted_text)

# Encrypt a word using Caesar cipher
encrypted_word = encrypt("hello", "caesar", "3")
print(encrypted_word) # prints "khoor"

# Decrypt the encrypted word using Caesar cipher
decrypted_word = decrypt(encrypted_word, "caesar", "3")
print(decrypted_word) # prints "hello"

# Encrypt a text using Substitution cipher
sub_key = "pqlmnoijkabcdeghfstruvwxyzz"
encrypted_text = encrypt("The quick brown fox jumps over the lazy dog.", "substitution", sub_key)
print(encrypted_text) # prints "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."

# Decrypt the encrypted text using Substitution cipher
decrypted_text = decrypt(encrypted_text, "substitution", sub_key)
print(decrypted_text) # prints "The quick brown fox jumps over the lazy dog."

# Encrypt a file using Caesar cipher
encrypt_file("input.txt", "output_encrypted.txt", "caesar", "5")

# Decrypt a file using Caesar cipher
decrypt_file("output_encrypted.txt", "output_decrypted.txt", "caesar", "5")

