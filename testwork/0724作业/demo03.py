grade = int(input("请输入你的百米赛跑成绩："))
if(grade<10):
    print("恭喜你进入决赛！")
    sex = input("请输入你的性别：")
    if(sex=="男"):
        print("请加入男子组")
    if(sex=="女"):
        print("请加入女子组")
else:
    print("你不能参加决赛！")
