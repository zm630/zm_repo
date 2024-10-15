import multiprocessing
import time
"""
保证多线程之间顺序执行
"""

def dakai():
    time.sleep(3)
    print("打开冰箱")
def fang():
    time.sleep(2)
    print("放入大象")
def guan():
    print("关闭冰箱")

if __name__ == '__main__':
    t1 = multiprocessing.Process(target=dakai)
    t2 = multiprocessing.Process(target=fang)
    t3 = multiprocessing.Process(target=guan)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
