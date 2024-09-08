class hashh:
    __obj = None
    """def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super().__new__(cls)
        return cls.__obj"""

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))


a = hashh(1,2)
b = hashh(1,2)
print(a == b)
print(hash(a))
print(hash(b))
print(id(a))
print(id(b))


#print(getattr(hashh,a.x))
class B:
    ...
print("B:",hash(B))

a=b
a=3
print(b)
print(bool(B))