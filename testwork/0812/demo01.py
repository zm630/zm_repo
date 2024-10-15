name_data=[{"姓名":"师父","员工编号":"1001","部门编号":"9002","工资":60000},
           {"姓名":"孙悟空","员工编号":"1002","部门编号":"9001","工资":50000},
           {"姓名":"猪八戒","员工编号":"1003","部门编号":"9002","工资":20000},
           {"姓名":"沙僧","员工编号":"1004","部门编号":"9001","工资":30000},
           {"姓名":"小白龙","员工编号":"1005","部门编号":"9001","工资":15000}]
def print_data(name_data):
    for data in name_data:
        xm=data["姓名"]
        bh=data["员工编号"]
        bmbh=data["部门编号"]
        gz=data["工资"]
        print(f"{xm}的员工编号是{bh},部门编号是{bmbh},月薪{gz}元")
#print_data(name_data)

def bm_data(name_data):
    for data in name_data:
        xm = data["姓名"]
        bmbh = data["部门编号"]
        if bmbh=="9002":
           print(xm)
#bm_data(name_data)

def min_data(name_data):
    return min(name_data,key=lambda x:x["工资"])
print("薪资最低的员工:", min_data(name_data))


def sort_data(name_data):
    return sorted(name_data, key=lambda x: x['工资'])
print(sort_data(name_data))



def remove_data(name_data):
    for emp in name_data:
        if len(emp['姓名']) != 3:
            print(emp)
print(remove_data(name_data))
