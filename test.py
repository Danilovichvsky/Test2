import time

# Оригінальні функції
def f1(i: int):
    l = []
    for ind, _ in enumerate(range(i)):
        print(f"{ind}: {_}")
        l.append(_)
    return l

def f2():
    l2 = []
    for i in range(10000):
        l2.append(i)
    print(l2[-1:])

# Замір часу виконання до тисячних
start = time.time()
f1(1000)
f2()
end = time.time()

# Виведення часу з точністю до тисячних
execution_time = end - start
print(f"Total time: {execution_time} seconds")
