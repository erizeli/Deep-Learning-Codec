# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# from processing import process_msg, process_rsp

# class VoiceRequest(BaseModel):
#     to: str
#     vdata: List[float]

# class SMSresponse(BaseModel):
#     sender: str
#     rsp_msg: str

# app = FastAPI()

# @app.post("/voice_processing")
# async def voice_processing(msg: VoiceRequest):
#     text = process_msg(msg.to, msg.vdata)

#     ######
#     #LOGIC FOR SMS
#     ######
#     #For now, placeholder by calling process rsp method

#     process_rsp(text)
#     return {"message": text}


# @app.post("/sms_response")
# async def sms_response(sms: SMSresponse):
#     print(f"Received SMS response: {sms.rsp_msg}")
#     process_rsp(sms.rsp_msg)
#     return {"status": "SMS response received", "message": sms.rsp_msg}

# server.py
import socket

HOST = '0.0.0.0'  # Accept connections from any IP
PORT = 5001       # Port number

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print(f"[SERVER] Listening on port {PORT}...")

conn, addr = server.accept()
print(f"[SERVER] Connected by {addr}")

filename = 'received_file.bin'
with open(filename, 'wb') as f:
    while True:
        data = conn.recv(4096)
        if not data:
            break
        f.write(data)

print(f"[SERVER] File received and saved as {filename}")
conn.close()
server.close()
