# TCP服务器端入门程序

import socket

if __name__ == '__main__':
    # 1.创建socket对象
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定端口
    server_socket.bind(("127.0.0.1",8888))
    # 3.开启监听  128表示最大允许的连接数
    server_socket.listen(128)
    # 4.获取客户端对象
    client_socket,client_ip=server_socket.accept()
    # 5.获取客户端发送的消息
    data_btyes=client_socket.recv(1024)
    data_msg=data_btyes.decode(encoding="utf-8")
    print("客户端",client_ip,data_msg)
    # 6.发送数据给客户端
    client_socket.send("滚吧!!!".encode(encoding="utf-8"))
    client_socket.close()