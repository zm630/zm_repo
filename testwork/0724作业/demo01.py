num = int(input("请输入一个1-5的数字："))
import sys   #导入函数
if (num==1) :
    print("新建")
elif(num==2):
    print("打开文件")
elif(num==3):
    print("保存")
elif(num==4):
    print("刷新")
elif(num==5):
    print("退出")
else:
    sys.exit()

