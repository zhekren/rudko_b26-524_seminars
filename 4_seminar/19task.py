import re

def phone_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(r'(?:\+7|8) (?:\d{3}|\(\d{3}\)) \d{3}-\d{2}-\d{2}', content)

    for i in matches:
        print(i)

phone_numbers('/Users/jokovich/Desktop/Python_basics/4_seminar/phone_numbers.txt')