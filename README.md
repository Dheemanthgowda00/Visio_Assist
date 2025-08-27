# Visio Assist  

Visio Assist is an **AI-powered assistive system** that integrates **computer vision, OCR, and a voice assistant**.  
It is designed to run on **Raspberry Pi (or PC)** and provides real-time support for **object detection, text recognition, and voice-based interaction**.  

---

## 🚀 Features  

- 📖 **OCR (Optical Character Recognition)**  
  - Extracts text from images and live camera feed.  

- 🎯 **Object Detection**  
  - Detects real-world objects using **SSD MobileNet v3**.  
  - Uses pretrained **COCO dataset** for classification.  

- 🎙 **Voice Assistant**  
  - Responds to user queries via **STT (Vosk)** and **TTS (Piper)**.  
  - Stores secure notes and reminders.  
  - Provides real-time assistance with interactive commands.  

- 🔐 **Secure Data Management**  
  - Stores encrypted notes and reminders.  
  - Supports secure key-based storage.  

---

## 📂 Project Structure

```bash
Visio_Assist/
│── OCR/                         # Optical Character Recognition module
│   └── ocr.py
│
│── ObjectDetection/              # Object detection using SSD MobileNet
│   ├── coco.names
│   ├── detection.py
│   ├── frozen_inference_graph.pb
│   └── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
│
│── VoiceAssistant/               # Voice assistant module
│   ├── assistant/                # Core assistant logic
│   │   └── models/               # Speech models
│   │       ├── piper/            # TTS model (Piper)
│   │       └── vosk/             # STT model (Vosk)
│   │
│   ├── data/                     # User data and reminders
│   │   └── reminders.json
│   │
│   ├── secure/                   # Encrypted/secure storage
│   │   ├── notes.json
│   │   └── secret.key
│   │
│   ├── assistant.py              # Main voice assistant logic
│   ├── reminder.py               # Reminder handling
│   ├── secure_notes.py           # Secure notes management
│   ├── test_stt.py               # Speech-to-text testing
│   ├── test_tts.py               # Text-to-speech testing
│   └── user_data.json            # User profile / settings
│
│── .gitignore                    # Git ignore rules
│── README.md                     # Project documentation
│── info.txt                      # Info / project notes
```

---

## 🛠 Python Libraries / Dependencies

- cv2 (OpenCV) – for image/video processing
- subprocess – for running system commands
- time – for time-related functions
- requests – for HTTP requests
- os – for operating system interaction
- sys – for system-specific parameters and functions
- json – for JSON encoding/decoding
- sounddevice – for audio input/output
- numpy – for numerical computations
- scipy.signal – for signal processing
- piper.voice (PiperVoice) – for TTS (Text-to-Speech)
- speech_recognition – for speech-to-text
- dotenv – for environment variable management (load_dotenv)
- signal – for handling signals
- datetime – for date and time operations
- pytz – for timezone handling
- smtplib – for sending emails
- email.mime.text – for creating email content
- yt_dlp – for YouTube video/audio downloading
- secure_notes – custom module for secure note management (save_secure_note, load_secure_note, load_notes)
- reminder – custom module for reminders (schedule_reminder, load_existing_reminders)
- twilio.rest (Client) – for Twilio API integration (SMS/calls)
- dateparser – for parsing dates from text
- apscheduler.schedulers.background (BackgroundScheduler) – for scheduling tasks
- cryptography.fernet (Fernet) – for encryption/decryption
- vosk (Model, KaldiRecognizer) – for offline speech recognition
- queue – for thread-safe queues


