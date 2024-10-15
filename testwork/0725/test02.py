gl = int(input("请输入您的工龄："))
jbgz=3000
if(gl>=10 and gl<15):
    zgz=5000
    print(f"您目前工作了{gl}年，基本工资为{jbgz}元，应涨工资{zgz}元，涨后工资{jbgz+zgz}元")
elif(gl>=5 and gl<10):
    zgz=2500
    print(f"您目前工作了{gl}年，基本工资为{jbgz}元，应涨工资{zgz}元，涨后工资{jbgz+zgz}元")
elif(gl>=3 and gl<5):
    zgz=1000
    print(f"您目前工作了{gl}年，基本工资为{jbgz}元，应涨工资{zgz}元，涨后工资{jbgz + zgz}元")
elif(gl>=1 and gl<3):
    zgz=500
    print(f"您目前工作了{gl}年，基本工资为{jbgz}元，应涨工资{zgz}元，涨后工资{jbgz + zgz}元")
elif(gl>=0 and gl<1):
    zgz=200
    print(f"您目前工作了{gl}年，基本工资为{jbgz}元，应涨工资{zgz}元，涨后工资{jbgz + zgz}元")
else:
    print("请输入正确的工龄")