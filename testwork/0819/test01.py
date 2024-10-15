class Manager:
    def __init__(self,__name,__id,__salary,__bonus):   #私有变量
        self.name=__name
        self.id=__id
        self.salary=__salary
        self.bonus=__bonus
    def work(self):  #私有方法
        print("工号为",self.id,"基本工资为",self.salary,"奖金为",self.bonus,"的",self.name,"正在努力的做着管理工作,分配任务,检查员工提交上来的代码.....")

class Coder:
    def __init__(self,__name,__id,__salary):
        self.name=__name
        self.id=__id
        self.salary=__salary
    def work(self):
        print("工号为",self.id,"基本工资为",self.salary,"的",self.name,"正在努力的写着代码.....")

manager=Manager("项目经理","123","15000","6000")
manager.work()
print("----------------->")

coder=Coder("程序员","135","10000")
coder.work()
print("----------------->")

class Manager1:
    __name=None
    __id = None
    __salary = None
    __bonus = None
    def work(self):
        print("工号为",self.__id,"基本工资为",self.__salary,"奖金为",self.__bonus,"的",self.__name,"正在努力的做着管理工作,分配任务,检查员工提交上来的代码.....")
    def setter(self,name,id,salary,bonus):
        self.__name=name
        self.__id=id
        self.__bonus=bonus
        self.__salary=salary
    def getter(self):
        return self.__name,self.__id, self.__bonus,self.__salary
manager1=Manager1()
manager1.setter("项目经理","123","15000","6000")
manager1.getter()
manager1.work()
