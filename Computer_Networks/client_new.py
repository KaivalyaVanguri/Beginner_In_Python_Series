import socket
s_name = '127.0.0.1'
p_name = 5005
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((client,p_name))
client.recv(1024)
print(client)
client.close()
