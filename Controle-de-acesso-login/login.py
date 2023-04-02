#  Prof. Ausberto S. Castro Vera
#  Disciplina : Segurança Computacional
#  UENF-CCT-LCMAT-CC
#  Data: Abril 2023
#  Aluno: Rômulo Souza Fernandes

import random
import string
import tkinter as tk

# Função para enviar um token de acesso para o usuário
def send_access_token(user):
    token = ''.join(random.choice(string.ascii_letters + string.digits)
                    for i in range(6))
    print(f"Token de acesso enviado para {user}: {token}")
    return token

# Função para verificar a força da senha
def check_password_strength(password):
    # Inicializar a força da senha como 0
    strength = 0
    
    # Verificar o comprimento da senha
    if len(password) >= 8:
        strength += 1
    
    # Verificar se a senha contém letras maiúsculas e minúsculas
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        strength += 1
        
    # Verificar se a senha contém números
    if any(c.isdigit() for c in password):
        strength += 1
        
    # Verificar se a senha contém caracteres especiais
    if any(c in string.punctuation for c in password):
        strength += 1
        
    return strength

# Função para verificar o login com autenticação de dois fatores
def two_factor_auth(user, password_entry, token_entry, message_label, strength_label):
    # Verificar se o usuário está no banco de dados
    if user not in users:
        message_label.config(text="Usuário não encontrado. Tente novamente.")
    elif password_entry.get() != users[user]['password']:
        message_label.config(text="Senha incorreta. Tente novamente.")
    elif token_entry.get() != users[user]['access_token']:
        message_label.config(text="Token de acesso inválido. Tente novamente.")
    else:
        message_label.config(text="Bem-vindo(a)!")
        strength = check_password_strength(password_entry.get())
        strength_label.config(text=f"Força da senha: {strength}/4")
        password_entry.delete(0, tk.END)
        token_entry.delete(0, tk.END)

# Banco de dados de usuários e senhas
users = {
    'user1': {'password': "Senha123!@#", 'access_token': send_access_token('user1')},
    'user2': {'password': "Senha123!@#", 'access_token': send_access_token('user2')},
    'user3': {'password': "Senha123!@#", 'access_token': send_access_token('user3')}
}

# Criar a janela principal
root = tk.Tk()
root.title("Login")

# Criar os widgets da interface
username_label = tk.Label(root, text="Nome de usuário:")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Senha:")
password_entry = tk.Entry(root, show="*")
token_label = tk.Label(root, text="Token de acesso:")
token_entry = tk.Entry(root)
submit_button = tk.Button(root, text="Entrar", command=lambda: two_factor_auth(username_entry.get(), password_entry, token_entry, message_label, strength_label))
message_label = tk.Label(root, text="Digite seu nome de usuário")
strength_label = tk.Label(root, text="Força da senha:")

# Posicionar os widgets na janela
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
token_label.grid(row=2, column=0)
token_entry.grid(row=2, column=1)
strength_label.grid(row=3, column=0, columnspan=2)
submit_button.grid(row=4, column=0, columnspan=2)
message_label.grid(row=5, column=0, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()