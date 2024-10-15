def menu():
    print("欢迎来到学生管理系统")
def main():
    while True:
        menu()  #调用菜单函数
        choice=int(input("请选择："))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
               answer=input("确定退出系统吗y/n:")
               if answer=="y" or answer=="Y":
                   print("谢谢你的使用")
                   break   #退出
               else:
                   continue   #退出本次循环，重新选择
            elif choice==1:
                add()
            elif choice==2:
                chazhao()
            elif choice==3:
                delete()
            elif choice==4:
                xiugai()
            elif choice==5:
                total()
            elif choice==6:
                sort()
            elif choice==7:
                show()

main()
