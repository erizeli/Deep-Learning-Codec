from tts_processing import process_rsp
from receive_packet import receive_packet

def server():
    packet = receive_packet()
    path = process_rsp(packet["text"])
    print(f"Response saved at {path}")

if __name__ == "__main__":
    server()