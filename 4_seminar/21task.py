import re

login = input("Введите логин: ")

def is_valid_login(login):
    if re.fullmatch(r'[a-zA-Z][a-zA-Z0-9_]{3,15}', login):
        return True
    else:
        return False

print(is_valid_login(login))