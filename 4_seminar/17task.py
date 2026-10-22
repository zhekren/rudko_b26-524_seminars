from faker import Faker

fake = Faker()
def faking(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for _ in range(100000):
            number = fake.random_int(min = -100000, max = 100000)
            file.write(f"{number}\n")


def analyze_numbers(file_path):
    summi = 0
    mini = 9999999999
    maxi = -9999999999
    counter = 0
    middle = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            counter += 1
            number = int(line)
            summi += number
            mini = min(mini, number)
            maxi = max(maxi, number)
    middle = summi/counter
    return summi, mini, maxi, counter, middle

faking('/Users/jokovich/Desktop/Python_basics/4_seminar/big_file_numbers.txt')
print(analyze_numbers('/Users/jokovich/Desktop/Python_basics/4_seminar/big_file_numbers.txt'))