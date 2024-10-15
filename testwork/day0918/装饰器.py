# 注意与包的区别：装饰器实质上是一个闭包函数，但是装饰器这个闭包函数。
# 他的参数有且只有一个并且是函数类型的话，他才是装饰器，否则他就是闭包函数！
def check(func):
    def inner():
        print("??")
        func()
        print("!!")
    return inner
def func():
    print("xzq!!!")
inner = check(func)
inner()