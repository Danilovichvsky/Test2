class Create(type):
    def __new__(cls, name, bases, attrs):
        attrs.update({"first_name":"name"})
        return type.__new__(cls,name, bases, attrs)

class Main(metaclass=Create):
    second_name = "Second Name"

obj = Main()
print(obj.first_name)  # Выведет: Name


*x,y = 1,2,3
print(y)

factorial = 4
i = 1
res = 1
while i<factorial+1:
    res*=i
    i+=1
print(res)