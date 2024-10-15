import socket

if __name__ == '__main__':
    #1.创建客户端对象
    # socket.AF_INET 表示ipv4 , socket.SOCK_STREAM 表示采用TCP协议  ， SOCK_DGRAM 表示UDP协议
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 127.0.0.1 or localhost都表示本机ip
    client_socket.connect(("192.168.31.248",8888))

    print("客户端成功连接服务器!!!")
    while(True):
        data_str = input("客户端说:")
        # 2.发送数据
        client_socket.send(data_str.encode(encoding="utf-8"))
        #3.接收数据
        # 1024 表示我一次性可以读取多少个字节
        data_bytes = client_socket.recv(1024)
        data_msg = data_bytes.decode(encoding="utf-8")
        print("服务器说:",data_msg)
        #4.关闭连接
        # client_socket.close()
