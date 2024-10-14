# http://10.20.186.248:6789/HelloWorld.html

#import socket module
from asyncio.base_events import Server
from socket import *
#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP socket
serverPort = 6789
serverSocket.bind(('', serverPort)) # 监听所有可用IP地址的端口
serverSocket.listen(1) # 同时监听最多一个连接请求

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024) # 获取客户发送的报文, 1024是接收的最大字节数
        filename = message.split()[1] # 获取请求的文件名
        '''
        message.split()：将接收到的用户发送的报文按空格分割成一个列表
        
        假设收到的请求信息如下：
        GET /HelloWorld.html HTTP/1.1
        Host: 10.20.186.248:6789
        
        那么处理之后的结果为：
        ['GET', '/HelloWorld.html', 'HTTP/1.1', 'Host:', '10.20.186.248:6789']
        '''
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        pass
        #Send response message for file not found


        #Close client socket

    serverSocket.close()