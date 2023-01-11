import socket
import time
import sys
from termcolor import colored

ADDR = "127.0.0.1"
PORT = 22222
ENCODER = 'utf-8'

def startClient():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ADDR, PORT))
    print(colored("\n* Connection established! \n", "blue"))

    try:
        while True:
            message = client_socket.recv(1024).decode(ENCODER)

            print(message)

            client_socket.send("\n You are connected to the client... \n".encode(ENCODER))

            print(colored("\n* Enter the file name to be downloaded... \n", "yellow"))
            user_input_filename = input("\n* Client: \n")

            with open(user_input_filename, 'wb') as f:
                print(colored("\n* File opened... \n", "blue"))
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    f.write(data)
            f.close()
            print(colored("\n* Successfully get the file! \n", "blue"))
            client_socket.close()

    except KeyboardInterrupt:
        print(colored("\n* Program end! \n", "red"))
        client_socket.close()
    
    except ConnectionRefusedError:
        print(colored("\n* Server has not started make sure the server is running... \n", "red"))

if __name__ == '__main__':
    startClient()