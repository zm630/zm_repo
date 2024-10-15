'''
从命令行读入一个字符串，表示一个年份，输出该年的世界杯冠军是哪支球队。如果该年没有举办世界杯，则输出：没有举办世界杯。
'''
dict_data={"1930":"乌拉圭","1934":"意大利","1938":"意大利","1950":"乌拉圭","1954":"西德",
      "1958":"巴西","1962":"巴西","1966":"英格兰","1970":"巴西","1974":"西德",
      "1978":"阿根廷","1982":"意大利","1986":"阿根廷","1990":"西德","1994":"巴西",
      "1998":"法国","2002":"巴西","2006":"意大利","2010":"西班牙","2014":"德国"}
time_data=input("请输入一个年份：")
if time_data in dict_data:
        print(f"{time_data}年的世界杯冠军是：{dict_data[time_data]}")
else:
        print("没有举办世界杯")

def name_data(dict_data):
    winner_data=input("请输入一个球队：")
    years=[]
    for year in dict_data.keys():
        if dict_data[year]==winner_data:
            years.append(year)
    if not years:
        print("没有获得世界杯")
        return years
print(name_data(dict_data))


