import multiprocessing
import time


def start_and_end_decorator(func):
    def wrapper(*args, **kwargs):
        # Вызываем оригинальную функцию и получаем результат
        list_res = func(*args, **kwargs)
        # Умножаем результаты на 2
        new_l = [el * 2 for el in list_res]
        return new_l
    return wrapper

# Применяем декоратор
@start_and_end_decorator
def print_table_of_squares(start, end):
    list_r = []
    for i in range(start, end + 1):
        square = i * i
        print(f"square of {i} is {square}")
        list_r.append(square)
    return list_r

# Вызываем функцию
result = print_table_of_squares(1, 3)
print(f"Результаты с умножением на 2: {result}")

def decor_some(f):
    def wrap():
        start = time.time()
        f()
        end = time.time()
        print("total time: ",end-start)
        return end-start
    return wrap
def some():
    for i in range(5):
        time.sleep(0.2)
        print("Hi")

some = decor_some(some)
some()

