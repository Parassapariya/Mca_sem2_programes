import socket
HOST = 'localhost'
PORT = 8080
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect((HOST, PORT))
# Print the connection information
print("Connected to {}:{}".format(HOST, PORT))
# Send and receive messages
while True:
    message = input("Enter your message: ")
    client_socket.sendall(message.encode())
    if message.lower() == 'bye':
        break
    data = client_socket.recv(1024).decode()
    print("Server: {}".format(data))
# Close the connection
client_socket.close()