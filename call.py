import math
import time


class Derivate:

    def __init__ (self, func):
        self.__fn = func

    def __call__ (self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def df_sin(x):
    return math.sin(x)

a = Derivate(df_sin)
print(a(math.pi/4))

print(hash((1,2)))
print(hash((1,2)))

dict1 = {1:[1,2,3]}
print(dict1)
print(hash("Миша"))

import timeit

list1 = ["Данил", "Алина", "Вася", "Петя"] * 10000  # Увеличиваем размер списка
dict1 = {f"Имя{i}": i for i in range(10000)}  # Увеличиваем размер словаря
dict1["Вася"] = 3  # Добавляем "Вася" в словарь

# Функция для поиска в списке
def search_in_list():
    found_name = ""
    for el in list1:
        if el == "Вася":
            found_name = el
            break
    return found_name

# Функция для поиска в словаре
def search_in_dict():
    return dict1["Вася"]

# Измеряем время поиска в списке
list_time = timeit.timeit(search_in_list, number=100)

# Измеряем время поиска в словаре
dict_time = timeit.timeit(search_in_dict, number=100)

print("Время поиска в списке:", list_time)
print("Время поиска в словаре:", dict_time)
