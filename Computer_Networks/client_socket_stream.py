import socket
serverName = '127.0.0.1'
serverPort = 5005
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('request a file: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print ('From Server:', modifiedSentence)
clientSocket.close()
