class Phone():
    # 定义了成员变量
    brand = None
    price = None
    color = None
    size = None

    # 定义成员方法
    def sendMsg(self,name):
        print(f"给{name}发短信....")

    def call(self,name):
        print(f"给{name}打电话...")

phone1 = Phone()
print(phone1)
print(phone1.brand)
phone1.brand = '华为'
print(phone1.brand)
phone1.sendMsg('张三')
# phone1.call('李四')
print("---------------------------->")
phone2 = Phone()
print(phone2)
phone2 = phone1
print(phone2)
print(phone2.brand)
phone2.brand = '三星'
print(phone2.brand)
print(phone1.brand)
phone2.sendMsg('王五')
# phone2.call('赵六')
print(phone1 == phone2)

class Dog():
    color = None
    brand = None
    name = None
#构造方法
    # def __init__(self):
    #     print("Dog类的无参构造执行了..")

    # 有参数的构造方法
    # def __init__(self,name):
    #     print("Dog类的有参构造执行了..")
    #     self.name = name
# 满参数的构造方法
#     def __init__(self,color,brand,name):
#         print("Dog类的有参构造执行了..")
#         self.name = name
#         self.color = color
#         self.brand = brand
    def eat(self):
        # 局部变量

        # 如何才能使用成员变量
        # 就近原则
        print(self) # <__main__.Dog object at 0x000001714F52EF28>  or <__main__.Dog object at 0x000001BE65FC6080>
        print("正在啃骨头...")
# dog1 = Dog("红色","哈士奇","张二狗")
dog1=Dog()
dog1.eat()
# print("有一只",dog1.color,"的",dog1.brand,"名字叫",dog1.name)
name = "张三"

class Student():
    name = None

stu = Student()
stu.name = "李四"
print(stu.name)