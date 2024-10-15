x=10000
count=0
for y in range(1,9001):
    z=x-y
    z_ge=z%10
    z_shi=z//10%10
    z_bai=z//100%10
    z_qian=z//1000%10
    if (z_ge+z_bai == z_shi+z_qian):
        print(z,"\t",end="")
        count+=1
        if (count%5==0):
            print()
print(f"个数为{count}")