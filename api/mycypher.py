import hashlib


def encrypt(text:str):
    password = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(password)
    return password


