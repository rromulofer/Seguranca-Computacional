import string

def cifra_cesar(mensagem, deslocamento):
    mensagem_encriptada = ""
    for caractere in mensagem:
        if caractere in string.ascii_lowercase:
            indice = (string.ascii_lowercase.index(caractere) + deslocamento) % 26
            mensagem_encriptada += string.ascii_lowercase[indice]
        elif caractere in string.ascii_uppercase:
            indice = (string.ascii_uppercase.index(caractere) + deslocamento) % 26
            mensagem_encriptada += string.ascii_uppercase[indice]
        else:
            mensagem_encriptada += caractere
    return mensagem_encriptada

def decifra_cesar(mensagem_encriptada, deslocamento):
    mensagem_desencriptada = cifra_cesar(mensagem_encriptada, -deslocamento)
    return mensagem_desencriptada

def gera_tabela_substituicao():
    alfabeto = list(string.ascii_lowercase)
    tabela_substituicao = {}
    for letra in alfabeto:
        substituta = input(f"Digite a letra substituta para '{letra}': ")
        tabela_substituicao[letra] = substituta
    return tabela_substituicao

def cifra_substituicao(mensagem, tabela_substituicao):
    mensagem_encriptada = ""
    for caractere in mensagem:
        if caractere in tabela_substituicao:
            mensagem_encriptada += tabela_substituicao[caractere]
        else:
            mensagem_encriptada += caractere
    return mensagem_encriptada

def decifra_substituicao(mensagem_encriptada, tabela_substituicao):
    tabela_inversa = {valor: chave for chave, valor in tabela_substituicao.items()}
    mensagem_desencriptada = cifra_substituicao(mensagem_encriptada, tabela_inversa)
    return mensagem_desencriptada

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
            tabela_substituicao = gera_tabela_substituicao()
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

                   

