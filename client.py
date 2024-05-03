import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) #using UDP network socket
server_address = '/tmp/socket_file'
print('connecting to {}' .format(server_address))

try:
    sock.connect(server_address)
    print('Success connecting to server.')
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        username = input("Enter username: ")
        sock.sendall(username.encode())
except Exception as e:
    print("Error:", e)

        