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

