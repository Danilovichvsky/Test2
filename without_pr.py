import multiprocessing
import time

def calc_and_print():
    res = 1
    #print(multiprocessing.current_process().name)
    for element in range(1,4):
        res *= element
    print(res)

def some():
    el = 0
    while el<5:
        print(f"{multiprocessing.current_process().name}")
        time.sleep(0.5)
        el+=1

if __name__ == '__main__':
    time_start = time.time()
    calc_and_print()
    some()
    time_end = time.time()
    print("total_time: ",time_end - time_start)