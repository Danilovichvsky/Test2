

def dec(f):
    def wr(a,b):
        res = sum(a,b)
        return f"result is {res}"
    return wr
def sum(a,b):
    return a+b

decorated = dec(sum)
res = decorated(3,4)
print(res)


def counter(start = 0):
    def step():
        nonlocal start
        start+=1
        return start
    return step

c1 = counter(10)
c2= counter()
print(c1(),c2())
print(c1(),c2())
print(c1(),c2())