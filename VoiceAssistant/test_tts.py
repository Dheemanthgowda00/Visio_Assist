import sounddevice as sd
import numpy as np
from piper.voice import PiperVoice
import scipy.signal

# Load the Piper voice model
voice = PiperVoice.load("assistant/models/piper/en_US-lessac-medium.onnx")

# Synthesize speech
audio_chunks = voice.synthesize("Hello, I am your offline voice assistant. Everything is working!")

# Concatenate audio data
audio_bytes = b"".join(chunk.audio_int16_bytes for chunk in audio_chunks)

# Convert to NumPy array
audio_array = np.frombuffer(audio_bytes, dtype=np.int16)

# 🔉 Lower the volume (scale down amplitude)
audio_array = (audio_array *1.0).astype(np.int16)  # 0.5 means 50% volume

# 🐢 Slow down the speed (resample to stretch time)
original_rate = 16000
slow_rate = int(original_rate * 1.0)  # 80% speed (slower)
number_of_samples = int(len(audio_array) * original_rate / slow_rate)
slowed_audio = scipy.signal.resample(audio_array, number_of_samples).astype(np.int16)

# Play the slowed and quieter audio
sd.play(slowed_audio, samplerate=original_rate)
sd.wait()
