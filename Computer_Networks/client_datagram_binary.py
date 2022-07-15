from socket import *
sock = socket(AF_INET, SOCK_DGRAM)
FileName = input("Enter the binary file You want: ")
sock.sendto(bytes(FileName, 'utf-8'), ("127.0.0.1", 5009))
File = open(f"{FileName}.bin", 'wb')
data, addr = sock.recvfrom(1024)
File.write(data)
File.close()
