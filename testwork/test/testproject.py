'''
1.要求开发一个学生管理系统
2.功能要求如下:
   2.1 带有注册功能
   2.2 带有登录功能
   2.3 带有查询学生信息
   2.4 带有增加学生信息
   2.5 带有删除学生信息
   2.6 带有修改学生信息
   2.7.退出系统
'''
import sys

students_list = {"zm": {"password": 12345, "sex": 1, "age": 18},
                 "pyz": {"password": 654321, "sex": 0, "age": 20}}


# 判断用户名是否存在
def isUsername(user_name):
    flag = False
    for name in students_list.keys():
        if (name == user_name):
            flag = True
    return flag



print("欢迎登陆系统")
for i in range(0, 3):
    user_name = input("请输入你的用户名：")
    password = int(input("请输入你的密码："))
    flag = isUsername(user_name)
    if (flag):
        # 判断密码
        pwd = students_list[user_name]['password']
        if (pwd == password):
            while True:
                print("@@请输入您的选择:")
                print("@@选择1进行学生信息查询:")
                print("@@选择2进行学生信息添加:")
                print("@@选择3进行学生信息删除:")
                print("@@选择4进行学生信息修改:")
                print("@@选择5退出学习管理系统:")
                xuanze = int(input("请输入你的选择:"))
                if (xuanze == 1):
                    select_student()
                elif (xuanze == 2):
                    insert_student()
                elif (xuanze == 3):
                    delete_student()
                elif (xuanze == 4):
                    update_student()
                elif (xuanze == 5):
                    exit_student()
                else:
                    print("*沙雕 请正确输入!!!")
        else:
            print("密码错误")
            if i==2:
                print("您的登录次数已使用完毕，请联系管理员!!!")
                sys.exit()
            print("请重新输入你的密码：")
    else:
        print("你输入的用户名不正确")
        if i == 2:
            print("您的登录次数已使用完毕，请联系管理员!!!")
            sys.exit()
        print("请重新输入你的用户名：")
