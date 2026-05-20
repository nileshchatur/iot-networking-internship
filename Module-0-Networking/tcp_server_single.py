import socket

# Step 1: Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind the socket to localhost and port 5000
server_socket.bind(("127.0.0.1", 5000))

# Step 3: Put the socket into listening mode
server_socket.listen(1)

print("Server is waiting for a client connection...")

# Step 4: Accept a connection from a client
client_socket, client_address = server_socket.accept()
print("Connected to client:", client_address)

# Step 5: Receive data from the client
data = client_socket.recv(1024)
print("Message from client:", data.decode())

# Step 6: Send reply to the client
client_socket.send(b"Hello from server")

# Step 7: Close client socket
client_socket.close()

# Step 8: Close server socket
server_socket.close()

print("Server closed")