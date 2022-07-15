import socket
host = '127.0.0.1'
port = 5005
#the bind function takes tuple as argument
server_socket = socket.socket()
server_socket.bind((host,port))
#configures how many clients the server can listen simultaneously
server_socket.listen(5)
print("Server is listening ")
#accepts new connection
conn, address = server_socket.accept()
filename = conn.recv(2048).decode()
print("Request recieved, processing...")
filehandler = open(filename,"r")
for i in filehandler:
    #recieves the data stream
    #it wont accept data packets greater than 2048 bytes
    print(i)
conn.send(filename.encode())
conn.close()
