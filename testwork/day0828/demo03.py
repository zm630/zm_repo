#TCP客户端入门程序
# TCP通信步骤  1.创建连接 2.传输数据 3.关闭连接

import socket

if __name__ == '__main__':
    ##1.创建客户端对象
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1",8888))
    # 2.发送数据
    client_socket.send("hallo".encode(encoding="utf-8"))
    #3.接收数据
    data_bytes = client_socket.recv(1024)
    data_msg = data_bytes.decode(encoding='utf-8')
    print("服务器说:",data_msg)
    # 4.关闭连接
    client_socket.close()