#4.从下标 0 开始索引，找出单词 “welcome”
# 在列表["Hello","welcome " ,"to" , "my" ," world”
# 中出现的位置，找不到返回 -1。
list=["Hello","welcome","to","my","world"]
index=0
for i in range(0,len(list)):
    if list[i]=="welcome":
        print(list.index("welcome"))
        break
    index+=1
