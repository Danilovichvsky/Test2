import datetime


class Stripchars:
    def __init__(self,chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0],str):
            raise TypeError("error")
        print(args)
        print(kwargs)
        return args[0].strip(self.__chars)

o1 = Stripchars("!,? ")
res = o1("Hi! Baby?",name="Bye, Baby?")
print(res)

def add_calc(target):

    def calc(self):
        return 42

    target.calc = calc
    return target


class MyClass:
    def __init__(self):
        print("MyClass __init__")

MyClass = add_calc(MyClass)
my_obj = MyClass()
print(my_obj.calc())


import time

class Dek:
    _instance = None

    def __new__(cls, func):
        if cls._instance is None:
            # Создаем новый экземпляр только если он еще не существует
            cls._instance = super().__new__(cls)
            # Инициализируем функцию
            #cls._instance.func = func
        return cls._instance

    def __init__(self, func):
        # Инициализация только при первом создании
        if not hasattr(self, 'func'):
            self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()  # Запись времени начала
        self.func(*args, **kwargs)  # Вызов обернутой функции
        end = time.time()  # Запись времени окончания
        print("Time taken: {:.6f} seconds".format(end - start))  # Вывод времени выполнения
        #return result

def func_hi(name):
    # Добавляем задержку для демонстрации измерения времени
    time.sleep(1)
    print("Hi {}".format(name))

# Создаем экземпляр Dek и передаем функцию
decorated_func_hi = Dek(func_hi)
decorated_func_hi("dan")

# Попытка создать второй экземпляр Dek
obj2 = Dek(func_hi)
print(id(decorated_func_hi))  # Вывод идентификатора первого экземпляра
print(id(obj2))              # Вывод идентификатора второго экземпляра

