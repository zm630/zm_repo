from abc import ABC,abstractmethod
class Universe():
    @abstractmethod
    def doAnything(self):
        pass
    def shine(self):
        print("star:星星一闪一闪亮晶晶")
class Star(Universe):
    def light(self):
        print("sun:光照八分钟，到达地球")

class Sun(Star,Universe):
    def doAnything(self):
        print("sun:太阳吸引着九大行星旋转")
class Test:
    def test_star(self):
        star=Star()
        star.shine()
        print("=================")
    def test_sun(self):
        sun=Sun()
        sun.doAnything()
        sun.light()

test=Test()
test.test_star()
test.test_sun()








