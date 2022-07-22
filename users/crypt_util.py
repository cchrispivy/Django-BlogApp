from cryptography.fernet import Fernet

class Crypt():
    key = '81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs=' 
    cipher = Fernet(key)

    def encrypt_token(self, value):
        return self.cipher.encrypt(value)

    def decrypt_token(self, value):
        return self.cipher.decrypt(value)
