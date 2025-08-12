# client.py
import socket
from recordWAV import recordWAV
import stt_processing

voice_msg = recordWAV()
txt_encoding = stt_processing.process_msg(voice_msg)

SERVER_IP = '192.168.1.24'  
PORT = 5001
FILE_TO_SEND = txt_encoding

if isinstance(txt_encoding, list):
    txt_encoding = "".join(map(str, txt_encoding))

client = socket.socket()
client.connect((SERVER_IP, PORT))
client.sendall(txt_encoding.encode("utf-8"))

print(f"[CLIENT] File '{FILE_TO_SEND}' sent successfully.")
client.close()
