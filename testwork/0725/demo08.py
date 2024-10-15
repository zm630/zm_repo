'''
1x1 1
2x1 3
3x2 9
4x6 33
5x24 153
'''
sum=1
count=0
for i in range(1,6):
        sum=i*sum
        count=count+sum
print(count)