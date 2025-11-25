import torch
import numpy as np
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
import os

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
tts.to("cuda")

def process_rsp(text):
    tts.tts_to_file(
        text=text,
        speaker_wav="audio_out.wav",
        language="en",
        file_path="audio_files/result.wav"
    )
    return os.join(os.getcwd(), "audio_files/result.wav")


if __name__ == "__main__":
    TEST_DATA = "hello, how are you?"
    path = process_rsp()
    print(f"result stored at {path}")