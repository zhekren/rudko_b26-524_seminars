def analyze_file(file_path):
    line_count = 0
    word_count = 0
    char_count = 0
    max_line_length = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += len(line)
            max_line_length = max(max_line_length, len(line.rstrip('\n')))
    return line_count, word_count, char_count, max_line_length

print(analyze_file('/Users/jokovich/Desktop/Python_basics/1_seminar/123.txt'))
