#找出列表 L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88] 中最大值和最小值。
L1 = [1,2,3,11,2,5,3,2,5,33,88]
min=L1[0]
max=L1[0]
for i in L1:
    if (i<min):
        min=i
print(min)

for j in L1:
    if (j>max):
        max=j
print(max)
