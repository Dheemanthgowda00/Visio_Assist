from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import queue

# Path to your Vosk model
model_path = "assistant/models/vosk/en"

# Sample rate (required by model)
sample_rate = 16000

# Load the model
model = Model(model_path)
recognizer = KaldiRecognizer(model, sample_rate)

# Create a queue to handle audio input
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print("⚠️ Status:", status)
    q.put(bytes(indata))

# Start recording from microphone
print("🎙 Speak into your mic... (Ctrl+C to stop)")
try:
    with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print("🗣 You said:", result.get("text", ""))
except KeyboardInterrupt:
    print("\n🛑 Stopped by user")
except Exception as e:
    print("❌ Error:", str(e))
