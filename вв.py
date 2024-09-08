import array
import multiprocessing
import random


def get_data_wr(arr,ind):
    data = 0
    for _ in range(5):
        data = random.randint(0,10)
        arr[ind] = data
    print(f"array[{ind}] = {data}")

n = 10
arr = multiprocessing.Array("i",range(n))
if __name__ == '__main__':
    for pr in range(n):
        processes = multiprocessing.Process(target=get_data_wr,args=(arr,pr,))
        processes.start()
        processes.join()
    print(list(arr))


print("_______")
from multiprocessing import Process, Queue
import time

def producer(queue):
    for i in range(5):
        queue.put(i)
        print(f'Producer put: {i}')
        time.sleep(1)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # Получаем сигнал завершения
            break
        print(f'Consumer got: {item}')
        time.sleep(1.5)

if __name__ == '__main__':
    # Создаем очередь
    queue = Queue()

    # Создаем процессы
    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    # Ждем завершения процесса производителя
    p1.join()

    # Отправляем сигнал завершения в очередь
    queue.put(None)

    # Ждем завершения процесса потребителя
    p2.join()

