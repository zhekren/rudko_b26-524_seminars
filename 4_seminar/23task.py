import re

def del_spaces(stroke):
    stroke = re.sub(r' +', ' ', stroke).strip()
    return stroke

print(del_spaces("Это   строка    с     большим    количеством   пробелов."))
print(del_spaces("   Текст   с   пробелами   "))