from socket import *
import os
import threading

#Setting up a socket to listen for incoming connections on port 1200.
portNumber = 1200
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', portNumber))
serverSocket.listen(1)
print('server is ready to listen')

#Function that handles an incoming client connection.
# It receives a file name from the client and
# creates source and destination paths for the file.

def handleClient(clientSocket, addr):
    fileName = clientSocket.recv(1024).decode()
    print('received filename:', fileName)

    source_path = os.path.join('c:/temp', fileName)
    destination_path = os.path.join('c:/temprecieve', fileName)


#Opens the source file for reading and the destination file for writing.
    # Then, it reads the source file in 1024-byte chunks and sends each chunk to the client
    # and writes it to the destination file.
    with open(source_path, 'rb') as source_file, open(destination_path, 'wb') as destination_file:
        file_data = source_file.read(1024)
        while file_data:
            print('sending...')
            clientSocket.send(file_data)
            destination_file.write(file_data)
            file_data = source_file.read(1024)

    print('Done sending')
    clientSocket.close()

#Continuously listens for incoming connections
# and creates a new thread to handle each connection.
while True:
    print('waiting for connection...')
    clientSocket, clientAddress = serverSocket.accept()
    print('Accepted connection from', clientAddress)

    client_thread = threading.Thread(target=handleClient, args=(clientSocket,clientAddress))
    client_thread.start()


