class log_operation:

    def __init__(self, filename, operation_name):
        self.filename = filename
        self.operation_name = operation_name

    def __enter__(self):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f'START: {self.operation_name}\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.filename, 'a', encoding='utf-8') as file:
            if exc_type is not None:
                file.write(f'ERROR: {self.operation_name}\n')
            else:
                file.write(f'END: {self.operation_name}\n')

        return False


with log_operation('/Users/jokovich/Desktop/Python_basics/4_seminar/operation.log', 'Data processing'):
    res = 1/1
    print('Выполнение операции...')