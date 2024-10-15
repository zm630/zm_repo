from abc import ABC,abstractmethod

class A():
    @abstractmethod
    def showA(self):
        pass
    def __show10(self,str):
        count=1
        while count<=10:
            print(str+'\t',end="")
            count+=1
        print()
    def showB10(self):
        self.__show10("BBB")
    def showC10(self):
        self.__show10("CCC")
class B(A):
    def showA(self):
        print("AAA")

b=B()
b.showA()
b.showB10()
b.showC10()
