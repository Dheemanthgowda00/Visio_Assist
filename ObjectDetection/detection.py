import cv2
import subprocess
import time

# ───── Load class names ─────
classNames = []
classFile = r'/home/raspberry/VISIOASSIST/ObjectDetection/coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# ───── Model config and weights ─────
configPath = r'/home/raspberry/VISIOASSIST/ObjectDetection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = r'/home/raspberry/VISIOASSIST/ObjectDetection/frozen_inference_graph.pb'

# ───── Initialize model ─────
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# ───── Speak function ─────
def speak(text):
    subprocess.run(f'espeak "{text}"', shell=True)

# ───── Start video capture ─────
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

if not cap.isOpened():
    print("❌ Camera failed to open")
    exit()

print("🚀 Headless object detection started...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame")
            break

        classIds, confs, bbox = net.detect(frame, confThreshold=0.55)

        if len(classIds) != 0:
            for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                className = classNames[classId - 1].upper()
                print(f"🔍 Detected: {className} ({round(confidence * 100, 2)}%)")
                speak(f"Detected {className}")
        
        time.sleep(0.5)  # Avoid repeated rapid announcements

except KeyboardInterrupt:
    print("\n🛑 Detection stopped manually.")

finally:
    cap.release()
    print("📷 Camera released.")
