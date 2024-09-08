import multiprocessing
import time

# Глобальный локер для синхронизации вывода
locker = multiprocessing.Lock()


def f1(el):
    with locker:  # Используем контекстный менеджер для автоматического захвата/освобождения локера
        time.sleep(0.3)
        print('str', el)


if __name__ == '__main__':
    print("Количество ядер:", multiprocessing.cpu_count())

    start = time.time()

    # Создаем пул процессов с количеством процессов, равным числу ядер
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        p.map(f1, list(range(10)))  # Передаем список для параллельной обработки

    end = time.time()
    print("Общее время: ", end - start)
