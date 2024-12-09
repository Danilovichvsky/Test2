import threading
import time

v = 0
def some():
    global v
    while True:
        lock.acquire()
        v +=1
        time.sleep(1)
        lock.release()
        print(v)

lock = threading.Lock()

for _ in range(5):
    thr = threading.Thread(target=some)
    #thr.start()
    #thr.join()


