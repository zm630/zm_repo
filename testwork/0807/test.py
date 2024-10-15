import json


def isUsername(user_name):
    flag = False
    with open("students_list.json","r",encoding="utf-8") as file:
        students_list=file.readlines()
        for name in students_list:
            if user_name in name:
                flag = True
        return flag

import json
with open("students_list.json","r",encoding="utf-8") as file:
    students_list=file.read()
#判断用户名是否存在
print("欢迎登陆系统")
user_name = input("请输入你的用户名：")
password = int(input("请输入你的密码："))
flag = isUsername(user_name)
if (flag):
    #判断密码
    pwd=students_list[user_name]['password']
    if pwd == password:
        print("可以进入系统")
    else:
        print("密码错误")
else:
    print("你输入的用户名不正确")