import threading
lock1 = threading.Lock()
lock2 = threading.Lock()
def print_strA():
    lock1.acquire()
    for i in range(0,5):
        print(i)
    lock1.release()
def print_strB():
    lock2.acquire()
    for i in range(5,10):
        print(i)
    print()
    print_strA()
    lock2.release()
t1 = threading.Thread(target=print_strA())
print()
t2 = threading.Thread(target=print_strB())
t1.start()
t2.start()


