import csv

def write_csv(file_path, data):

    with open(file_path, 'w', encoding = 'utf-8', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'category', 'price'])
        for row in data:
            writer.writerow(row)

def prices(file_path):

    with open(file_path, 'r', encoding = "utf-8", newline = '') as file:
        data = []
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            row[2] = int(row[2])
            if row[2] > 100:
                data.append(row)

        write_csv('/Users/jokovich/Desktop/Python_basics/4_seminar/expensive.csv', data)
            
            
prices('/Users/jokovich/Desktop/Python_basics/4_seminar/products.csv')