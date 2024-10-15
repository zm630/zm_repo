import threading
def print_num1(a,b):
    print('输出偶数：')
    for i in range(a,b):
        if i%2 == 0:
            print(i,end=' ')
def print_num2(a,b):
    print('输出奇数：')
    for i in range(a,b):
        if i%2 != 0:
            print(i,end=' ')

t1 = threading.Thread(target=print_num1(1,101))
print()
t2 = threading.Thread(target=print_num2(1,101))
t1.start()
t2.start()