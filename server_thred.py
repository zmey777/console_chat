from socket import *
from threading import Thread
import sys

HOST = '10.10.1.23'
PORT = 9090
BUFSIZE = 1024
ADDR = (HOST, PORT)
users = 5

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(users)

def main():

    print("server running on port 9090 !")
    user = []

    def recive(client_sock, client_addr):

        while True:

            data = client_sock.recv(1024)
            if not data:
                break
            for client in user:
                try:
                    if client != client_sock:
                        client.sendall(data)
                except OSError:
                    pass
        client_sock.close()
        print("Client disconected >> ", client_addr)

    while True:

        client_sock, client_addr = s.accept()
        print("Client connected >> ", client_addr)
        if client_addr not in user:
            user.append(client_sock)

        send = Thread(target=recive, args=(client_sock, client_addr))
        send.setDaemon(True)
        send.start()

if __name__=="__main__":
    main()

