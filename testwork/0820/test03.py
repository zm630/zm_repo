from abc import ABC,abstractmethod,abstractstaticmethod
class A():
    @abstractmethod
    def showA(self):
        pass

    @staticmethod
    def __show10(str):
        for i in range(0,10):
            print(str+'\t',end="")
        print()

    @staticmethod
    def showB10():
        print("static BBBB")
        A.__show10("BBB")

    @staticmethod
    def showC10():
        print("static CCCC")
        A.__show10("CCC")
class B(A):
    @staticmethod
    def showD():
        print("DDDD")
    def showA(self):
        print("AAAA")


class Test:
    def test_A(self):
        A.showB10()
        A.showC10()


    def test_B(self):
        b=B()
        b.showA()
        B.showD()
test=Test()
test.test_A()
test.test_B()

