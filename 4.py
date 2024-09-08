class Add:
    def __init__(self, chislo):
        self.chislo = chislo
        self.x = 1
        self.y = 2

    def get_chislo(self):
        print("chislo =",self.chislo)


    def __add__(self, other):
        if isinstance(other,Add):
            ch = other.chislo
            return Add(self.chislo + ch)
        else:
            return Add(other+self.chislo)

    def __sub__(self, other):
        if isinstance(other,int):
            return Add(self.chislo - other)
        elif isinstance(other,Add):
            return Add(self.chislo - other.chislo)
        else:
            print("other  must be int")

    def __isub__(self, other):
        print("__isub__")
        if isinstance(other, int):
             self.chislo -= other
        elif isinstance(other, Add):
            self.chislo -= other.chislo
        else:
            raise TypeError("other must be int or Add")
        return self

    def __rsub__(self, other):
        print("__rsub__")
        if isinstance(other, int):
            return Add(other - self.chislo)
        else:
            raise TypeError("other must be int")

    def __radd__(self, other):
        print("__radd__")
        return self + other

    def __verify_data(self,other):
        if not isinstance(other, (int,Add)):
            raise TypeError("errorchik")
        return other if isinstance(other, int) else other.chislo

    def __eq__(self, other):
        print("__eq__")
        oth = self.__verify_data(other)
        return self.chislo == oth

    def __lt__(self, other):
        print("__lt__")
        oth = self.__verify_data(other)

        return self.chislo < oth

    def __le__(self, other):
        print("__le__")
        oth = self.__verify_data(other)

        return self.chislo <= oth

    def __delattr__(self, item):
        object.__delattr__(self,item)







o = Add(100)
o2 = Add(1)
o1 = Add(-100)
o3 = o2 - o
o3.get_chislo()
o4 = 12+o3
print(type(o4))
o4.get_chislo()
print(o4 == -87)
print(-87 == o4)
print(o4>=o2)
print(hash(o4.x) == hash(o1.x))
iterator = iter(o)
print(next(iterator))



