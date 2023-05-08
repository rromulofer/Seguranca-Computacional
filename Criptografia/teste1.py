import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization


def encrypt_aes(key, plaintext):
    iv = get_random_bytes(16)  # gerar um vetor de inicialização aleatório
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    return (ciphertext, iv)


def decrypt_aes(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


def generate_rsa_key():
    return rsa.generate_private_key(
        public_exponent=65537, key_size=2048)


def serialize_rsa_key(key):
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())


def deserialize_rsa_key(data):
    return serialization.load_pem_private_key(
        data, password=None)


def encrypt_rsa(public_key, plaintext):
    ciphertext = public_key.encrypt(
        plaintext.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
    return ciphertext


def decrypt_rsa(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
    return plaintext.decode('utf-8')


def input_password():
    return input("Digite a senha de criptografia: ")


def input_text():
    return input("Digite o texto a ser criptografado: ")


def input_file():
    filename = input("Digite o caminho do arquivo a ser criptografado: ")
    with open(filename, 'rb') as f:
        contents = f.read()
    return contents


def output_text(text, encrypted_text):
    print("Texto original: ", text)
    print("Texto criptografado: ", encrypted_text)


def output_file(filename, contents):


with open(filename, 'wb') as f:
f.write(contents)
print("Arquivo criptografado salvo em", filename)


def choose_algorithm():


print("Escolha um algoritmo de criptografia:")
print("1. AES")
print("2. RSA")
choice = input("Digite o número correspondente: ")
return int(choice)


def encrypt_text(key, algorithm, plaintext):


if algorithm == 1:
ciphertext, iv = encrypt_aes(key, plaintext.encode('utf-8'))
return (ciphertext, iv)
elif algorithm == 2:
public_key = deserialize_rsa_key(key)
ciphertext = encrypt_rsa(public_key, plaintext)
return (ciphertext, None)


def decrypt_text(key, algorithm, ciphertext, iv=None):


if algorithm == 1:
plaintext = decrypt_aes(key, ciphertext, iv)
return plaintext.decode('utf-8')
elif algorithm == 2:
private_key = deserialize_rsa_key(key)
plaintext = decrypt_rsa(private_key, ciphertext)
return plaintext
