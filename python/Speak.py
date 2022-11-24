import glob
import json
import os
import wave

import numpy as np
import requests
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv()


def Speak(message):
    returnValue = None
    params = (
        ("text", message),
        ("speaker", os.getenv("SPEAKER")),
    )
    audio_query = requests.post(
        f"http://localhost:50021/audio_query",
        params=params
    )
    headers = {"Content-Type": "application/json", }
    synthesis = requests.post(
        f"http://localhost:50021/synthesis",
        headers=headers,
        params=params,
        data=json.dumps(audio_query.json())
    )
    with wave.open("message.wav", "wb") as messageData:
        messageData.setnchannels(1)
        messageData.setsampwidth(2)
        messageData.setframerate(24000)
        messageData.writeframes(synthesis.content)
    audios = []
    for f in sorted(glob.glob("message.wav")):
        with wave.open(f, "rb") as fp:
            buf = fp.readframes(-1)
            assert fp.getsampwidth() == 2
            audios.append(np.frombuffer(buf, np.int16))
            params = fp.getparams()
    audio_data = np.concatenate(audios)
    scaling_factors = [np.iinfo(np.int16).max/(np.max(audio_data)+1e-8),
                       np.iinfo(np.int16).min/(np.min(audio_data)+1e-8)]
    scaling_factors = min([s for s in scaling_factors if s > 0])
    audio_data = (audio_data * scaling_factors).astype(np.int16)
    with wave.Wave_write("message.wav") as fp:
        fp.setparams(params)
        fp.writeframes(audio_data.tobytes())
    sound = AudioSegment.from_file("message.wav", format="wav")[100:10000]
    sound.export("message.wav", format="wav")
    returnValue = "Success"
    return returnValue
