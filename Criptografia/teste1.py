import os
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
             
