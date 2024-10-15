#找出列表 a = [“hello”, “world”, “yoyo”, “congratulations”] 中单词最长的一个。
a = ["hello","world","yoyo","congratulations"]
len_min=len(a[0])
for i in a:
    if len(i)>=len(a[0]):
        min=i
print(min)
