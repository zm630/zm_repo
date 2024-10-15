#服务器端
import socket

def receive_file(connection,file_path):
    with open(file_path,'w') as file_data:
        while True:
            data = connection.recv(1024)
            file_data.write(data)
if __name__ == '__main__':
    # 1.创建socket对象
    sever_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定端口
    # server_socket.bind(("192.168.2.54",8888))
    sever_socket.bind(("127.0.0.1", 12345))
    # 3.开启监听  128表示最大允许的连接数
    sever_socket.listen(128)
    # 4.获取客户端对象
    client_socket, client_ip = sever_socket.accept()
    print(client_ip, "连接上服务器!!!")
    file_path = input("Enter file path to save: ")
    receive_file(client_socket, file_path)

