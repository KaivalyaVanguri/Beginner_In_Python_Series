from socket import *
s = socket(AF_INET, SOCK_STREAM)
print("Socket successfully created")
port = 5007
s.bind(('127.0.0.1', port))

while True:
    s.listen(10)#listening to 10 clients simultaneously
    print("server is listening")
    c, ClientName = s.accept()
    RecvMsg = c.recv(1024).decode()
    print(f"{ClientName} is requesting for: ", RecvMsg)
    f_name = f'{RecvMsg}.txt' #f-strings
    try:
        f = open(f_name, "r")
        Data = f.read()
        f.close()
        c.send(bytes(Data, 'utf-8'))

    except IOError:#try-except block
        print("Requested File Not found")
        c.send(bytes('File Not Found', 'utf-8'))
    
