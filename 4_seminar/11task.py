import re
def logs(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    user_ids = re.findall(r"User (\d+)", logs)
    print("Идентификаторы пользователей:", [int(i) for i in user_ids])

    error_lines = re.findall(r".*ERROR.*", logs)
    print("Cтроки с ERROR:", error_lines)


    error_user_ids = re.findall(r"ERROR User (\d+)", logs)
    print("Идентификаторы пользователей с ошибкой:", [int(i) for i in error_user_ids])

logs("/Users/jokovich/Desktop/Python_basics/4_seminar/logs.txt")