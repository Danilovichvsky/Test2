import threading

data = threading.local()
def get_data():
    print(data.name)
def thread():
    data.name = threading.current_thread().name
    v = 0
    for _ in range(1,11):
        v+=1
        print(v)
    get_data()


thr1 = threading.Thread(target=thread)
thr1.start()

thr2 = threading.Thread(target=thread)
thr2.start()