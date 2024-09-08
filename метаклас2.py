class Create(type):
    def __new__(cls, name, bases, attrs):
        attrs.update({"first_name":"name"})
        return type.__new__(cls,name, bases, attrs)

class Main(metaclass=Create):
    second_name = "Second Name"

obj = Main()
print(obj.first_name)  # Выведет: Name
