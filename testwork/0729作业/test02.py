"""
4. 需求：
  (1)定义一个int类型的一维数组，内容为{171,72,19,16,118,51,210,7,18}
  (2)求出该数组中满足要求的元素和。
 		要求：求和的元素的个位和十位不能包含7,并且只能为偶数。

 if(arr[i]  % 10  != 7  && arr[i]  / 10 % 10 != 7  && arr[i] % 2 == 0 )

"""
data_list = [171,72,19,16,118,51,210,7,18]
index=0
sum=0
for i in data_list:
    if (i % 10 != 7 and i // 10 % 10 != 7 and i % 2 == 0):
        sum += i
        index += 1
print(sum)