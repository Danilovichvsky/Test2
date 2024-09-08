import threading

def calc(n = 1):
    if n <= 1:
        return 1
    return n * calc(n-1)

def res_(n):
    res = calc(n)
    for _ in range(5):
        print(f"Факториал {n} равен {res}\n")
        print(threading.current_thread().name)

thr1 = threading.Thread(target=res_, args=(5,), name="поток 1",daemon=True)
thr1.start()
print("End")






