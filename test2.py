import threading
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
thr1 = threading.Thread(target=f1,args=(1000,))

thr2 = threading.Thread(target=f2)
thr1.start()
thr2.start()
thr1.join()
thr2.join()
end = time.time()

# Виведення часу з точністю до тисячних
execution_time = end - start
print(f"Total time: {execution_time} seconds")
from tkinter import *
tk = Tk()
def print1():
    l = []
    for i in range(10):
        if i % 2 == 0:
            #time.sleep(0.5)
            l.append(i)
    label1 = Label(text=f"{l}")
    label1.pack()

def print2():
    l = []
    for i in range(10):
        if i % 2 == 0:
            l.append(i)
            time.sleep(0.5)
    label2 = Label(text=f"{l}")
    label2.pack()
#def start_thr1():
    #thr1 = threading.Thread(target=print1)
    #thr1.start()

def start_thr2():
    thr2 = threading.Thread(target=print2)
    thr2.start()

btn1 = Button(text="calc1",command=print1)
btn1.pack()

btn2 = Button(text="calc2",command=start_thr2)
btn2.pack()

tk.geometry("300x400")
tk.mainloop()
