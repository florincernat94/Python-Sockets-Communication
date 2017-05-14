import socket
result=int
def Main():
    host = '127.0.0.1'
    port = 5001

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    result=0
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("from connected user: " + data)
        print("sending: " + data)
        c.send(data.encode('utf-8'))
        result=result+int(data)
    c.close()
    s = socket.socket()
    s.connect(('127.0.0.3',5003))
    print(result)
    s.send(str(result).encode('utf-8'))
if __name__ == '__main__':
    Main()
