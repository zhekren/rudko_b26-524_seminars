import re
def emails(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file = file.read()
        return set(re.findall(r"[a-zA-Z0-9!#$%&'*+-/=?^`{|}~]+@[a-zA-Z0-9]+.[a-z]+", file))

print(emails("/Users/jokovich/Desktop/Python_basics/4_seminar/emails.txt"))