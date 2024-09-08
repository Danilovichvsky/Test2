d=[1,2,3,4,5]
it=iter(d)

print(next(it))
print(next(it))

inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

inputdata2=list(filter(lambda x: x[::-1].lower()==x.lower(),inputdata))
print(inputdata2)

class Descript:
    def __set_name__(self, owner, name):
        self.name = "_"+name

    def __get__(self, instance, owner):
        # Get the value from instance's __dict__
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        # Set the value in instance's __dict__
        setattr(instance,self.name,value)

class notDescript:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        # Get the value from instance's __dict__
        return getattr(instance, self.name, None)

    #def __set__(self, instance, value):
       # # Set the value in instance's __dict__
     #   setattr(instance,self.name,value)

class MyClass:
    x = Descript()
    y = Descript()
    #z = Descript()
    new = notDescript()
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
# Пример использования
obj = MyClass(1,2,3)
obj.__dict__['new'] = 5
obj.z = 4
print("z =",obj.z)

print(obj.new,obj.__dict__)  # Проверяем __dict__ объекта

class Borg:
    shared = {}
    def __init__(self):
        self.__dict__ = self.shared
        #self._shared = self.__dict__

borg_1 = Borg()
borg_1.value = 1
borg_2 = Borg()
print(borg_2.value)


print(borg_1.__dict__)

l = []
s = l
s.append(1)
print("l=",l)
print("s=",s)

list_g = (i for i in range(1000))
print(list(list_g))

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in list_a)
print(sum(my_gen))  # 12
print(sum(my_gen))  # 0

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

def fact2(n):
    ch = 1
    while n > 1:
        ch *= n  # Умножаем текущий результат на n
        n -= 1   # Уменьшаем n на 1, чтобы продолжить умножение на следующее число

    return ch

print(fact2(5))  # Ожидаемый результат: 120


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x
def fibonacci_numbers2(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        return x

def square(nums):
    for num in nums:
        yield num ** 2
print("----")
for i in fibonacci_numbers(4):
    print(i)


print(sum(square(fibonacci_numbers(10))))

""" 
Создать генератор геометрической прогрессии.

При задании начала прогрессии -2 и шага прогрессии -5,

генератор выдаёт такую последовательность:
"""

def geom_pr(n,start,step):
    for _ in range(n):
        yield start
        start*=step


gen_f = geom_pr(6,10,3)
for el in gen_f:
    print(el)
