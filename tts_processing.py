import torch
import numpy as np
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig

##############
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
tts.to("cuda")

def process_rsp(data):
    tts.tts_to_file(
        text=data,
        speaker_wav="audio_out.wav",
        language="en",
        file_path="result.wav"
    )
    return None

