import sys
from socket import *



def http_client(server_host, server_port, filename):
    # 创建TCP连接
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_host, int(server_port)))

    # HTTP请求报文
    request = f'GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\nConnection: close\r\n'

    # 发送HTTP请求报文
    clientSocket.send(request.encode())

    # 接收HTTP响应报文
    """
    'responses = clientSocket.recv(4096)'
    如果如上代码不可行，因为服务器是分两段发送，第一段是报文第二段才是文件内容
    那么可以使用如下代码：
    responses = b""
    while True:
        response = clientSocket.recv(1024)
        if not response:
            break
        responses += response
    """
    responses = clientSocket.recv(4096)

    # 解析HTTP响应报文获取内容并输出
    header,_,body = responses.partition(b'\r\n\r\n')
    print(body.decode())



    clientSocket.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = sys.argv[2]
    filename = sys.argv[3]

    http_client(server_host, server_port, filename)