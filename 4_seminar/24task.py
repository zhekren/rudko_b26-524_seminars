import re

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]

def analyse_ids(list):
    list_result = []
    for i in range(len(list)):
        if re.fullmatch(r'PRD-[0-9]{5}', list[i]):
            list_result.append(list[i])

    return list_result

print(analyse_ids(products))