def numbers_file(file_path, res_path):
    min_num = 0 
    max_num = 0
    count = 0
    sum_num = 0
    mid_num = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            number = line.strip()
            if number.isdigit():
                count += 1
                sum_num += int(number)
                min_num = min(int(number), min_num)
                max_num = max(int(number), max_num)
        mid_num = sum_num / count
    return min_num, max_num, count, sum_num, mid_num

    with open(res_path, 'w', encoding='utf-8') as res_file:
        res_file.write(f'Минимальное число: {min_num}\n')
        res_file.write(f'Максимальное число: {max_num}\n')
        res_file.write(f'среднее арифметическое: {mid_num}\n')

print(numbers_file('/Users/jokovich/Desktop/Python_basics/4_seminar/numbers.txt', '/Users/jokovich/Desktop/Python_basics/4_seminar/result.txt'))
