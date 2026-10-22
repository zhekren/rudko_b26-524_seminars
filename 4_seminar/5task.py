import json
import copy

def students(file_path_toread, file_path_towrite):
    super_student = {'score': 0}

    with open (file_path_toread, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        for i in range(len(data)):
            data[i]['passed'] = 'yes' if data[i]['score'] >= 60 else 'no'
            if data[i]['score'] > super_student['score']:
                super_student = copy.deepcopy(data[i])

    super_student['best_student_name'] = super_student['name']
    del super_student['name']
    data.append(super_student)

    with open(file_path_towrite, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)

students('/Users/jokovich/Desktop/Python_basics/4_seminar/students_input.json', '/Users/jokovich/Desktop/Python_basics/4_seminar/students_output.json')