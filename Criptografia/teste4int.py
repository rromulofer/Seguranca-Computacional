import os

def cifra_de_cesar(texto, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    tamanho_alfabeto = len(alfabeto)
    texto = texto.lower()
    texto_cifrado = ''
    for letra in texto:
        if letra in alfabeto:
            indice_letra = alfabeto.index(letra)
            if modo == 'cifrar':
                novo_indice = (indice_letra + chave) % tamanho_alfabeto
            elif modo == 'decifrar':
                novo_indice = (indice_letra - chave) % tamanho_alfabeto
            nova_letra = alfabeto[novo_indice]
            texto_cifrado += nova_letra
        else:
            texto_cifrado += letra
    return texto_cifrado


def cifra_de_substituicao(texto, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    tamanho_alfabeto = len(alfabeto)
    chave = chave.lower()
    texto = texto.lower()
    texto_cifrado = ''
    for letra in texto:
        if letra in alfabeto:
            indice_letra = alfabeto.index(letra)
            if modo == 'cifrar':
                nova_letra = chave[indice_letra]
            elif modo == 'decifrar':
                novo_indice = chave.find(letra)
                nova_letra = alfabeto[novo_indice]
            texto_cifrado += nova_letra
        else:
            texto_cifrado += letra
    return texto_cifrado


def encriptar_palavra():
    palavra = input("Digite uma palavra: ")
    chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
    cifra = input("Digite 'C' para cifra de César ou 'S' para cifra de substituição: ")
    modo = 'cifrar'
    if cifra.upper() == 'C':
        palavra_cifrada = cifra_de_cesar(palavra, chave, modo)
    elif cifra.upper() == 'S':
        palavra_cifrada = cifra_de_substituicao(palavra, chave, modo)
    else:
        print("Opção inválida.")
        return
    print("Palavra original:", palavra)
    print("Palavra criptografada:", palavra_cifrada)


def decriptar_palavra():
    palavra_cifrada = input("Digite a palavra: ")
    chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
    cifra = input("Digite 'C' para cifra de César ou 'S' para cifra de substituição: ")
    modo = 'decifrar'
    if cifra.upper() == 'C':
        palavra_decifrada = cifra_de_cesar(palavra_cifrada, chave, modo)
    elif cifra.upper() == 'S':
        palavra_decifrada = cifra_de_substituicao(palavra_cifrada, chave, modo)
    else:
        print("Opção inválida.")
        return
    print("Palavra criptografada:", palavra_cifrada)
    print("Palavra original:", palavra_decifrada)


def encriptar_texto():
    texto = input("Digite o texto: ")
    chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
    cifra = input("Digite 'C' para cifra de César ou 'S' para cifra de substituição: ")
    modo = 'cifrar'
    if cifra.upper() == 'C':
        texto_cifrado = cifra_de_cesar(texto, chave, modo)
    elif cifra.upper() == 'S':
        texto_cifrado = cifra_de_substituicao(texto, chave, modo)
    else:
        print("Opção inválida.")
        return
    print("Texto original:\n", texto)
    print("Texto criptografado:\n", texto_cifrado)


def decriptar_texto():
    texto_cifrado = input("Digite o texto: ")
    chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
    cifra = input("Digite 'C' para cifra de César ou 'S' para cifra de substituição: ")
    modo = 'decifrar'
    if cifra.upper() == 'C':
        texto_decifrado = cifra_de_cesar(texto_cifrado, chave, modo)
    elif cifra.upper() == 'S':
        texto_decifrado = cifra_de_substituicao(texto_cifrado, chave, modo)
    else:
        print("Opção inválida.")
        return
    print("Texto criptografado:\n", texto_cifrado)
    print("Texto original:\n", texto_decifrado)


def encriptar_arquivo():
    caminho_arquivo = input("Digite o caminho do arquivo: ")
    chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
    cifra = input("Digite 'C' para cifra de César ou 'S' para cifra de substituição: ")
    modo = 'cifrar'
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            texto = arquivo.read()
            if cifra.upper() == 'C':
                texto_cifrado = cifra_de_cesar(texto, chave, modo)
            elif cifra.upper() == 'S':
                texto_cifrado = cifra_de_substituicao(texto, chave, modo)
            else:
                print("Opção inválida.")
                return
        with open(caminho_arquivo + '.cifrado', 'w') as arquivo_cifrado:
            arquivo_cifrado.write(texto_cifrado)
        print("Arquivo criptografado com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")


def decriptar_arquivo():
    caminho_arquivo = input("Digite o caminho do arquivo: ")
    chave = int(input("Digite a chave de deslocamento ou a chave de substituição: "))
    cifra = input("Digite 'C' para cifra de César ou 'S' para cifra de substituição: ")
    modo = 'decifrar'
    try:
        with open(caminho_arquivo[:-8], 'w') as arquivo_decifrado:
            arquivo_decifrado.write(texto_decifrado)
        print("Arquivo descriptografado com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")


# Great! Now that we know the user wants to encrypt a message, we need to ask them for the message they want to encrypt.

# We can do this by using the input() function again:

message = input("Please enter the message you want to encrypt: ")


# This will ask the user to input a message and store it in the variable message.

# Now that we have the message, we can use the Caesar cipher to encrypt it. We can do this by shifting each 
# letter in the message by the specified number of positions.

# Here's an implementation of the Caesar cipher:

def caesar_cipher(message, shift):
    encrypted_message = ""

    for letter in message:
        if letter.isalpha():
            # Determine the ASCII code for the letter
            ascii_code = ord(letter)

            # Determine if the letter is uppercase or lowercase
            if letter.isupper():
                # Shift the letter by the specified number of positions
                new_ascii_code = (ascii_code - 65 + shift) % 26 + 65
            else:
                new_ascii_code = (ascii_code - 97 + shift) % 26 + 97

            # Convert the new ASCII code to a letter
            new_letter = chr(new_ascii_code)
        else:
            new_letter = letter

        encrypted_message += new_letter

    return encrypted_message


# This code will ask the user whether they want to encrypt or decrypt a message, and then ask 
# for the message and shift value if the user wants to encrypt. If the user wants to decrypt, it 
# will print a message saying that decryption is not yet implemented. If the user enters an invalid input, 
# it will print a message saying so.

# I hope this helps! Let me know if you have any questions.