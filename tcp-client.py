from socket import *
import argparse

BUFFER_SIZE = 2048

defaultServerName = "localhost"
defaultServerPort = 12000

def get_destination_addr():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="input for destination ip or hostname", default=defaultServerName)
    parser.add_argument("--port", help="input for destination port", type=int, default=defaultServerPort)
    return parser.parse_args()

destAddr = get_destination_addr()

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((destAddr.host, destAddr.port))
sentence = input("Input lowercase sentence: ")
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(BUFFER_SIZE).decode()
print("Received from server {}:{} ->".format(destAddr.host, destAddr.port), modifiedSentence)

clientSocket.close()