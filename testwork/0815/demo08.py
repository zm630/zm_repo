list1=[2,3,6,4,67,5,4]
# list=list1[4:2:-1]
list=sorted(list1)
print(list)

data_dict = {"aaa":"bbb","ccc":"ddd","aaa":"zzz","xxx":"ddd"}
for key in data_dict.keys():
    value=data_dict.get(key)
    print(key,"==",value)


data_l1 = [1,2,3,4,5]
data_l2 = [6,2,3,4,5]
print(set(data_l1) ^ set(data_l2))