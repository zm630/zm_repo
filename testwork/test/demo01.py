
data_set3 = {1,2,3,4,5}
data_set4 = {6,7,8,9,1}
diff_data_set1 = data_set3.difference(data_set4)
diff_data_set2 = data_set4.difference(data_set3)
# print(diff_data_set1)
# print(diff_data_set2)

#4.进程间不共享全局变量.py
import multiprocessing
import time

# 全局变量
my_list = []

def write_func():
    for data in range(1,3):
        my_list.append(data)
        print("write: %d" % data)
    print("write_func:", my_list)

def read_func():
    print("read_func:", my_list)

if __name__ == '__main__':
    # 创建写入数据进程
    write_target = multiprocessing.Process(target = write_func)
    # 创建读取数据进程
    read_target = multiprocessing.Process(target=read_func)

    write_target.start()
    time.sleep(1) #增加效果几率
    read_target.start()

import multiprocessing
import time


def work():
    for data in range(1, 10):
       print("work...")
    time.sleep(0.2)


if __name__ == '__main__':
    work_target = multiprocessing.Process(target=work)
    work_target.start()

    time.sleep(1)
    print("主进程任务结束")