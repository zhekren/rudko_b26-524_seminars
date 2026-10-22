import re
from pprint import pprint

def get_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    URLs = re.findall(r'https?://[\w./]+', content)
    pprint(URLs)

get_urls('/Users/jokovich/Desktop/Python_basics/4_seminar/URLs.txt')