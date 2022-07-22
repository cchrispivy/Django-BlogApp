from cryptography.fernet import Fernet

def encrypt(value):
    key = '81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs=' 
    cipher = Fernet(key)
    return cipher.encrypt(value)

def decrypt(value):
    key = '81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs=' 
    cipher = Fernet(key)
    return cipher.decrypt(value)
