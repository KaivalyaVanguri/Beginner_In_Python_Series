import socket
serverName = socket.gethostname()
serverPort = 5004
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = ''
while sentence != 'hello':
    sentence = input('Say something: ')

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print('From Server:', modifiedSentence.decode())
clientSocket.close()

    
