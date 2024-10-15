from abc import ABC,abstractmethod

class Bluetooth():
    @abstractmethod
    def btFunction(self):
        pass
    def connecting(self):
        print("可以连接蓝牙")


class Phone(Bluetooth):
    # name=None

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def playMusic(self,song):
        pass

class Song:
    def __init__(self,singer,name):
        self.name=name
        self.singer=singer
    def set_name(self,name):
        self.name = name
    def set_singer(self,singer):
        self.singer = singer
    def get_name(self):
        return self.name
    def get_singer(self):
        return self.singer

class IPhone(Phone):
    def btFunction(self):
        print("支持蓝牙功能")
    def playMusic(self,song):
        print(f"{self.get_name()}手机播放的是{song.get_name()}唱的{song.get_singer()}")
class Test1:
    def main():
        song = Song('于文文','体面')
        iphone = IPhone()
        iphone.set_name("iphone8")
        iphone.btFunction()
        iphone.connecting()
        iphone.playMusic(song)
test1=Test1
test1.main()

