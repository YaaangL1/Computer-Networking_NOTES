# http://10.20.186.248:6789/HelloWorld.html
# http://10.16.60.43:6789/HelloWorld.html
# import socket module
import threading
from socket import *


# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
serverPort = 6789
serverSocket.bind(('', serverPort))  # 监听所有可用IP地址的端口
serverSocket.listen()  # 同时监听最少一个连接请求

def handle_server(connectionSocket):
    try:
        message = connectionSocket.recv(1024)  # 获取客户发送的报文, 1024是接收的最大字节数
        filename = message.split()[1]  # 获取请求的文件名
        resourceFolder = "resource"
        path = resourceFolder.encode() + filename

        f = open(path)
        outputdata = f.read()

        # Send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (
            len(outputdata))
        connectionSocket.send(header.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        header = 'HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())
        # Close client socket
        connectionSocket.close()


while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    clientThread = threading.Thread(target=handle_server, args=(connectionSocket,))
    clientThread.start()
