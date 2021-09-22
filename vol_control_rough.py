#TODO: Creating functions or modules based on gestures
#TODO: Debug multiple openings problem
#TODO: Figure out "ok" gesture
#TODO: Debug thumb and fist problem

# Importing libraries and modules
import cv2 as cv
import numpy as np
import time
import math
# Importing self-made modules
import hand_tracking_module as htm
import volume_control_module as gsc

# Importing modules for volume control (PyCAW)
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#Setting size of display window
vid = cv.VideoCapture(0)
width_cam, height_cam = 1280, 720
vid.set(3, width_cam)
vid.set(4, height_cam)


detector = htm.HandDetector(max_hands=2, detection_confidence=0.75)
prev_time = 0
# Declaring volume variables
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()

vol_range = volume.GetVolumeRange()
# Setting minimum and maximum vol values to variables
min_vol = vol_range[0]
max_vol = vol_range[1]
# bar = initial y-coordinate of rectangle
vol_bar = 500
# per = initial percentage of volume
vol_per = 0
vol_flag = True

while True:
    success, img = vid.read()
    # Mediapipe tracker activated
    img = detector.detect_hands(img)
    # Storing all co-ordinates of hand-landmarks in a list
    lm_list = detector.position_hands(img, dots=False)
    # if hand exists on the screen, execute the loop
    if len(lm_list) != 0:
        gsc.vol_control(img, lm_list)

    # Setting fps
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    # Displaying the fps
    cv.putText(img, str(int(fps)) + " fps", (10, 50), cv.FONT_HERSHEY_PLAIN, 3, (100, 50, 200), 4)

    # Displaying the video, i.e a series of images
    cv.imshow("Volume Control", img)
    # Old window closes every 1ms
    cv.waitKey(1)

##FOR APP OPENING-
# class AppOpeners():
#     def __init__(self, lm_list, img):
#         self.lm_list = lm_list
#         self.img = img
#
#     def powerpoint(self, x_index, y_index, x_index_pip, y_index_pip):
#         self.x_index, self.y_index = x_index, y_index
#         self.x_index_pip, self.y_index_pip = x_index_pip, y_index_pip
#
#
#
#             if (x_index_pip > x_index and y_index_pip > y_index):
#                 os.system('POWERPNT.EXE')


# Taking co-odrinates of index finger and thumb


