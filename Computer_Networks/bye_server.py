import socket

def server_program():
    host = socket.gethostname()
    port = 5003  
    server_socket = socket.socket()  
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if data == 'bye':#not data
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()
    
server_program()
