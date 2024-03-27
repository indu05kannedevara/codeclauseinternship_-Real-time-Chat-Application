import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    while True:
        # Receive message from client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        
        print(f"Received message from {client_address}: {data}")

        # Broadcast message to all clients
        broadcast(data, client_socket)

    print(f"Connection from {client_address} closed")
    client_socket.close()

# Function to broadcast message to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message to {client.getpeername()}: {e}")
                client.close()
                clients.remove(client)

# Server configuration
HOST = '127.0.0.1'
PORT = 55555

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# List to keep track of client sockets
clients = []

while True:
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()

    # Add client socket to the list
    clients.append(client_socket)

    # Create a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
