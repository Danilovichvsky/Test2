class MyIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._iterable):
            raise StopIteration
        value = self._iterable[self._index]
        self._index += 1
        return value


# Пример использования:
my_list = [10, 20, 30]
iterator = MyIterator(my_list)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
#(next(iterator))  # StopIteration исключение
"""start = 0
while True:
    start+=1
    print(start)
    if start == 10:
        break
print("start is 10")"""

class MyIt:
    def __init__(self,start,end,step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        current = self.start
        if current  > self.end:
            raise StopIteration
        self.start += self.step
        return current


class MyIt2:
    def __init__(self, start, end, step, row):
        self.row = row
        self.start = start
        self.end = end
        self.step = step
        self.current_row = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_row >= self.row:
            raise StopIteration
        myit = MyIt(self.start, self.end, self.step)
        row_it = [val for val in myit]
        self.current_row += 1
        return row_it

ob = MyIt(0,10,2)
it = iter(ob)

#print(next(ob))
#(next(ob))
for el in it:
    print(el)
print("end")
"""
ob2 = MyIt(8,16,2)
for el in ob2:
    print(el)"""
ob2 = MyIt2(0, 10, 2, 7)
for row in ob2:
    print(row)