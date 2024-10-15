#写一个程序，将两个列表合并成一个有序的列表
list1=[2,45,34,23,42]
list2=[24,54,34,42,7,]
new_list=sorted(list1+list2)
print(new_list)

#.写一个程序，找出两个列表中的相同元素
new_list1=set(list1) & set(list2)
print(new_list1)

#写一个程序，找出两个列表中的不同元素
new_list2=set(list1) ^ set(list2)
print(new_list2)

#写一个程序，将一个列表中的元素去重
list3=[1,1,2,2,3,3,4,5,6,6]
set_list=list(set(list3))  #转换为集合又转换为列表
print(set_list)

#写一个程序，将一个字符串中的所有字母转换为小写并去除空格
text = "Hello World! I Am A Python Developer."
new_text=text.lower().replace(" ","")
print(new_text)
