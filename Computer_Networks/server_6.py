from socket import *
s = socket(AF_INET, SOCK_STREAM)
print("Socket successfully created")
port = 5006
s.bind(('127.0.0.1', port))

while True:
    s.listen(5)
    print("socket is listening")
    c, ClientName = s.accept()
    RecvMsg = c.recv(1024).decode()
    print(f"{ClientName} is requesting for: ", RecvMsg)
    f_name = f'{RecvMsg}.bin'
    try:
        f = open(f_name, "rb")
        Data = f.read().decode()
        f.close()
        c.send(bytes(Data, 'utf-8'))
        print("Requested File found")

    except IOError:
        print("Requested File Not found")
        c.send(bytes('File Not Found', 'utf-8'))

    c.close()


    

