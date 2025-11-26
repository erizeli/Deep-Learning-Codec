import socket
import json

def receive_packet() -> str:
    HOST: str = "0.0.0.0"
    PORT: int = 5001

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"[SERVER] Listening on port {PORT}...")

    conn, addr = server.accept()
    print(f"[SERVER] Connected by {addr}")

    data = conn.recv(100000)
    conn.close()

    packet = data.decode("utf-8")
    return json.loads(packet)


#tts_processing.process_rsp(full_message)

if __name__ == "__main__":
    packet = receive_packet()
    text = packet["text"]
    print("[DEBUG] Message Received: \"{text}\"")
