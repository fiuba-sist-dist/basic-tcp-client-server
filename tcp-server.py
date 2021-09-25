from socket import *
import argparse

BUFFER_SIZE = 2048

defaultServerPort = 12000

def get_origin_port():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="input for server port", type=int, default=defaultServerPort)
    return parser.parse_args().port

port = get_origin_port()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", port))
serverSocket.listen(1)
print("Listening connections on port", port)

while (True):
    connectionSocket, clientAddr = serverSocket.accept()
    sentence = connectionSocket.recv(BUFFER_SIZE).decode()
    print("Received from client {}:{} ->".format(clientAddr[0], clientAddr[1]), sentence)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()