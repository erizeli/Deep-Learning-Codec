from record import record
from stt_processing import record_msg
from packetize import packetize
from send_packet import send_packet

def client():
    samples = record()
    text = record_msg(samples)
    packet = packetize(text)
    send_packet(packet)


if __name__ == "__main__":
    client()