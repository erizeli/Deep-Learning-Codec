import json
import librosa
import numpy as np
import requests
from recordWAV import convert_json, recordWAV
# Load the audio file
data1, fs1 = librosa.load("audio1.mp3", sr=16000)

user_input = ""
while user_input != "q":
    data_list = []
    user_input = input('Choose audio (enter "q" to esc): ')
    if user_input == "1":

        data_list = data1.tolist()


    elif user_input == "2":
        data_list = recordWAV().tolist()
        
    if user_input == "1" or user_input == "2":
        json_pack = convert_json("XXX", data_list)

        response = requests.post(
        "http://127.0.0.1:8000/voice_processing", 
        headers={"Content-Type": "application/json"},
        data=json_pack
        )

        print("Status:", response.status_code)
        print("Response:", response.json())