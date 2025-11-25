# client.py
import socket

def send_packet(packet) -> None:     
    SERVER_IP = get_local_ip()  
    PORT = 5001

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, PORT))
    sock.sendall(packet.encode("utf-8"))

    print(f"[CLIENT] File '{packet}' sent successfully.")
    sock.close()

def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
