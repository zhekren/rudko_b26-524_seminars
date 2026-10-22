from io import StringIO

def count_lines(stream):
    count = 0
    for line in stream:
        print(line.rstrip())
        count += 1
    return count

with open('/Users/jokovich/Desktop/Python_basics/4_seminar/data.txt', "r", encoding="utf-8") as file:
    print(count_lines(file), "\n")

with open('/Users/jokovich/Desktop/Python_basics/4_seminar/14task.py', "r", encoding="utf-8") as file:
    print(count_lines(file),"\n")

print(count_lines(StringIO("first\nsecond\nthird")), "\n")