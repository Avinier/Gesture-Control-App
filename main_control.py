# TODO: Make exe file (app)
# TODO: Fine tune code (later)
import cv2 as cv
import time

import hand_tracking_module as htm
import volume_control_module as vsc
import gesture_controls_module as gsc
import rps_module as rps

vid = cv.VideoCapture(0)
width_cam, height_cam = 1000, 620
vid.set(3, width_cam)
vid.set(4, height_cam)

vol_flag = False
gesture_flag = False
rps_flag = False

def set_volflag(flag_bool):
    global vol_flag
    vol_flag = flag_bool

def set_gestureflag(gestureflag):
    global gesture_flag
    gesture_flag = gestureflag

def set_rpsflag(rpsflag):
    global rps_flag
    rps_flag = rpsflag


def main():
    detector = htm.HandDetector()
    prev_time = 0

    global vol_flag, gesture_flag, rps_flag
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
        cv.imshow("Gesture Recognition and Hand Tracking", img)

        cv.waitKey(1)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break
