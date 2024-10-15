data_list=["ab1","123ad","bca","dadfadf","dddaaa","你好啊","我来啦","别跑啊"]
a=0
while a<len(data_list):
    if (len(data_list[a])>5):
        data_list.remove(data_list[a])
        a-=1
    else:
        a+=1
print(data_list)

a=0
while a<len(data_list):
    if (len(data_list[a])>5):
        data_list.remove(data_list[a])
        a-=1
    else:
        a+=1
print(data_list)

index=0
for i in data_list[index]:
    print(data_list[index])
index += 1
str_data=data_list[index]
print(str_data)

