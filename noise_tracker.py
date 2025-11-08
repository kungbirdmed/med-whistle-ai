# noise_tracker.py - auto-log harassment
import datetime, geocoder, sounddevice as sd
import numpy as np, wavio

def record_and_tag(duration=10):
    print("Recording... speak or let the revving happen.")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
    sd.wait()
    wavio.write(f"logs/rev_{datetime.datetime.now().isoformat()}.wav", audio, 44100, sampwidth=2)
    loc = geocoder.ip('me').latlng
    print(f"Logged: {loc} | {duration}s | #ReinaRise")

record_and_tag()
