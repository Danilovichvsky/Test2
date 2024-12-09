from multiprocessing import Process, Pipe

def get_info(pipe):
    get, _ = pipe  # Мы используем только get

    while True:
        try:
            data = get.recv()  # Корректный вызов метода recv
            print("data:", data)

        except EOFError:
            break
    get.close()

def set_info(pipe, listus):
    _, set_pipe = pipe  # Мы используем только set
    for el in listus:
        set_pipe.send(el)
    set_pipe.close()  # Закрываем pipe после отправки всех данных



if __name__ == '__main__':
    get, set = Pipe()  # Создание канала

    p1 = Process(target=get_info, args=((get, set),))
    p2 = Process(target=set_info, args=((get, set), [1, 2, 3, 4, 5]))

    p1.start()
    p2.start()

    p1.join()  # Ждем завершения процессов
    p2.join()

