class Phone():
    def __init__(self,__brand,__price):
        self.brand = __brand
        self.price = __price
    def call(self):
        print("正在使用价格为",self.price,"元的",self.brand,"品牌的手机打电话...")
    def sendMessage(self):
        print("正在使用价格为",self.price,"元的",self.brand,"品牌的手机发短信...")
    def playGame(self):
        print("正在使用价格为",self.price,"元的",self.brand,"品牌的手机打游戏...")

phone1=Phone("小米","998")
phone1.call()
phone1.sendMessage()
phone1.playGame()

print("-------------------------------")

class Phone1():
    __brand = None
    __price = None

    def call(self):
        print(f"正在使用价格为{self.__price}元的{self.__brand}品牌的手机打电话....")

    def sendMessage(self):
        print(f"正在使用价格为{self.__price}元的{self.__brand}品牌的手机发短信....")

    def palyGame(self):
        print(f"正在使用价格为{self.__price}元的{self.__brand}品牌的手机玩游戏....")
    def setter(self,brand,price):
        self.__price=price
        self.__brand=brand
phone2=Phone1()
phone2.setter("小米","998")
phone2.call()
phone2.sendMessage()
phone2.palyGame()



