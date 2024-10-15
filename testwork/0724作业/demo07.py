#建立一个集合装入学生成绩
scores = []
count=0
while True:
    grade = int(input("输入学生成绩(输入-1结束)："))
    scores.append(grade)
    count+=1
    if (grade==-1):
      break
print("平均值为：",sum(scores)/count)