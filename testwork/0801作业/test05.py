#5.统计字符串“Hello, welcome to my world.” 中字母 w 出现的次数。
str_data="Hello,welcome to my world"
count=0
for i in str_data:
    if i=="w":
        count+=1
print(f"w出现的次数为{count}次")
