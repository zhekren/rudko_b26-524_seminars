import re

def extract_datas(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    datas = re.findall(r'\d{2}.\d{2}.\d{4}', content)

    for data in datas:
        print(data)

extract_datas('Users/jokovich/Desktop/Python_basics/4_seminar/datas_file.txt')