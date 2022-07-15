from socket import *
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('127.0.0.1', 5009))
a = []
b = []
m = 0
while True:
    data, client = sock.recvfrom(1024)
    filename = data.decode('utf-8')
    print(filename, "request recieved from", str(client))
    a.append(filename)
    b.append(client)
    m += 1
    x = input("Enter Q to stop accepting requests & any alphabet to continue: ")
    if x == "Q":
        for i in range(m):
            File = open(f"{a[i]}.bin", 'rb')
            Data = File.read(1024)
            sock.sendto(Data, b[i])
            print("File sent to ", str(client))
            File.close()
        break

