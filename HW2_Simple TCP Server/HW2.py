import socket
ONE_CONNECTION_ONLY = (True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print('File server started....')
while True:
    clientsocket,address = s.accept()
    print(f'Connection from {address} has been established')
    data = clientsocket.recv(1024)
    print(f'Server received {data}')
    with open ("Hello_World.txt",'rb') as file:
        data = file.read(1024)
        while data:
            clientsocket.send(data)
            print(f'sent {data!r}')
            data = file.read(1024)
    print('File sent successfully')
    clientsocket.close()
    if(ONE_CONNECTION_ONLY):
        break
s.close()