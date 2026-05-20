import socket

# Step 1: Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server at localhost port 5000
client_socket.connect(("127.0.0.1", 5000))

# Step 3: Send data to the server
client_socket.send(b"Hello from client")

# Step 4: Receive reply from the server
data = client_socket.recv(1024)
print("Message from server:", data.decode())

# Step 5: Close the socket
client_socket.close()
