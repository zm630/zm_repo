#2.求两个List列表中的相同元素和不相同元素
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
set1=set(list1)
set2=set(list2)
same=set1.intersection(set2)
print(same)
dif=set1.symmetric_difference(set2)
print(dif)
dif1=set1.union(set2)#交集
print(dif1)