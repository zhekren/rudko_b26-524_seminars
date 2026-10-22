from pathlib import Path

class InvalidDirectoryError(Exception):
    pass

def py_analyse():
    catalog = input("Введите каталог:")
    extension = input("Введите расширение:")
    base_dir = Path(catalog)
    if base_dir.is_dir():

        files = [str(p) for p in base_dir.rglob('*' + extension) if p.is_file()]
        for i in range(len(files)):
            files[i] = [files[i], Path(files[i]).stat().st_size]
        print(files)

    else:
        raise InvalidDirectoryError(f"Путь не найден")

py_analyse()