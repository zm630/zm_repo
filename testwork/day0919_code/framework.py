import json
import time
import pymysql
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

#装饰器的方式添加路由
router_list = []
### debug 其实就是观察代码的执行流程
### 1，打断点 哪里不会打哪里 或者想看哪里打哪里
### 2.进行调试

def router(path):
    def decorator(func):
        router_list.append((path,func))
        def inner():
            func()
        return inner
    return decorator

### 客户端一次请求对应一个函数
@router("/center.html")
def center():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "PWS2.0")]
    with open("template/center.html","r",encoding="utf-8") as file:
        file_data = file.read()
    # 处理后的数据
    # 这里的数据实际上将应该是从数据库查询得到的
    result = file_data.replace("{%content%}","")
    return status, response_header, result

@router("/center_data.html")
def center():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "PWS2.0"), ("Content-Type", "application/json")]
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="root",
                           database="demodb",
                           charset="utf8")

    # 获取游标
    cursor = conn.cursor()
    # 查询sql语句
    sql = '''SELECT i.code, i.desc, i.price, 
             i.turnover_rate, i.new_price, i.prev_hight, f.note_info 
             FROM info AS i INNER JOIN focus AS f ON i.id = f.info_id;'''
    # 执行sql
    cursor.execute(sql)
    # 获取结果集
    result = cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()
    center_data_list = list()
    # 遍历每一行数据转成字典
    for row in result:
        # 创建空的字典
        center_dict = dict()
        center_dict["code"] = row[0]
        center_dict["desc"] = row[1]
        center_dict["price"] = row[2]
        center_dict["turnover_rate"] = row[3]
        center_dict["new_price"] = str(row[4])
        center_dict["prev_hight"] = str(row[5])
        center_dict["note_info"] = row[6]
        # 添加每个字典信息
        center_data_list.append(center_dict)
    data_json = json.dumps(center_data_list)
    return status, response_header, data_json

@router("/index.html")
def index():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "PWS2.0")]
    with open("template/index.html", "r",encoding="utf-8") as file:
        file_data = file.read()
    # 处理后的数据
    # 这里的数据实际上将应该是从数据库查询得到的
    # data = time.ctime()
    # 处理后的数据, 从数据库查询
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="root",
                           database="demodb",
                           charset="utf8")
    # 获取游标
    cursor = conn.cursor()
    # 查询sql语句
    sql = "select * from info;"
    # 执行sql
    cursor.execute(sql)
    # 获取结果集
    result = cursor.fetchall()
    response_body = ""
    for data in result:
        response_body += " <tr>" \
                         f"<td>{data[0]}</td>" \
                         f"<td>{data[1]}</td>" \
                         f"<td>{data[2]}</td>" \
                         f"<td>{data[3]}</td>" \
                         f"<td>{data[4]}</td>" \
                         f"<td>{data[5]}</td>" \
                         f"<td>{data[6]}</td>" \
                         f"<td>{data[7]}</td>" \
                         f"<td>{data[8]}</td>" \
                         "<td><input type='button' value='添加' id='toAdd' name='toAdd' systemidvaule='000007'></td>" \
                         "</tr>"
        response_body += "\r\n"
    # date = time.ctime()
    response_body = file_data.replace("{%content%}",response_body)
    return status, response_header, response_body

def not_found():
    # 响应状态
    status = "404 OK";
    # 响应头
    response_header = [("Server", "PWS2.0")]
    # 处理后的数据
    data = "not found"
    logging.error("发生了错误...")
    return status, response_header, data

### 路由列表
# router_list = [
#     ("/index.html",index),
#     ("/center.html",center)
# ]

def handle_request(env):
    request_path = env['request_path']
    # if(request_path == "/index.html"):
    #     result = index()
    #     return result
    # if(request_path == "/center.html"):
    #     result = center()
    #     return result
    for path,func in router_list:
        if(request_path == path):
            logging.info("路由"+request_path+"执行了...")
            return func()

    result = not_found()
    return result

