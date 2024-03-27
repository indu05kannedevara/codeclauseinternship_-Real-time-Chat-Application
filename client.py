import socket
import threading

# Function to receive messages from server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Client configuration
HOST = '127.0.0.1'
PORT = 55555

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))

# Start a thread to receive messages from server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send messages to server
while True:
    message = input()
    client_socket.send(message.encode('utf-8'))
