import socket
import sys
import time

TIMEOUT_THRESHOLD = 120

last_activate_time = time.time()
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) #using UDP network socke

server_address = '/tmp/socket_file'
print('connecting to {}' .format(server_address))

# Automatically connecting to server so dont need this part
#try:
#    sock.connect(server_address)
#    print('Success connecting to server.')
#except socket.error as err:
#    print(err)
#    sys.exit(1)

#First action by user
try:
    while True:
        username = input("Enter username: ") 
        sock.sendto(username.encode(), server_address) #send user name
        break
except Exception as e:
    print("Error:", e)

#Second action by user
try:
    while True:
        message = input("Send message: ")
        sock.sendto(message.encode(), server_address) #send message

        username_other, server = sock.recvfrom(255) # receive user name
        data, server = sock.recvfrom(4096) # receive message from other user
        if data:
            if username_other == username:
                print("You: ", data)
            else:
                print(username_other, ": ", data)            
            last_activity_time = time.time()
        else:
            break

        if time.time() - last_activity_time > TIMEOUT_THRESHOLD:
            print("Client has been inactive for too long. Removing from relay system.")
            break

except Exception as e:
    print("Erro:", e)

finally:
    print('closing connection')
    sock.close()        