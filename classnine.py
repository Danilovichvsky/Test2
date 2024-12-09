class Ad:
    def __init__(self, chislo):
        self.ch = chislo

    def __add__(self, other):
        if isinstance(other, Ad):
            oth = other.ch
            return Ad(self.ch + oth)
        else:
            return Ad(self.ch + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f"результат={str(self.ch)}"

    def __repr__(self):
        return str(self.ch)

ob = Ad(100)
res = 2 + ob
print(res)
