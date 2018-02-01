from socket import *
from threading import Thread
import sys

HOST = '10.10.1.23'
PORT = 9090
BUFSIZE = 1024
ADDR = (HOST, PORT)

def main():

    def recv():
        while True:
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                sys.exit(0)
            print ("\n","from > ",data.decode("utf-8"))

    def send():
        T = True
        while T:
            data = input('>> ')
            if data == "exit":
                break
            if not data:
                break
            tcpCliSock.send(data.encode())
        tcpCliSock.close()
        sys.exit(0)

    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)

        recive = Thread(target=recv)
        recive.setDaemon(True)
        recive.start()
        send()
    except:
        print("server not response !!!")

if __name__=="__main__":
    main()