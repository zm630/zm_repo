import random
str=("1","1","2","3","3","32","21")
string=random.choice(str)
def found (string):

#found(string,str)
    print(f"随机选择的字符是: {string}")
    count = str.count(string)
    return count
def main():
    user_input = input("请输入一个字符串: ")
    result=found(string)
    print(f"字符 '{random.choice(str)}' 在字符串中出现了 {result} 次。")
if __name__ == '__main__':
    main()

