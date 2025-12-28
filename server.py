import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost and port 12345
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

# Accept a connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    # Receive data from client
    data = conn.recv(1024)
    if not data:
        break
    msg = data.decode()
    print(f"Received from client: {msg}")

    # Send a customized response
    response = f"hello, {msg}"
    conn.sendall(response.encode())

# Close connection
conn.close()
server_socket.close()
