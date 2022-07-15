from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 5006))
FileName = input("Enter the binary file you want: ")
s.send(bytes(FileName, 'utf-8'))

x = s.recv(1024).decode()
if x == "File Not Found":
    print("File Not Found")
else:
    File = open(f'{FileName}.bin', "wb")
    File.write(x.encode())
    File.close()
    print(x)

s.close()
    
