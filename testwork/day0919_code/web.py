"""
  开发web服务器
"""
import socket
import threading
import sys
import framework
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
"""
 请求的情况说明
   /index.html 
     要么框架能够找到对应的函数处理请求
     要么框架找不到对应的函数处理请求 走 not_fond函数
   /findAll 
     这样的请求可能处理不了 则响应error.html
   /5.jpg or jquery.js or index.css 
    这样的情况直接去static目录下读取资源进行响应


"""
# 定义web服务器类
class HttpWebServer(object):
    def __init__(self, port):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用, 程序退出端口立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    # 处理客户的请求
    def handle_client_quest(self,new_socket):
        # 代码执行到此，说明连接建立成功
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            print("关闭浏览器了")
            # 关闭服务与客户端的套接字
            new_socket.close()
            return
        # 对二进制数据进行解码
        recv_client_content = recv_client_data.decode("utf-8")
        # print(recv_client_content)
        request_list = recv_client_content.split(" ",maxsplit=2)
        # print(request_list)
        request_path = request_list[1]

        logging.info("用户访问的日志为:" + request_path)

        if(request_path == "/"):
            request_path = "/oldindex.html"
        ### 判断请求的资源是动态资源还是静态资源
        if(request_path.endswith(".html")):
        # if(".html" not in request_path):
            #### 动态资源 将来需要交给我们框架来进行处理
            #### 字典
            env = {
                "request_path":request_path
            }
            status,headers,data = framework.handle_request(env)
            response_line = "HTTP/1.1 %s OK\r\n" % status
            response_header = ""
            for header in headers:
                response_header += "%s: %s\r\n" %header
            response_body = data
            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")
            # 发送数据
            new_socket.send(response_data)
            ### 响应行 响应头 响应空行 响应体

        else:
            #### 这里是静态资源请求 请求的是js  图片 css
            try:
                # 动态打开指定文件
                with open("static" + request_path, "rb") as file:
                    # 读取文件数据
                    file_data = file.read()
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 响应头
                response_header = "Server: PWS1.0\r\n"

                # 响应体
                response_body = file_data

                # 拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                # 发送数据
                new_socket.send(response_data)
            except Exception as e:
                # 请求资源不存在，返回404数据
                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 响应头
                response_header = "Server: PWS1.0\r\n"
                with open("static/error.html", "rb") as file:
                    file_data = file.read()
                # 响应体
                response_body = file_data

                # 拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                # 发送数据
                new_socket.send(response_data)
            finally:
                # 关闭服务与客户端的套接字
                new_socket.close()
    def start(self):
        while True:
            # 等待接受客户端的连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target=self.handle_client_quest,args=(new_socket,))
            # 设置守护线程
            # sub_thread.setDaemon(True)
            sub_thread.start()


# 程序入口函数
def main():

    # #获取命令行参数判断长度
    # if len(sys.argv) != 2:
    #     print("执行命令如下: python3 xxx.py 9000")
    #     return
    #
    # # 判断端口号是否是数字
    # if not sys.argv[1].isdigit():
    #     print("执行命令如下: python3 xxx.py 9000")
    #     return
    #
    # # 需要转成int类型
    # port = int(sys.argv[1])
    port = 9999
    # 创建web服务器
    web_server = HttpWebServer(port)
    # 启动web服务器
    web_server.start()

if __name__ == '__main__':
    main()