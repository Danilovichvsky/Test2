import random
import sys
import timeit
from functools import reduce

class Car:
    name = "your_car_name"
    def __init__(self):
        print("Car is inited")

class BMW(Car):
    name = "BMW"
    V = 3.5
    __slots__ = ('model','weight')

    def __init__(self,model,weight):
        self.model = model
        self.weight = weight

    def get_all_data(self):
        print(self.name)
        print(self.model)
        print(self.V)
        print(self.weight)

class Mercedes(Car):
    name = "Mercedes"
    V = 3.5

    def __init__(self, model,weight):
        self.model = model
        self.weight = weight

    def get_all_data(self):
        print(self.name)
        print(self.model)
        print(self.V)
        print(self.weight)

class MyClass:
    def __str__(self):
        # Код формування строкового представлення об'єкта
        return "Строкове представлення об'єкта"

# Використання str() або print() викликає метод __str__
my_instance = MyClass()
print(str(my_instance))
print(my_instance)

bmw1 = BMW('m450',2800)
model_bmw = bmw1.model
print(model_bmw)

merc1 = Mercedes('e450',3000)
model_merc = merc1.model
print(model_merc)

print("BMW: ", sys.getsizeof(bmw1))
print("Merc: ", sys.getsizeof(merc1) + sys.getsizeof(merc1.__dict__))

# Измерение времени выполнения методов
c1 = timeit.timeit(lambda: bmw1.get_all_data(), number=1)
c2 = timeit.timeit(lambda: merc1.get_all_data(), number=1)
print("Время выполнения BMW: ", c1)
print("Время выполнения Mercedes: ", c2)
merc1.new  = "new"
print(merc1.new)
print(merc1.__dict__)


l = [1, 2, 3, 4, 5]
index = 0
res = 1  # Начальное значение для перемножения всех пар

while index < len(l) - 1:  # Проверяем до предпоследнего элемента
    res = l[index] * l[index + 1]
    print(f"Произведение {l[index]} и {l[index+1]}: {res}")
    index += 1  # Увеличиваем индекс для перехода к следующей паре

l = [1, 2, 3, 4, 5]
index = 0
res = 1  # Начальное значение для перемножения всех элементов

while index < len(l):
    res *= l[index]  # Умножаем результат на текущий элемент списка
    index += 1  # Увеличиваем индекс для перехода к следующему элементу

print("Произведение всех чисел:", res)

res = 1
for el in l:
    res*=el
print(res)

#reduce(lambda a,b: a*b, [1,2,3,4,5])

l = [random.randint(0,100) for el in range(10)]
print(l)

matrix = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(random.randint(1, 100))
    matrix.append(row)
for i in matrix:
    print(i)
def f(a):
    if a % 2 == 0:
        return a
ch = filter(lambda a: a % 2 == 0,[1,2,3])
print(list(ch))

list1 = [1,2,3,4,5]
list2 = [6,54,22,11,23]
res = []
for ind1,el1 in enumerate(list1):
    for ind2,el2 in enumerate(list2):
        res.append(el1+el2)
        ind1+=1
        ind2 += 1
print(res)

print(list(zip(list1,list2)))
res = []
for el1,el2 in zip(list1,list2):
    res.append(el1+el2)
print(res)
x = 0
while x<=3:
    print(x)
    x+=1

