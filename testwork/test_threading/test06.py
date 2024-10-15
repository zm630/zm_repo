import threading
import time

def print_strA(con):
    con.acquire()
    while True:
        for i in range(0,10):
            time.sleep(0.2)
            print(f"我是{i}")
            con.notify()
            con.wait()
        break
    con.release()
def print_strB(con):
    con.acquire()
    while True:
        for i in range(0,10):
            # time.sleep(0.2)
            print(i)
            con.notify()
            con.wait()
        break
    con.release()
con= threading.Condition()
t1 = threading.Thread(target=print_strA,args=(con,))
t2 = threading.Thread(target=print_strB,args=(con,))
t1.start()
t2.start()