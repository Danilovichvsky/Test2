import multiprocessing
import time


def f2(condition,listus):
    with condition:
        condition.wait()
    print("this is 4")

    with condition:
        condition.wait()
        while len(listus)!=0:
            del_el = listus.pop(0)
            print("удален елемент", del_el)
    print(listus)

def f(condition,listus):
    c = 0
    while True:
        with condition:
            if c == 3:
                condition.notify()
        if c == 10:
            break
        c+=1
        print(c)
        time.sleep(0.3)
    print('----------------------next--------------------')
    for el in range(10):
        listus.append(el)
        print("добавлен - ",el)
    with condition:
        condition.notify()
    print(listus)

if __name__ == '__main__':
    cond = multiprocessing.Condition()
    common_list = multiprocessing.Manager().list()
    pr1 = multiprocessing.Process(target=f,args=(cond,common_list,))
    pr2 = multiprocessing.Process(target=f2, args=(cond,common_list,))
    pr1.start()
    pr2.start()

    pr1.join()
    pr2.join()

