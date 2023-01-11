import socket
import time
import sys
from Start import startDownload
from termcolor import colored

ADDR = "127.0.0.1"
PORT = 22222
ENCODER = 'utf-8'

def startServer():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind((ADDR, PORT))
        server_socket.listen()
        print(colored("\n* Server has started! Waiting for connection with client! \n", "blue"))

        while True:
            conn, addr = server_socket.accept()

            print("\n* Connected with: \n", conn)

            conn.send("\n* You are connected to the server... \n".encode(ENCODER))

            message = conn.recv(1024).decode(ENCODER)

            print(message)

            print(colored("\n* Enter the name of the file that should be made available for download... \n", "yellow"))
            user_input_filename = input("\n* Server: \n")

            f = open(user_input_filename,'rb')
            l = f.read(1024)
            while (l):
                conn.send(l)
                l = f.read(1024)
            f.close()

            print(colored("\n* Done sending! \n","blue"))
    
    except KeyboardInterrupt:
        print(colored("\n Program was terminated by the user! CTRL + C \n", "red"))
        server_socket.close()
    
    except FileNotFoundError:
        print(colored("\n* Enter a valid file name! \n", "red"))

    finally:
        print(colored("\n* Process is finished! \n", "blue"))

if __name__ == '__main__':
    startDownload()
    startServer()
