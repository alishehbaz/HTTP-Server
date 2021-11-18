from socket import *
import sys  # In order to terminate the program


def webServer(port=6789):


    # Prepare a server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)  


    #  assigns an IP address and a port number to the socket
    serverSocket.bind(('localhost', port))

    # set a queue size
    serverSocket.listen(1)


    while True:


        # Establish the connection
        print('Ready to serve...')

        # accepts an incoming connection request from a TCP client.
        connectionSocket, addr = serverSocket.accept() 

        try:

            # no of bytes to receive
            message = connectionSocket.recv(1024)

            if message:
                filename = message.split()[1]
                #print(message)
                f = open(filename[1:])

                outputdata = f.read() 
                # Send one HTTP header line into socket
                connectionSocket.send(
                    "HTTP/1.1 200 OK \r\n\r\n".encode('utf-8'))

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode('utf-8'))

            # connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            print(IOError)

            connectionSocket.send(
                "HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8'))
            connectionSocket.send("\r\n".encode('utf-8'))

            connectionSocket.close()

    serverSocket.close()

    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(6789)
