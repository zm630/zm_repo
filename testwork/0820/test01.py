from abc import ABC,abstractmethod

class A():
    @abstractmethod
    def showA(self):
        pass
    def showB(self):
        print("BBB")

class B(A):
    def showA(self):
        print("AAA")
b=B()
b.showA()
b.showB()



