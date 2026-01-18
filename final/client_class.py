import socket

class Client:
    def __init__(self, host='127.0.0.1', port=12345):
        """
        Initialize a new client and connect to the server.
        """
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
        except ConnectionRefusedError:
            print("Connection failed. Is the server running?")
            self.socket = None

    def send(self, message):
        """
        Send a message to the server.
        """
        if self.socket:
            self.socket.sendall(message.encode())

    def receive(self):
        """
        Receive a response from the server.
        """
        if self.socket:
            response = self.socket.recv(1024)
            return response.decode()
        return None

    def close(self):
        """
        Close the connection.
        """
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Connection closed.")

# Example usage
if __name__ == "__main__":
    client = Client()
    while True:
        msg = input("Enter message (type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        client.send(msg)
        response = client.receive()
        print(f"Server says: {response}")
    client.close()
