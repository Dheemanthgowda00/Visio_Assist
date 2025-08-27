# /home/raspberry/VISIOASSIST/OCR/ocr_read.py

import cv2
import requests
import subprocess
import time

API_KEY = 'ab8bd882d488957'
URL = 'https://api.ocr.space/parse/image'

def speak(text):
    subprocess.run(f'espeak \"{text}\" --stdout | aplay', shell=True)

def perform_ocr():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        speak("Camera error.")
        return

    speak("Starting OCR for 20 seconds.")
    start_time = time.time()
    last_text = set()
    frame_interval = 4  # capture every 4 seconds

    while time.time() - start_time < 20:
        ret, frame = cap.read()
        if not ret:
            continue

        image_path = "/tmp/temp_ocr.jpg"
        cv2.imwrite(image_path, frame)

        with open(image_path, 'rb') as image_file:
            response = requests.post(
                URL,
                files={'image': image_file},
                data={'apikey': API_KEY}
            )

        try:
            result = response.json()
            if result.get('IsErroredOnProcessing') is False:
                extracted = result['ParsedResults'][0]['ParsedText'].strip()
                if extracted:
                    last_text.add(extracted)
            else:
                print("OCR error:", result.get('ErrorMessage'))
        except:
            continue

        time.sleep(frame_interval)

    cap.release()

    final_text = " ".join(last_text).strip()
    if final_text:
        speak("Text detected is:")
        speak(final_text)
    else:
        speak("No readable text was detected.")

if __name__ == "__main__":
    perform_ocr()
