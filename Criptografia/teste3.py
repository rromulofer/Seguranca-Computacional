# cifra de César
def cifra_cesar(texto, deslocamento):
    texto_encriptado = ""
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra)
            codigo += deslocamento
            if letra.isupper():
                if codigo > ord('Z'):
                    codigo -= 26
                elif codigo < ord('A'):
                    codigo += 26
            else:
                if codigo > ord('z'):
                    codigo -= 26
                elif codigo < ord('a'):
                    codigo += 26
            texto_encriptado += chr(codigo)
        else:
            texto_encriptado += letra
    return texto_encriptado

def decifra_cesar(texto_encriptado, deslocamento):
    return cifra_cesar(texto_encriptado, -deslocamento)


# cifra de substituição
import random

def gera_tabela_substituicao():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_embaralhado = "".join(random.sample(alfabeto, len(alfabeto)))
    tabela_substituicao = str.maketrans(alfabeto, alfabeto_embaralhado)
    return tabela_substituicao

def cifra_substituicao(texto):
    tabela_substituicao = gera_tabela_substituicao()
    texto_encriptado = texto.translate(tabela_substituicao)
    return texto_encriptado, tabela_substituicao

def decifra_substituicao(texto_encriptado, tabela_substituicao):
    tabela_substituicao = gera_tabela_substituicao()
    texto_desencriptado = decifra_substituicao(texto_encriptado, tabela_substituicao)
    return texto_desencriptado


# função principal
def main():
    print("Escolha o algoritmo de criptografia:")
    print("1. Cifra de César")
    print("2. Cifra de substituição")
    opcao = input("Opção: ")
    if opcao == "1":
        deslocamento = int(input("Digite o número de deslocamento: "))
        tipo = input("Digite o tipo de entrada (palavra, texto ou arquivo): ")
        if tipo == "palavra":
            palavra = input("Digite a palavra: ")
            palavra_encriptada = cifra_cesar(palavra, deslocamento)
            print("Palavra encriptada:", palavra_encriptada)
            palavra_desencriptada = decifra_cesar(palavra_encriptada, deslocamento)
            print("Palavra desencriptada:", palavra_desencriptada)
        elif tipo == "texto":
            texto = input("Digite o texto: ")
            texto_encriptado = cifra_cesar(texto, deslocamento)
            print("Texto encriptado:", texto_encriptado)
            texto_desencriptado = decifra_cesar(texto_encriptado, deslocamento)
            print("Texto desencriptado:", texto_desencriptado)
        elif tipo == "arquivo":
            nome_arquivo = input("Digite o nome do arquivo: ")
            try:
                with open(nome_arquivo, "r") as arquivo:
                    texto = arquivo.read()
                    texto_encriptado = cifra_cesar(texto, deslocamento)
                    with open(nome_arquivo + ".encriptado", "w") as arquivo_encriptado:
                        arquivo_encriptado.write(texto_encriptado)
                    print("Arquivo encriptado salvo como", nome_arquivo + ".encriptado")
            except FileNotFoundError:
                print("Arquivo não encontrado")
            except:
                print("Erro ao processar arquivo")
    elif opcao == "2":
        tipo = input("Digite o tipo de entrada (palavra, texto ou arquivo): ")
        if tipo == "palavra":
            palavra = input("Digite a palavra: ")
            palavra_encriptada = cifra_substituicao(palavra)
            print("Palavra encriptada:", palavra_encriptada)
            palavra_desencriptada = decifra_substituicao(palavra_encriptada)
            print("Palavra desencriptada:", palavra_desencriptada)
        elif tipo == "texto":
            texto = input("Digite o texto: ")
            texto_encriptado = cifra_substituicao(texto)
            print("Texto encriptado:", texto_encriptado)
            texto_desencriptado = decifra_substituicao(texto_encriptado, tabela_substituicao)
            print("Texto desencriptado:", texto_desencriptado)
        elif tipo == "arquivo":
            nome_arquivo = input("Digite o nome do arquivo: ")
            try:
                with open(nome_arquivo, "r") as arquivo:
                    texto = arquivo.read()
                    texto_encriptado = cifra_substituicao(texto)
                    with open(nome_arquivo + ".encriptado", "w") as arquivo_encriptado:
                        arquivo_encriptado.write(texto_encriptado)
                    print("Arquivo encriptado salvo como", nome_arquivo + ".encriptado")
            except FileNotFoundError:
                print("Arquivo não encontrado")
            except:
                print("Erro ao processar arquivo")
    else:
        print("Opção inválida")

if __name__ == '__main__':
    main()
