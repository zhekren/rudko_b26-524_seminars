import re

value = input("Введите число:")

def parse_num(value):
    try:
        return float(value)
    except ValueError:
        if not(re.search(r"\d+", value)):
            print("В строке нет цифр")
        raise ValueError("Некорректное значение")
    
try:
    a = parse_num(value)
    print("Введеное число:", a)
except ValueError as e:
    print(e)