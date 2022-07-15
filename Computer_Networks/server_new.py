import socket
p_name = 5005
conn, addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.listen(1)
socket.bind(conn,addr)
conn.recv(1024)
conn.send("kaivalya".encode())
socket.close()
print(
