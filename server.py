import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}' .format(server_address))
sock.bind(server_address)

while True:
    while True:
        name, client_address = sock.recvfrom(255) #receive user name
        message , client_address = sock.recvfrom(4096) #receive user message

        if message:
                print(name, ": ", message)
                #name_bytes = name.encode() # convet name to byte
                #message_bytes = message.encode() #convert message to byte
                sock.sendto(name, client_address)
                sock.sendto(message, client_address)                
        else:
            print('No message received, clietn disconnected')
            break

    print("Closing current connection.")
