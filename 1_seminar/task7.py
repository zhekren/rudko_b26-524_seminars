import re
import faker

def count_words_in_file(file_path):
    word_count = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count

def get_top_n_words(word_count, n=10):
    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:n]


def generate_test_file(file_path, num_sentences=10000):
    fake = faker.Faker()
    with open(file_path, 'w', encoding='utf-8') as file:
        for _ in range(num_sentences):
            sentence = fake.sentence()
            file.write(sentence + '\n')



if __name__ == "__main__":
    test_file_path = 'test_file.txt'
    generate_test_file('/Users/jokovich/Desktop/Python_basics/1_seminar/generation.txt')

    word_count = count_words_in_file('/Users/jokovich/Desktop/Python_basics/1_seminar/generation.txt')

    top_words = get_top_n_words(word_count, 10)
    
    print("10 наиболее часто встречающихся слов:")
    for word, count in top_words:
        print(f"{word}: {count}")
