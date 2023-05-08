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
