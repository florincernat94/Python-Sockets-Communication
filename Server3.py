import socket

def Main():
    host = '127.0.0.3'
    port = 5003

    s = socket.socket()
    s.bind((host,port))

    s.listen(2)
    c, addr = s.accept()
    c2, addr2 = s.accept()
    print("Connection from: " + str(addr))
    print("Connection from: " + str(addr2))

    while True:
        data = c.recv(1024).decode('utf-8')
        data2 = c2.recv(1024).decode('utf-8')
        if not data:
            break
        print("Rezultatul sumei este: " + data)
        print("Rezultatul produsului este: " + data2)
    c.close()

if __name__ == '__main__':
    Main()
