import time
from contextlib import contextmanager

def sleep_function(seconds):
    time.sleep(seconds)

input_seconds = float(input("Введите количество секунд для ожидания для проверки работы контекстного менеджера: "))

class Timer:

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.perf_counter()
        execution_time = end_time - self.start_time
        print(f'Время выполнения: {execution_time:.5f} сек.')
        return True


with Timer():
    sleep_function(input_seconds)


import time
from contextlib import contextmanager

@contextmanager
def Timer():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f'Время выполнения: {execution_time:.5f} сек.')


with Timer():
    sleep_function(input_seconds)