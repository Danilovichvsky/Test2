class A():
    def __init__(self):
        print("init is calles")

    def __call__(self, some):
        print(some)


a = A()
a('some value')  # some value

gen_compr = (2 * (-5) ** i for i in range(6))
for el in gen_compr:
    print(el)

print([i for i in range(0,6)])