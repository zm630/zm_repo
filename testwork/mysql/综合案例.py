from testwork.mysql.Order import Order
from pymysql import Connection
#1.读取数据
with open ("2011年1月销售数据.txt","r",encoding="utf-8") as file:
    data_list = file.readlines()
# print(data_list)
#['2011-01-01,4b34218c-9f37-4e66-b33e-327ecd5fb897,1689,湖南省\n',
# '2011-01-01,5b6a6417-9a16-4243-9704-255719074bff,2353,河北省\n', ...]

#连接MySQL
conn = Connection(
    user = 'root',
    password = 'root',
    host = '127.0.0.1',
    port = 3306,
    database = 'homework',
    autocommit = True
)
#获取游标
cursor = conn.cursor()

#1.插入数据
def insert_orders():
    # 2.清洗数据并插入数据库
    # 创建一个类Order，将每一个数据都封装成一个对象，再将对象的值插入到数据库里面
    for data in data_list:
        data_str_list = data.split(",")
        # print(data_str_list)
        # ['2011-01-01', '4b34218c-9f37-4e66-b33e-327ecd5fb897', '1689', '湖南省\n']
        # ['2011-01-01', '5b6a6417-9a16-4243-9704-255719074bff', '2353', '河北省\n']
        order = Order(data_str_list[1], data_str_list[0], data_str_list[2], data_str_list[3])
        sql = f"insert into orders(order_id,order_date,order_money,order_province) values ('{order.id}','{order.date}',{order.money},'{order.province}');"
        cursor.execute(sql)
    # 3.关闭连接
    conn.close()
# insert_orders()

#2.查询所有数据
def select_all_orders():
    sql = "select * from orders"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
# select_all_orders()

#3.单个条件查询
def selectBycondition1_orders(order:Order):
    sql = "select * from orders"
    if (order.id != None):
        sql += f" where order_id='{order.id}'"
    if (order.date != None):
        sql += f" where order_date='{order.date}'"
    if (order.money != None):
        sql += f" where order_money={order.money}"
    if (order.province != None):
        sql += f" where order_province='{order.province}'"
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
# order = Order(None,None,None,'四川省\n')
# selectBycondition1_orders(order)

#4.多个条件查询
def selectBycondition2_orders(order:Order):
    sql = "select * from orders where 1=1 " #恒等式欺骗MySQL，便于我们连接语句
    if (order.id != None):
        sql += f" and order_id='{order.id}'"
    if (order.date != None):
        sql += f" and order_date='{order.date}'"
    if (order.money != None):
        sql += f" and order_money={order.money}"
    if (order.province != None):
        sql += f" and order_province='{order.province}'"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
# order = Order(None,'2011-01-01',None,'四川省\n')
# selectBycondition2_orders(order)

#5.删除数据
def delete_orders(order:Order):
    sql = "delete from orders where 1=1"
    if (order.id != None):
        sql += f" and order_id='{order.id}'"
    if (order.date != None):
        sql += f" and order_date='{order.date}'"
    if (order.money != None):
        sql += f" and order_money={order.money}"
    if (order.province != None):
        sql += f" and order_province='{order.province}'"
    print(sql)
    cursor.execute(sql)

#6.根据id修改数据
def update_orders(order:Order):
    sql = "update orders "
    if (order.date != None):
        sql += f" set order_date='{order.date}' "
    if (order.money != None):
        if ("set" in sql):
            sql += f" , order_money={order.money} "
        else:
            sql += f" set order_money={order.money} "
    if (order.province != None):
        if ("set" in sql):
            sql += f" , order_province={order.province} "
        else:
            sql += f" set order_province={order.province} "
    sql += f" where order_id = '{order.id}';"
    print(sql)
    cursor.execute(sql)
# order = Order('4b34218c-9f37-4e66-b33e-327ecd5fb897',None,1111,None)
# update_orders(order)


