import socket
server_address = ('localhost', 12345)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)

print('start up server')

usernames = {}

while True:
    data, address = sock.recvfrom(4096)
    usernamelen = data[0]
    username = data[1: 1+usernamelen].decode()
    message = data[1+usernamelen:].decode()
    print(f"user name: {username} from: {address} message: {message}")

    if address not in usernames:
        usernames[address] = username
        print(f"username '{username}' saved. current user: {username}")

        response_message = f"{username}: {message}"
        sock.sendto(response_message.encode(), address)