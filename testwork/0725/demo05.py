#有1234个数字，能组成多少个互不相同且不重复的数字的三位数
for x in range (1,5):
    for y in range (1,5):
        for z in range (1,5):
            if (x!=y and y!=z and z!=x):
                print(f"{x}{y}{z}")
                
