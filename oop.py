import math

class Descript:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # Получаем значение из __dict__ без рекурсии
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        # Устанавливаем значение в словаре __dict__ экземпляра
        instance.__dict__[self.name] = value

class Robot:
    hand = ["left", "right"]
    __diction = {'name': 'Vas'}
    ROB_NAME = "Slon"
    x = Descript()
    y = Descript()
    z = Descript()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __del__(self):
        print("объект удален " + str(self))

    def __setattr__(self, key, value):
        if key == 'a':
            raise AttributeError("нельзя установить значение для a")
        else:
            super().__setattr__(key, value)

    @classmethod
    def get_rob_name(cls):
        print(cls.ROB_NAME)

    @staticmethod
    def add_to_func(f, number=2):
        def wrapper(*args, **kwargs):
            print("----start moving----", number)
            f(*args, **kwargs)
            print("----end moving----")
        return wrapper

    @staticmethod
    def get_square(func):
        def wrapper(*args, **kwargs):
            res1 = func(*args, **kwargs)
            res2 = math.sqrt(res1)
            return res2
        return wrapper

    @get_square
    def math_f(self):
        sum = self.x + self.y + self.z
        return sum

    @add_to_func
    def up_left_hand(self):
        print("left hand is up")

    def __getitem__(self, item):
        return self.ROB_NAME[item]

    def __setitem__(self, key, value):
        if key > len(self.ROB_NAME):
            # Добавляем None до нужного индекса
            non_items = key - len(self.ROB_NAME) + 1
            print("noneitems= ",non_items)
            self.ROB_NAME.extend([None] * non_items)
        self.ROB_NAME[key] = value

# Создание объекта класса Robot
obj1 = Robot(1, 1, 2)
print("class", obj1)
print(obj1.hand)
print(Robot.hand)
if hasattr(Robot, 'hand'):
    print("Present")

print(getattr(Robot, 'hand', False))

# Использование декоратора
print("-" * 50)
obj1.up_left_hand()

obj1.name = "poc"
print(obj1.name)

print("-" * 50)
print(obj1.math_f())

print("+", obj1.x)

# Получение значений x, y, z через дескриптор
print("значение x:", obj1.x)
print("значение y:", obj1.y)
print("значение z:", obj1.z)

# Создание нового объекта класса Robot
name = Robot(3, 5, -1)
name.ROB_NAME = ["Abu", "Vlados","саня","ури"]
print(name.ROB_NAME)
name[1] = "Vladtrans"
name[6] = "vas"
print(name.ROB_NAME)
name[6] = "vasil"
print(name.ROB_NAME)
Robot.x=3
print(Robot.x)

