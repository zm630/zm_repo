#3.有个列表 [“hello”, “world”, “yoyo”]，
# 如何把列表里面的字符串联起来，
# 得到字符串 “hello_world_yoyo”？
list=["hello", "world", "yoyo"]
new_list=" ".join(list)
print(new_list)
print(type(new_list))
new_list=new_list.replace(" ","_")
print(new_list)



