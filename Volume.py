import cv2
import numpy as np
import math
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import Handtracker as customHand

width, height = 640, 480
camera = cv2.VideoCapture(0)
camera.set(3, width)
camera.set(4, height)
handTracker = customHand.handDetector(detectionCon=1)

audio_device = AudioUtilities.GetSpeakers()
audio_interface = audio_device.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_controller = cast(audio_interface, POINTER(IAudioEndpointVolume))
vol_min, vol_max = volume_controller.GetVolumeRange()[:2]

vol_level = 0
vol_percent = 0
vol_bar_target = 400
vol_bar_current = 400

while True:
    success, frame = camera.read()
    if not success:
        continue
    frame = handTracker.findHands(frame)
    lmList, _ = handTracker.findPosition(frame, draw=False)
    if lmList and len(lmList) > 8:
        x_thumb, y_thumb = lmList[4][1], lmList[4][2]
        x_index, y_index = lmList[8][1], lmList[8][2]
        x_center, y_center = (x_thumb + x_index) // 2, (y_thumb + y_index) // 2
        cv2.circle(frame, (x_thumb, y_thumb), 10, (255, 100, 100), cv2.FILLED)
        cv2.circle(frame, (x_index, y_index), 10, (255, 100, 100), cv2.FILLED)
        cv2.line(frame, (x_thumb, y_thumb), (x_index, y_index), (255, 100, 100), 2)
        cv2.circle(frame, (x_center, y_center), 8, (255, 100, 100), cv2.FILLED)
        distance = math.hypot(x_index - x_thumb, y_index - y_thumb)

        vol_level = np.interp(distance, [50, 300], [vol_min, vol_max])
        vol_bar_target = np.interp(distance, [50, 300], [400, 150])
        vol_percent = np.interp(distance, [50, 300], [0, 100])

        if abs(volume_controller.GetMasterVolumeLevel() - vol_level) > 1.5:
            volume_controller.SetMasterVolumeLevel(vol_level, None)

        if distance < 50:
            cv2.circle(frame, (x_center, y_center), 10, (0, 255, 0), cv2.FILLED)

    vol_bar_current = int(vol_bar_current + (vol_bar_target - vol_bar_current) * 0.2)

    cv2.rectangle(frame, (50, 150), (85, 400), (100, 100, 255), 3)
    cv2.rectangle(frame, (50, vol_bar_current), (85, 400), (100, 100, 255), cv2.FILLED)
    cv2.putText(frame, f'{int(vol_percent)}%', (40, 440),
                cv2.FONT_HERSHEY_PLAIN, 2, (100, 100, 255), 2)
    cv2.imshow("Smart Volume Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
