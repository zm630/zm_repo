#有100个数据，启动5个线程，每个线程分20个数据，怎么把这20个数据分别传给每个线程。

import threading
data=list(range(100))
# def work(data_list):
#     for i in data_list:
#         print(i)

data_split=[]
for i in range(0,100,20):
    data_split.append(data[i,i+20])
    print(data_split)

