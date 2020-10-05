import socket
TCP_IP = '94.142.241.111'
TCP_PORT = 23
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((TCP_IP, TCP_PORT))
while True:
    data = c.recv(1024)
    stringdata = data.decode('utf-8')
    print(stringdata)
