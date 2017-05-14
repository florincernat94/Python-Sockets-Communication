#//CLIENT//

import socket

def Main():
    host = '127.0.0.1'
    port = 5001

    s = socket.socket()
    s.connect((host, port))
    print("SUMA A DOUA NUMERE")
    message = input("Introduceti un numar: ")
    s.send(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Am primit ' + data)
    message = input("Introduceti un numar: ")
    s.send(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Am primit ' + data)
    s.close()

    s = socket.socket()
    s.connect(('127.0.0.2',5002))
    print("PRODUSUL A DOUA NUMERE")
    message = input("Introduceti un numar: ")
    s.send(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Am primit ' + data)
    message = input("Introduceti un numar: ")
    s.send(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Am primit ' + data)
    s.close()


if __name__ == '__main__':
    Main()