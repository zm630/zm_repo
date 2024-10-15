import random
score_list = []
for i in range(1,7):
    score = random.randint(0,101)
    score_list.append(score)
print(score_list)
#求最大值
max = score_list[0]
for i in range(1,len(score_list)):
    if max<score_list[i]:
        max=score_list[i]
