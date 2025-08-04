# client.py
import socket

SERVER_IP = '192.168.1.24'  # CHANGE THIS to your receiver's IP
PORT = 5001
FILE_TO_SEND = 'your_file.pdf'  # CHANGE THIS to the path of your file

client = socket.socket()
client.connect((SERVER_IP, PORT))

with open(FILE_TO_SEND, 'rb') as f:
    while True:
        data = f.read(4096)
        if not data:
            break
        client.sendall(data)

print(f"[CLIENT] File '{FILE_TO_SEND}' sent successfully.")
client.close()
