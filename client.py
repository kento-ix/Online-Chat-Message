import socket

server_address = ('localhost', 12345)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

username = input("Enter username: ")
message = input("Enter message: ")

usernamelen = len(username)
if usernamelen > 255:
    raise ValueError("Too long username.")

packet = bytes([usernamelen]) + username.encode() + message.encode()

try:
    sent = sock.sendto(packet, server_address)

    data, server = sock.recvfrom(4096)
    print(data.decode())

finally:
    print("Socket close")
    sock.close()