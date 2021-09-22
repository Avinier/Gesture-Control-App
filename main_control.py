# TODO: Make GUI with Tkinter (Aditya- Developing, Dhruv- Designing)
#TODO: Fix minor GUI bugs
# TODO: Make exe file (app)
# TODO: Fine tune code (later)
# TODO: Fix volume-control bug (later)
import cv2 as cv
import time

import hand_tracking_module as htm
import volume_control_module as vsc
import gesture_controls_module as gsc
# import control_gui as gui
import rps_module as rps

from tkinter import *
from PIL import Image, ImageTk

# Create an instance of TKinter Window or frame
win = Tk()
# Set the size of the window
win.geometry("700x350")
# Create a Label to capture the Video frames
label =Label(win)
label.grid(row=0, column=0)

vid = cv.VideoCapture(0)
width_cam, height_cam = 1000, 620
vid.set(3, width_cam)
vid.set(4, height_cam)

# gui.vol_toggle()
def main():
    detector = htm.HandDetector()
    prev_time = 0
    vol_flag = False
    gesture_flag = False
    rps_flag = False
    while True:
        success, img = vid.read()
        img = detector.detect_hands(img)
        lm_list = detector.position_hands(img, dots=False)

        if len(lm_list) != 0:
            if vol_flag:
                vsc.vol_control(img, lm_list)
            if gesture_flag:
                gsc.gesture_control(img, lm_list)
            if rps_flag:
                rps.rps_control(img, lm_list)

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        cv.putText(img, str(int(fps)) + " fps", (10, 50), cv.FONT_HERSHEY_PLAIN, 3, (100, 50, 200), 4)
        cv.waitKey(1)
        cv.imshow("Volume Control", img)

main()





