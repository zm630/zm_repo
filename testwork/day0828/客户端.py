import socket
def send_file(file_path,host="127.0.0.1",port=12345):
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))
    sock = socket.socket()
    with open (file_path,"rb") as file:
        while True:
            data = file.read(1024)
            sock.sendall(data)
    print("File sent successfully")

if __name__ == '__main__':
    file_path = input("输入你想传输的文件名: ")
    send_file(file_path)


# import socket
# def send_file(file_path, host='127.0.0.1', port=12345):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((host, port))
#
#         with open(file_path, 'rb') as f:
#             while True:
#                 data = f.read(1024)
#                 if not data:
#                     break
#                 sock.sendall(data)
#
#         print("File sent successfully")
#
#
# if __name__ == "__main__":
#     file_path = input("Enter file path to send: ")
#     send_file(file_path)