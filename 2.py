class Descriptor:
    #def __set_name__(self, owner, name):
        #self.name = "_"+name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

class MyClass:
    attr = Descriptor()

    def __init__(self):
        self.p = []
    def hi(self,a):
        return "a",a
    class Inner_class:
        X = 10
        Y = 5

# Пример использования
obj = MyClass()
print(obj.__dict__)
obj.attr = 10  # Устанавливаем значение
print(obj.attr)  # Получаем значение: 10
print(obj.__dict__)  # {'attr': 10}
a=5
print(id(a))
b=a
print(id(b))
a=4
print(id(a))
dict = {1:"one",2:"two"}
print("dict id =",id(dict))
dict["3"]="three"
print(id(dict))
print(obj.hi(3))
lista = [1,2,55,32,-1]
for i in lista:
    obj.p.append(i)

print(obj.p)

