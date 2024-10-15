user_name = "程序员"
user_type = "SSSSSVIP用户"
print('您好:' +user_name,'您是尊贵的：'+user_type, '，欢迎您的光临。')

print("--------------------------------->")

name = "阿里妈妈"
stock_code="003032"
stock_price =19.99
stock_price_daily_growth_factor=1.2
growth_days=7
price=stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司：{name},股票代码：{stock_code},当前股价,{stock_price}")
print("每日的增长系数：%.1f，经过 %d 天的增长后，股价达到了 %.2f" %(stock_price_daily_growth_factor,growth_days,price))
print("--------------------------------->")

age = 18
score=98
sex = "男"
print("我的年龄："+str(age))
print("我的成绩："+str(score))
print("我的性别:"+sex)
print("--------------------------------->")


print(f"我的年龄：{age}\n我的成绩：{score}\n我的性别：{sex}")

print("--------------------------------->")

print("我的年龄：%d\n我的成绩：%d\n我的性别：%s" %(age,score,sex))

