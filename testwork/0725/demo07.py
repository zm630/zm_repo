count=0
sum=0
for a in range(1,101):
    if (a%3==0 and a%5==0):
        sum+=a
        count+=1
print(sum)