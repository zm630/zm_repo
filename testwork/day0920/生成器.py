def sum_num(n):
    a,b=0,1
    count=0
    while count<n :
        yield a
        a,b=b,a+b
        count+=1
sub=sum_num(21)
for i in sub:
    print(i)
# def sib(n):
#     for i in range(n):
#         print("开始")
#         yield i
#         print("结束")
# sub = sib(5)
# for d in sub:
#     print(d)
