class MyIt:
    def __init__(self,l=[1,2,3,4,5]):
        self.l = l
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.l):
            raise StopIteration
        result = self.l[self.index]
        self.index += 1
        return result

o = MyIt()
print(o.l)


for index,el in enumerate(o):
    if index % 2 != 0:
        print(el)