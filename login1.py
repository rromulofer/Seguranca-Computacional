import hashlib

# Informações de login
usuario = "romulo"
senha = "Senha123!"

# Mecanismo de segurança 1: Hash da senha
hash_senha = hashlib.sha256(senha.encode()).hexdigest()

# Mecanismo de segurança 2: Verificação de usuário e senha
def verificar_login(usuario, senha):
    if usuario == "usuario" and senha == "senha123":
        return True
    else:
        return False

# Mecanismo de segurança 3: Autenticação de dois fatores
def autenticacao_dois_fatores(codigo):
    if codigo == "1234":
        return True
    else:
        return False

# Pedir ao usuário as informações de login
usuario_digitado = input("Digite seu usuário: ")
senha_digitada = input("Digite sua senha: ")

# Verificar se as informações de login estão corretas
if usuario_digitado == usuario and hash_senha == hashlib.sha256(senha_digitada.encode()).hexdigest():
    # Se o usuário e a senha estiverem corretos, pedir o código de autenticação de dois fatores
    codigo_digitado = input("Digite o código de autenticação de dois fatores: ")
    
    # Verificar se o código de autenticação de dois fatores está correto
    if autenticacao_dois_fatores(codigo_digitado):
        print("Login efetuado com sucesso!")
    else:
        print("Código de autenticação incorreto.")
else:
    print("Usuário ou senha incorretos.")
