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

try:
    while True:
        message = input("Send message")
        sock.sendall(message.encode())

        username_other = sock.recv(255) # receive user name
        data = sock.recv(4096) # receive message from other user
        if data:
            print("Message from", username_other.decode(), ": ",  data.decode())            
        else:
            break

except Exception as e:
    print("Erro:", e)

finally:
    print('closing connection')
    sock.close()        