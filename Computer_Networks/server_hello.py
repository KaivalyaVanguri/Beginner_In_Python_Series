import socket 
serverPort = 5004
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive a hello')
connectionSocket, x = serverSocket.accept()#, addr
sentence = connectionSocket.recv(2048)
if sentence.decode() == 'hello':
     connectionSocket.send('hello from server side!'.encode())
     connectionSocket.close()
     
