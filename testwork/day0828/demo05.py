#TCP客户端循环版
import socket

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1',18392))
    server_socket.listen(128)
    client_socket,client_ip=server_socket.accept()

    print("客户端",client_ip,data_msg)
    while True:
        data_str=input("客户端说:")
        client_socket.send(data_str.encode(encoding="utf-8"))
        data_btyes = client_socket.recv(1024)
        data_msg = data_btyes.decode(encoding="utf-8")
        print("服务器说:", data_msg)
        # client_socket.close()
