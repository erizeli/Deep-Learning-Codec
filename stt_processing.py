import whisper
import torch
import numpy as np

model = whisper.load_model("base")

def process_msg(data):
    data = np.array(data).astype("float32") / 32768.0
    print(data)
    result = model.transcribe(data)
    return result["text"]