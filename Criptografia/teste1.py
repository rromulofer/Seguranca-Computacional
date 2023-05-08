import os
<<<<<<< HEAD
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util import Padding

def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(Padding.pad(plaintext.encode('utf-8'), AES.block_size))
    return iv + ciphertext

def decrypt_aes(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = Padding.unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')

def generate_rsa_keypair():
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()

def encrypt_rsa(public_key, plaintext):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return ciphertext

def decrypt_rsa(private_key, ciphertext):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')

def main():
    print('Sistema Pedagógico de Criptografia')
    print('Escolha um algoritmo de criptografia:')
    print('1. AES')
    print('2. RSA')

    algorithm = int(input('Digite o número correspondente: '))
    if algorithm == 1:
        key = os.urandom(32)
        print('Chave AES gerada:', key.hex())

        while True:
            print('Escolha uma opção:')
            print('1. Criptografar palavra')
            print('2. Descriptografar palavra')
            print('3. Criptografar texto')
            print('4. Descriptografar texto')
            print('5. Criptografar arquivo')
            print('6. Descriptografar arquivo')
            print('0. Sair')

            option = int(input('Digite o número correspondente: '))
            if option == 1:
                plaintext = input('Digite a palavra a ser criptografada: ')
                ciphertext = encrypt_aes(key, plaintext)
                print('Palavra criptografada:', ciphertext.hex())
            elif option == 2:
                ciphertext = bytes.fromhex(input('Digite a palavra criptografada: '))
                plaintext = decrypt_aes(key, ciphertext)
                print('Palavra descriptografada:', plaintext)
            elif option == 3:
                plaintext = input('Digite o texto a ser criptografado: ')
                ciphertext = encrypt_aes(key, plaintext)
                print('Texto criptografado:', ciphertext.hex())
                print('Texto normal:', plaintext)
            elif option == 4:
                ciphertext = bytes.fromhex(input('Digite o texto criptografado: '))
                plaintext = decrypt_aes(key, ciphertext)
                print('Texto descriptografado:', plaintext)
                print('Texto criptografado:', ciphertext.hex())
            elif option == 5:
                filename = input('Digite o nome do arquivo a ser criptografado: ')
                with open(filename, 'rb') as f:
                    plaintext = f.read()
                ciphertext = encrypt_aes(key, plaintext)
                with open(filename + '.enc', 'wb') as f:
                    f.write(ciphertext)
                print('Arquivo criptografado:', filename +'.enc')
            elif option == 6:
                filename = input('Digite o nome do arquivo a ser descriptografado: ')
                with open(filename, 'rb') as f:
                    ciphertext = f.read()
                plaintext = decrypt_aes(key, ciphertext)
                with open(filename[:-4], 'wb') as f:
                    f.write(plaintext)
                print('Arquivo descriptografado:', filename[:-4])

            elif option == 0:
                break

            else:
                print('Opção inválida. Tente novamente.')

    elif algorithm == 2:
        private_key, public_key = generate_rsa_keypair()
        print('Chave privada RSA gerada:', private_key.decode('utf-8'))
        print('Chave pública RSA gerada:', public_key.decode('utf-8'))

        while True:
            print('Escolha uma opção:')
            print('1. Criptografar palavra')
            print('2. Descriptografar palavra')
            print('3. Criptografar texto')
            print('4. Descriptografar texto')
            print('5. Criptografar arquivo')
            print('6. Descriptografar arquivo')
            print('0. Sair')

            option = int(input('Digite o número correspondente: '))
            if option == 1:
                plaintext = input('Digite a palavra a ser criptografada: ')
                ciphertext = encrypt_rsa(public_key, plaintext)
                print('Palavra criptografada:', ciphertext.hex())
            elif option == 2:
                ciphertext = bytes.fromhex(input('Digite a palavra criptografada: '))
                plaintext = decrypt_rsa(private_key, ciphertext)
                print('Palavra descriptografada:', plaintext)
            elif option == 3:
                plaintext = input('Digite o texto a ser criptografado: ')
                ciphertext = encrypt_rsa(public_key, plaintext)
                print('Texto criptografado:', ciphertext.hex())
                print('Texto normal:', plaintext)
            elif option == 4:
                ciphertext = bytes.fromhex(input('Digite o texto criptografado: '))
                plaintext = decrypt_rsa(private_key, ciphertext)
                print('Texto descriptografado:', plaintext)
                print('Texto criptografado:', ciphertext.hex())
            elif option == 5:
                filename = input('Digite o nome do arquivo a ser criptografado: ')
                with open(filename, 'rb') as f:
                    plaintext = f.read()
                ciphertext = encrypt_rsa(public_key, plaintext)
                with open(filename + '.enc', 'wb') as f:
                    f.write(ciphertext)
                print('Arquivo criptografado:', filename + '.enc')
            elif option == 6:
                filename = input('Digite o nome do arquivo a ser descriptografado: ')
                with open(filename, 'rb') as f:
                    ciphertext = f.read()
                plaintext = decrypt_rsa(private_key, ciphertext)
                with open(filename[:-4], 'wb') as f:
                    f.write(plaintext)
                print('Arquivo descriptografado:', filename[:-4])
            elif option == 0:
                break
            else:
                print('Opção inválida. Tente novamente.')
    else:
        print('Opção inválida. Tente novamente.')
             
=======
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
>>>>>>> aa8ac93f0f5e84df3c0664ccfbf5d3986a5b6136
