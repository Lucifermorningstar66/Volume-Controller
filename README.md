# 🖐 Hand Gesture Volume Controller

Control your system's audio volume using simple hand gestures via your webcam! This project uses Python, OpenCV, and MediaPipe to track hand movements and adjust volume in real-time based on the distance between your fingers.

---

## ✨ Features

- 📷 Real-time hand tracking using MediaPipe
- 🔊 Smooth control of system volume with finger pinch
- 💡 Visual feedback for distance and volume level
- ⚙️ Adjustable parameters for fine-tuning accuracy

---

## 🛠 Technologies Used

- Python 3.x
- OpenCV
- MediaPipe (by Google)
- PyCaw (Python Core Audio Windows Library)

---

## ▶️ Run the Project
```bash
python Volume.py
```
A webcam window will open, and you'll be able to control volume by:
Bringing your thumb and index finger close together = Low volume
Spreading them apart = High volume
The system volume will update in real-time!

---

## 🎥 How It Works
MediaPipe detects and tracks your hand in real-time.
The distance between your thumb tip and index finger tip is calculated.
This distance is mapped to a volume level using linear interpolation.
PyCaw interfaces with your system to change the volume accordingly.

If ModuleNotFoundError appears, install missing packages using pip.

Ensure you're running on Windows (due to pycaw compatibility).

---

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙌 Acknowledgments
MediaPipe – Real-time ML solutions by Google
PyCaw – Control Windows volume with Python
OpenCV community

---

## 📬 Contact
Created by @Lucifermorningstar66 — feel free to connect!
