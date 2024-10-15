
class Teacher():
    __name = None
    __age = None
    __content = None

    def eat(self):
        print(f"年龄{self.__age}的老师{self.__name}正在吃饭。")
    def speak(self):
        print(f"年龄{self.__age}的老师{self.__name}正在亢奋的讲着{self.__content}。")
    def setter(self,name,age,content):  #获取成员变量，自己传参
        self.__name=name
        self.__age=age
        self.__content=content

    def getter(self):  #调用成员变量
        return self.__age, self.__name, self.__content
teacher=Teacher()
teacher.setter("张三丰","30","python基础中面向对象")
teacher.eat()
teacher.speak()

class Student():
    __name = None
    __age = None
    __content = None
    def eat(self):
        print(f"年龄{self.__age}的{self.__name}同学正在吃饭。")
    def study(self):
        print(f"年龄{self.__age}的{self.__name}正在专心致志的听着{self.__content}的知识。")
    def setter(self,name,age,content):
        self.__name=name
        self.__age=age
        self.content=content
student=Student()
student.setter("张无忌","18","面向对象")
student.study()
student.eat()


