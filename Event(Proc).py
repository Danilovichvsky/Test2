import multiprocessing
import time

lock = multiprocessing.Lock()
def func1(event,com_list):
    event.set()
    with lock:
        for el in range(50):
            com_list.append(el)
            print("елемент додан",el )
    event.clear()
    print(com_list)

def func2(event,com_list):
    event.set()
    with lock:
        while len(com_list)!=0:
            deleted_item = com_list.pop()
            print("елемент удален",deleted_item)
    print(com_list)


if __name__ == '__main__':
    event = multiprocessing.Event()
    com_list = multiprocessing.Manager().list()

    first_pr = multiprocessing.Process(target=func1, args=(event,com_list,))
    second_pr = multiprocessing.Process(target=func2, args=(event,com_list,))
    first_pr.start()
    second_pr.start()

    first_pr.join()
    second_pr.join()


