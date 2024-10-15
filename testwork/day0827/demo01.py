"""
进程的入门
"""
import multiprocessing
def func():
    for i in range(0,10):
        print(i)
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=func)
    process1.start()