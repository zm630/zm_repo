data_list=["abc","def","def","efg","qwe","swd","wwe"]
for i in range(0,len(data_list)):
    print(data_list[3])
    break
print("------------------->")
index=0
while (index<len(data_list)):
    print(data_list[index])
    index += 1

print("------------------->")
index=0
while (index<len(data_list)):
    if (data_list[index]=="def"):
        data_list.remove("def")
    else:
        print(data_list[index])
    index += 1

print("------------------->")
data_list1=[]
for i in data_list:
    data_list1.append(i.upper())
print(data_list1)
data_set=set(data_list1)
print(data_set)
print("------------------->")





