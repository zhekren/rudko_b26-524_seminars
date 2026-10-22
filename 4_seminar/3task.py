import csv

def res_students(file_path):
    middle_score = 0
    count = 0
    max_score = [0]
    groups = []
    rows = []
    with open(file_path, 'r', encoding='utf-8', newline = '') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            rows.append(row)
            if max_score[0] < int(row[2]):
                max_score = [int(row[2]), row[0]]
            groups.append(int(row[1]))
            count += 1
            middle_score += int(row[2])
    middle_score = middle_score / count
    groups = set(groups)
    groups = list(groups)
    groups_summi = [0]*len(groups)
    groups_count = [0]*len(groups)
    for i in range(len(groups)):
        count = 0
        for row in rows:
            if int(row[1]) == groups[i]:
                count += 1
                groups_summi[i] += int(row[2])
                groups_count[i] = count
    middle_score = middle_score / count
    for i in range(len(groups)):
        groups[i] = [groups[i], groups_summi[i] / groups_count[i]]

    return middle_score, max_score, groups

print(res_students('//Users/jokovich/Desktop/Python_basics/4_seminar/students.csv'))
