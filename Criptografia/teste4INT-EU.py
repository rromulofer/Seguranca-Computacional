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


opcao = int(input("Digite:\n 1-criptografar uma palavra \n 2-descriptografar uma palavra, "
                  "\n 3-criptografar um texto, \n 4-descriptografar um texto, "
                  "\n 5-criptografar um arquivo \n 6-descriptografar um arquivo \n Opção desejada:"))

if opcao == 1:
    encriptar_palavra()
elif opcao == 2:
    decriptar_palavra()
elif opcao == 3:
    encriptar_texto()
elif opcao == 4:
    decriptar_texto()
elif opcao == 5:
    encriptar_arquivo()
elif opcao == 6:
    decriptar_arquivo()
else:
    print("Opção inválida.")