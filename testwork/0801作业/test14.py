#14.判断五位数中有哪些回文数(回文数比如12321,即个位与万位相同，十位与千位相同)
for i in range(10000,100000):
    ge = i % 10
    shi = i //10 % 10
    qian = i //1000 % 10
    wan = i //10000 % 10
    if ge==wan and shi==qian:
        print(i)