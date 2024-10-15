import threading

def num1(a,b):
    for i in range(a,b):
       print(i,end=' ')

t1 = threading.Thread(target=num1(1,51))
t2 = threading.Thread(target=num1(51,101))
t1.start()
t2.start()