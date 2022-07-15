import socket
host = '127.0.0.1'
port = 5006
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind((host,port))#bind takes only tuple as argument
serversock.listen(10)
print("Server activated \nServer is listening...")
conn, address = serversock.accept()
filename = conn.recv(2048).decode()
print("Request recieved, processing...")
filehandler = open(filename,"r")
s = ""

for i in filehandler:
    s += i

conn.send(filename.encode())
conn.send(s.encode())
conn.close()
