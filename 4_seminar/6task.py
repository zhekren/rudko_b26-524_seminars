from pathlib import *

def path_analyse(path):
    base_dir = Path(path)

    file_counter = sum(1 for p in base_dir.rglob('*') if p.is_file())
    dir_counter = sum(1 for p in base_dir.rglob('*') if p.is_dir())
    py_files_counter = [str(p) for p in base_dir.rglob('*.py') if p.is_file()]
    total_size = sum(p.stat().st_size for p in base_dir.rglob('*') if p.is_file())

    return file_counter, dir_counter, py_files_counter, total_size

print(path_analyse('/Users/jokovich/Desktop/Python_basics'))