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
    audioQuery = requests.post(
        f"http://localhost:50021/audioQuery",
        params=params
    )
    headers = {"Content-Type": "application/json", }
    synthesis = requests.post(
        f"http://localhost:50021/synthesis",
        headers=headers,
        params=params,
        data=json.dumps(audioQuery.json())
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
    audioData = np.concatenate(audios)
    scalingFactors = [np.iinfo(np.int16).max/(np.max(audioData)+1e-8),
                       np.iinfo(np.int16).min/(np.min(audioData)+1e-8)]
    scalingFactors = min([s for s in scalingFactors if s > 0])
    audioData = (audioData * scalingFactors).astype(np.int16)
    with wave.Wave_write("message.wav") as fp:
        fp.setparams(params)
        fp.writeframes(audioData.tobytes())
    sound = AudioSegment.from_file("message.wav", format="wav")[100:10000]
    sound.export("message.wav", format="wav")
    returnValue = "Success"
    return returnValue
