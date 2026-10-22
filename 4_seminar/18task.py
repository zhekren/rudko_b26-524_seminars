import json
import re
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [logging.StreamHandler()]
)


def writing_json(file_path, data):
    logging.info(f'Начало записи результатов в файл: {file_path}')
    
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    logging.info(f'Данные успешно записаны в {file_path}')


def reading_log(file_path_toread, file_path_towrite):
    logging.info(f'Запуск обработки лог-файла: {file_path_toread}')
    
    try:
        IPs = []
        HTTP_methods = []
        URLs = []
        code_responses = []

        lines_count = 0
        with open(file_path_toread, 'r', encoding='utf-8') as file:
            for line in file:
                IPs.append(re.search(r'(\d+\.\d+\.\d+\.\d+)', line).group())
                HTTP_methods.append(re.search(r'\b(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|CONNECT|TRACE)\b', line).group())
                URLs.append(re.search(r'(/[\w/.]+)', line).group())
                code_responses.append(re.search(r'(\d{3})$', line).group())
                lines_count += 1
        
        logging.info(f'Файл успешно прочитан. Обработано строк: {lines_count}')

        logging.info('Расчет статистических показателей...')

        counter_HTTP_methods = len(set(HTTP_methods))
        counter_4xx_errors = len([code for code in code_responses if code[0] == '4'])

        most_frequent_URL = URLs[0] if URLs else 'Нет данных'
        for i in range(len(URLs)):
            if URLs.count(URLs[i]) > URLs.count(most_frequent_URL):
                most_frequent_URL = URLs[i]
        
        output_data  = {
            'Количество запросов каждого типа': counter_HTTP_methods,
            'Количество ошибок 4xx': counter_4xx_errors,
            'Наиболее частый URL': most_frequent_URL
        }
        writing_json(file_path_towrite, output_data)

        logging.info('Обработка лога полностью завершена')

    except FileNotFoundError:
        logging.error('Ошибка: файл не найден')
        return []
    except IOError:
        logging.error(f'Ошибка: произошла ошибка I/O при чтении файла')
        return []

reading_log('/Users/jokovich/Desktop/Python_basics/4_seminar/access.log', '/Users/jokovich/Desktop/Python_basics/4_seminar/output_log.json')