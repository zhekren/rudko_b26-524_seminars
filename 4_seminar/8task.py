from pathlib import Path
import os

class FileNotExists(Exception):
    pass

class NotFile(Exception):
    pass

class NoRules(Exception):
    pass

def read_file(path):
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotExists(f"Файла или данного пути не существует")
    elif not file_path.is_file():
        raise NotFile(f"Путь не ведёт к файлу")
    elif not os.access(file_path, os.R_OK):
        raise NoRules(f"Отсутствуют права доступа к данному файлу")

    else:
        text = file_path.read_text(encoding = 'utf-8')
        return text

print(read_file('/Users/jokovich/Desktop/Python_basics/4_seminar/8task.py'))
