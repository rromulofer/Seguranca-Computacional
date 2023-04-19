#  Prof. Ausberto S. Castro Vera
#  Disciplina : Segurança Computacional
#  UENF-CCT-LCMAT-CC
#  Data: Abril 2023
#  Aluno: Rômulo Souza Fernandes

# Controle de acesso - Login
# Com 3 mecanismos de segurança
# 1 - Senha
# 2 - Força da senha
# 3 - Token de acesso

# Bibliotecas utilizadas
# Gera o token de acesso de forma aleatória
import random 

# Utilizada junto com a random para gerar tokens aleatórias
# Também para verificar se a senha possui caracteres especiais
import string

# Criação da interface
import tkinter as tk

# Função utilizada para gerar um token de acesso aleatório e enviar para o usuário. 
# O token é composto por letras e números, com um comprimento de 6 caracteres.
def send_access_token(user):
    token = ''.join(random.choice(string.ascii_letters + string.digits)
                    for i in range(6))
    print(f"Token de acesso enviado para {user}: {token}")
    return token

# Função responsável por verificar a força da senha informada pelo usuário. 
# A força da senha é calculada com base no seu comprimento, presença de letras 
# maiúsculas e minúsculas, números e caracteres especiais. A força da senha é 
# classificada em uma escala de 1 a 4.
def check_password_strength(password):
    # Inicializa a força da senha como 0
    strength = 0
    
    # Verifica o comprimento da senha
    if len(password) >= 8:
        strength += 1
    
    # Verifica se a senha contém letras maiúsculas e minúsculas
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        strength += 1
        
    # Verifica se a senha contém números
    if any(c.isdigit() for c in password):
        strength += 1
        
    # Verifica se a senha contém caracteres especiais
    if any(c in string.punctuation for c in password):
        strength += 1
        
    return strength

# Função usada para solicitar um token de acesso para o usuário. 
# Se o usuário estiver no banco de dados, a função chama a função send_access_token() 
# para gerar um novo token e atualiza o banco de dados com o novo token.
def request_access_token(user, message_label):
    # Verifica se o usuário está no banco de dados
    if user not in users:
        message_label.config(text="Usuário não encontrado. Tente novamente.")
    else:
        users[user]['access_token'] = send_access_token(user)
        message_label.config(text=f"Token de acesso enviado para {user}.")

# Função responsável por verificar o login do usuário com autenticação de dois fatores. 
# A função verifica se o usuário está no banco de dados, se a senha informada está correta
#  e solicita o token de acesso. Se o login for bem-sucedido, a função exibe uma mensagem 
# de boas-vindas e a força da senha.
def two_factor_auth(user, password_entry, token_entry, message_label, strength_label):
    # Verifica se o usuário está no banco de dados
    if user not in users:
        message_label.config(text="Usuário não encontrado. Tente novamente.")
    elif password_entry.get() != users[user]['password']:
        message_label.config(text="Senha incorreta. Tente novamente.")
    else:
        message_label.config(text="Bem-vindo(a)!")
        strength = check_password_strength(password_entry.get())
        strength_label.config(text=f"Força da senha: {strength}/4")
        password_entry.delete(0, tk.END)
        token_entry.delete(0, tk.END)
        # Solicitar o token de acesso
        request_access_token(user, message_label)

# Função utilizada para verificar se o token de acesso informado pelo usuário é válido. 
# A função verifica se o usuário está no banco de dados e se o token informado é igual 
# ao token armazenado no banco de dados.
# Função utilizada para verificar se o token de acesso informado pelo usuário é válido. 
# A função verifica se o usuário está no banco de dados e se o token informado é igual 
# ao token armazenado no banco de dados.
def verify_access_token():
    user = username_entry.get()
    if user in users:
        token = access_token_entry.get()
        if token == users[user]['access_token']:
            message_label.config(text="Token válido.")
            
            # Cria a nova janela de login bem-sucedido
            success_window = tk.Toplevel(root)
            success_window.title("Login bem-sucedido")
    
            # Cria o rótulo para exibir a mensagem de boas-vindas
            welcome_label = tk.Label(success_window, text="Bem-vindo(a) ao sistema!")
            welcome_label.pack()
    
             # Cria um botão para fechar a janela de login bem-sucedido e a janela principal
            def close_windows():
                success_window.destroy()
                root.destroy()
            close_button = tk.Button(success_window, text="Fechar", command=close_windows)
            close_button.pack()
            
            # Esconde a janela principal
            root.withdraw()
        else:
            message_label.config(text="Token inválido. Tente novamente.")
    else:
        message_label.config(text="Usuário não encontrado. Tente novamente.")

# Banco de dados de usuários e senhas
users = {
    'user1': {'password': "Senha12345!", 'access_token': ""},
    'user2': {'password': "Senha12345@", 'access_token': ""},
    'user3': {'password': "Senha12345#", 'access_token': ""}
}

# Cria a janela principal
root = tk.Tk()
root.title("Login")

# Cria os widgets da interface
username_label = tk.Label(root, text="Nome de usuário:")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Senha:")
password_entry = tk.Entry(root, show="*")
access_token_label = tk.Label(root, text="Token de acesso:")
access_token_entry = tk.Entry(root)
submit_button = tk.Button(root, text="Entrar", command=lambda: two_factor_auth(username_entry.get(), password_entry, access_token_entry, message_label, strength_label))
verify_token_button = tk.Button(root, text="Verificar token", command=verify_access_token)
message_label = tk.Label(root, text="Digite seu nome de usuário e senha")
strength_label = tk.Label(root, text="Força da senha:")

# Posiciona os widgets na janela
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
access_token_label.grid(row=5, column=0)
access_token_entry.grid(row=5, column=1)
strength_label.grid(row=4, column=0, columnspan=2)
submit_button.grid(row=3, column=0, columnspan=2)
verify_token_button.grid(row=6, column=0, columnspan=2)
message_label.grid(row=0, column=0, columnspan=2)

# Inicia o loop da interface gráfica
root.mainloop()