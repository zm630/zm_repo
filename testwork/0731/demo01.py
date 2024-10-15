data_list=["ab1","123ad","bca","dadfadf","dddaaa","你好啊","我来啦","别跑啊"]
index=0
new_data_list=[]
while index<len(data_list):
    print(data_list[index])
    for i in data_list[index]:
        if i>"0" and i<"9":
            data_list.remove(data_list[index])
            print(data_list)



