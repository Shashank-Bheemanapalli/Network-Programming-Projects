import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 1234))
c.send(b"Hello from client")
with open("ASCII_ART.txt",'wb') as file:
    print("file open")
    print("receiving data...")
    while True:
        data = c.recv(1024)
        print(f'data={data}')
        if not data:
            break
        file.write(data)
print('Received the file')
with open("ASCII_ART.txt",'r') as f:
    art = f.read()
    print(art)
c.close()
print("Connection is closed")

