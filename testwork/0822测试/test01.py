from abc import ABC,abstractmethod

class Credit():
    @abstractmethod
    def Prepaid(self):
        pass
    def Save(self):
        print("可以存钱")


class Card(Credit):
    name=None
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    @abstractmethod
    def cardholder(self,person):
        pass

class Person:
    def __init__(self,name):
        self.name=name
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

class ICBC(Card):
    def Prepaid(self):
        print("信用卡可以先消费")
    def cardholder(self,person):
        print(f"{person.get_name()}使用的是{self.get_name()}")
class Test():
    def main():
        person = Person('张三')
        bank = ICBC()
        bank.set_name("工商银行信用卡")
        bank.Prepaid()
        bank.Save()
        bank.cardholder(person)

test=Test
test.main()



