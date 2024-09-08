# Определение метакласса
class MyMeta(type):
    def __init__(cls, name, bases, dct):
        # Вызов инициализатора базового метакласса
        super().__init__(name, bases, dct)

        # Добавление нового атрибута в класс
        cls.custom_attr = "Я добавлен метаклассом!"

        # Вывод сообщения при инициализации класса
        print(f"Класс {name} инициализирован с метаклассом MyMeta")


# Использование метакласса
class MyClass(metaclass=MyMeta):
    def __init__(self):
        print("Экземпляр класса MyClass создан")


# Создание экземпляра класса
obj = MyClass()

# Доступ к атрибуту, добавленному метаклассом
print(obj.custom_attr)  # "Я добавлен метаклассом!"
