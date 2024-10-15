import threading
lock = threading.Lock()
ticket=100

def sell_ticket():
    global ticket
    while (True):
        lock.acquire()
        if ticket>0:
            print(threading.current_thread().name,f"正在卖第{ticket}张票")
            ticket-=1
        lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=sell_ticket,name="窗口1")
    t2 = threading.Thread(target=sell_ticket,name="窗口2")
    t3 = threading.Thread(target=sell_ticket,name="窗口3")
    t1.start()
    t2.start()
    t3.start()