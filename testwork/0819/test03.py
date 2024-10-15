class Cat():
    __color = None
    __brand = None

    def eat(self):
        print(f"{self.__color}的{self.__brand}正在吃鱼")
    def catchMouse(self):
        print(f"{self.__color}的{self.__brand}正在抓老鼠")
    def setter(self,color,brand):
        self.__color=color
        self.__brand=brand


class Dog():
    __color = None
    __brand = None
    def eat(self):
        print(self.__color,"的",self.__brand,"正在啃骨头")
    def lookHome(self):
        print(self.__color,"的",self.__brand,"正在看家")
    def setter(self,color,brand):
        self.__color=color
        self.__brand=brand


cat=Cat()
cat.setter("花色","波斯猫")
cat.eat()
cat.catchMouse()
dog=Dog()
dog.setter("黑色","藏獒")
dog.eat()
dog.lookHome()
print("-------------------------->")

class Cat1():
    def __init__(self,__color,__brand):
        self.brand = __brand
        self.color = __color
    def eat1(self):
        print(self.color,"的",self.brand,"正在吃鱼")
    def catchMouse1(self):
        print(self.color, "的", self.brand, "正在逮老鼠")
    def main(self):
        Cat1.eat1(self)
        Cat1.catchMouse1(self)
cat1=Cat1("花色","波斯猫")
cat1.main()
print("-------------------------->")

class Cat():
    __color = None
    __brand = None

    def eat(self):
        print(f"{self.__color}的{self.__brand}正在吃鱼")
    def catchMouse(self):
        print(f"{self.__color}的{self.__brand}正在抓老鼠")
    def setter(self,color,brand):
        self.__color=color
        self.__brand=brand
    def main(self):
        Cat.eat(self)
        Cat.catchMouse(self)

cat1=Cat()
cat1.setter("花色","波斯猫")
cat1.main()