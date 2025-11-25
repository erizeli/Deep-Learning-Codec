# records user input stream, returns raw audio in int array form

import pyaudio
import keyboard
from scipy.io.wavfile import write
import numpy as np

def record():
    format = pyaudio.paInt16
    chunk = 1024
    channels = 1
    fs = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=fs,
                    input=True,
                    frames_per_buffer=chunk)

    print("NOW RECORDING (press s to stop): ")
    stop = False
    frames = []
    while (not stop): 
        data = stream.read(chunk)
        frames.append(data)
        if keyboard.is_pressed("s"):  
            stop = True

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Join all chunks into a single bytes object
    all_bytes = b''.join(frames)

    # Convert to int16 NumPy array
    samples = np.frombuffer(all_bytes, dtype=np.int16)  # shape: (num_samples,)

    write("audiofiles/initial_audio.wav", 16000, samples)
    return samples

