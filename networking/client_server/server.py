#using socket programming clent server message passing  
import socket
HOST = ''
PORT = 8080
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the port
server_socket.bind((HOST, PORT))
# Listen for incoming connections
server_socket.listen(5)
print("Listening on port {}:{}".format(HOST,PORT))
# Accept the connection
conn, addr = server_socket.accept()
print("Connection from: {}:{}".format(addr[0], addr[1]))
# Receive and send messages
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Client: {}".format(data))
    message = input("Enter your message: ")
    conn.sendall(message.encode())
    if message.lower() == 'bye':
        break
# Close the connection
conn.close()
server_socket.close()
#using socket programming clent server message passing

