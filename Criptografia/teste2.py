<<<<<<< HEAD
import base64
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class Criptografia:
    def __init__(self, chave):
        self.chave = chave

    def criptografar_fernet(self, texto):
        chave_bytes = self.chave.encode()
        f = Fernet(base64.urlsafe_b64encode(chave_bytes))
        texto_bytes = texto.encode()
        texto_criptografado = f.encrypt(texto_bytes)
        return texto_criptografado

    def descriptografar_fernet(self, texto_criptografado):
        chave_bytes = self.chave.encode()
        f = Fernet(base64.urlsafe_b64encode(chave_bytes))
        texto_bytes = f.decrypt(texto_criptografado)
        texto_descriptografado = texto_bytes.decode()
        return texto_descriptografado

    def criptografar_aes(self, texto):
        chave_bytes = self.chave.encode()
        iv = b'1234567890123456'
        cipher = AES.new(chave_bytes, AES.MODE_CBC, iv)
        texto_bytes = texto.encode()
        texto_pad = pad(texto_bytes, AES.block_size)
        texto_criptografado = cipher.encrypt(texto_pad)
        return texto_criptografado

    def descriptografar_aes(self, texto_criptografado):
        chave_bytes = self.chave.encode()
        iv = b'1234567890123456'
        cipher = AES.new(chave_bytes, AES.MODE_CBC, iv)
        texto_pad = cipher.decrypt(texto_criptografado)
        texto_bytes = unpad(texto_pad, AES.block_size)
        texto_descriptografado = texto_bytes.decode()
        return texto_descriptografado
=======
import os
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes


def input_password():
    return input("Digite a senha de criptografia: ")


def generate_rsa_key():
    return RSA.generate(2048)


def serialize_rsa_key(key):
    return key.export_key()


def deserialize_rsa_key(key_data):
    return RSA.import_key(key_data)


def encrypt_aes(key, plaintext):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += bytes([padding_length]) * padding_length
    ciphertext = cipher.encrypt(plaintext)
    return (ciphertext, iv)


def decrypt_aes(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]
    return plaintext


def encrypt_rsa(public_key, plaintext):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return ciphertext


def decrypt_rsa(private_key, ciphertext):
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')


def input_text():
    return input("Digite o texto a ser criptografado: ")


def input_file():
    filename = input("Digite o caminho do arquivo: ")
    with open(filename, 'rb') as f:
        contents = f.read()
    return contents


def output_text(plaintext, encrypted_text):
    print("Texto original:", plaintext)
    print("Texto criptografado:", encrypted_text)


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


def encrypt_text(key, choice, text):
    if choice == '1':
        # Criptografia simétrica usando AES-256
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        ciphertext, iv = encrypt_text(key, choice, text)
        return ciphertext, iv
    elif choice == '2':
        # Criptografia assimétrica usando RSA
        public_key = deserialize_rsa_key(input("Digite a chave pública: "))
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext, iv = encrypt_text(key, choice, text)
        return ciphertext, None

def decrypt_text(key, algorithm, ciphertext, iv=None):
    if choice == '1':
        ciphertext, iv = encrypt_text(key, text)
        return ciphertext, iv
    elif choice == '2':
        ciphertext = encrypt_file(key, text)
        return ciphertext, None
    else:
        print("Opção inválida.")
        return None, None



if __name__ == '__main__':
    choice = str(choose_algorithm())
    if choice == 1:
        key = input_password().encode('utf-8')
    elif choice == 2:
        key = serialize_rsa_key(generate_rsa_key())
    text = input_text()

    if choice == '1':
        key = input_password().encode('utf-8')
    elif choice == '2':
        key = serialize_rsa_key(generate_rsa_key())
    ciphertext = encrypt_text(key, choice, text)

    encrypted_text = ciphertext.hex()
    output_text(text, encrypted_text)
    choice = input("Digite 1 para salvar em arquivo ou 2 para criptografar um arquivo inteiro, ou qualquer outra tecla para sair: ")
    if choice == '1':
        filename = input("Digite o nome do arquivo: ")
        output_file(filename, ciphertext)
    elif choice == '2':
        filename = input("Digite o caminho do arquivo: ")
        with open(filename, 'rb') as f:
            contents = f.read()
        ciphertext, iv = encrypt_aes(key, contents)
        encrypted_file = filename + '.encrypted'
        output_file(encrypted_file, ciphertext)
    else:
        sys.exit(0)
>>>>>>> aa8ac93f0f5e84df3c0664ccfbf5d3986a5b6136
