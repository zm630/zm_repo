#.题目 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并
# (将字母全部转换为大写), 输出到一个新文件C中。

fileA=open("A.txt","w").write("jschbchsj")
fileB=open("B.txt","w").write("wjfbejherg")

with open("A.txt","r") as file:
    for data1 in file:
        data1 = data1.upper()
        fileC = open("C.txt", "a").write(data1)
    with open("B.txt","r") as file:
        for data2 in file:
            data2 = data2.upper()
            fileC = open("C.txt", "a").write(data2)



