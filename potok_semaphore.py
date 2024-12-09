import threading
import time

# Создаем семафор, который позволяет одновременно работать с ресурсом не более 2 потокам
semaphore = threading.Semaphore(2)

def worker(thread_id):
    print(f"Поток {thread_id} ожидает доступ к ресурсу")
    with semaphore:  # Захватываем семафор
        print(f"Поток {thread_id} получил доступ к ресурсу")
        time.sleep(2)  # Симуляция работы с ресурсом
        print(f"Поток {thread_id} освободил ресурс")

# Запускаем 5 потоков
threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()

print("Все потоки завершили работу")



def worker(thread_id):
    print(f"Поток {thread_id} достиг барьера")
    barrier.wait()  # Ждем, пока все потоки достигнут барьера
    print(f"Поток {thread_id} продолжает выполнение после барьера")

# Создаем барьер для 3 потоков
barrier = threading.Barrier(3)

# Запускаем 3 потока
threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()


x=5
def ss():
    return x+5

r = ss()
print(r)