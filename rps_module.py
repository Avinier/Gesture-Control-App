import os
import math
import cv2 as cv
import hand_tracking_module as htm

# vid = cv.VideoCapture(0)
# width_cam, height_cam = 1280, 720
# vid.set(3, width_cam)
# vid.set(4, height_cam)

ges_detector = htm.HandDetector()

fist_flag = True
three_flag = True
scissors_flag = True
kill_flag = True


def rps_control(img, lm_list):
    global fist_flag, three_flag, scissors_flag ,kill_flag
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [2, 6, 10, 14, 18]
    finger_positions = []
    # For 'thumbs up' gesture
    index_mcp = (lm_list[5][1], lm_list[5][2])
    pinky_mcp = (lm_list[17][1], lm_list[17][2])
    thumb_tip = (lm_list[4][1], lm_list[4][2])

    # For 'ok' gesture
    index_tip = (lm_list[8][1], lm_list[8][2])
    dist = math.hypot(thumb_tip[0] - index_tip[0], thumb_tip[1] - index_tip[1])

    # For Thumb
    if lm_list[4][1] > lm_list[3][1]:
        finger_positions.insert(0, 1)
    else:
        finger_positions.insert(0, 0)

    # For 4 fingers
    for i in range(1, 5):
        if lm_list[finger_tips[i]][2] < lm_list[finger_pips[i]][2]:
            finger_positions.append(1)
        else:
            finger_positions.append(0)

    fist_statement = (finger_positions == [0, 0, 0, 0, 0] and index_mcp > pinky_mcp)
    three_statement = (finger_positions == [0, 1, 1, 1, 0])
    scissors_statement = (finger_positions == [0, 1, 1, 0, 0])
    kill_statement = (finger_positions == [0, 0, 0, 0, 1])

    if fist_statement:
        for i in range(0, 21):
            cv.circle(img, (lm_list[i][1], lm_list[i][2]), 20, (205,133,0), -1)
        if fist_flag:
            print("FIST")
            os.system('START BRAVE.EXE')
            os.system('TASKKILL /IM CHROME.EXE')
            scissors_flag = True
            fist_flag = False

    if three_statement:
        cv.line(img, (lm_list[8][1], lm_list[8][2]), (lm_list[5][1], lm_list[5][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[12][1], lm_list[12][2]), (lm_list[9][1], lm_list[9][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[16][1], lm_list[16][2]), (lm_list[13][1], lm_list[13][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[5][1], lm_list[5][2]), (lm_list[9][1], lm_list[9][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[9][1], lm_list[9][2]), (lm_list[13][1], lm_list[13][2]), (200, 125, 0), 10)

        if three_flag:
            print("THREE")
            os.system('START FIREFOX.EXE')
            os.system('TASKKILL /IM BRAVE.EXE')
            fist_flag = True
            three_flag = False

    if scissors_statement:
        cv.line(img, (lm_list[8][1], lm_list[8][2]), (lm_list[5][1], lm_list[5][2]), (66, 111, 29), 10)
        cv.line(img, (lm_list[12][1],lm_list[12][2]),(lm_list[9][1],lm_list[9][2]),(66, 111, 29), 10)
        cv.line(img, (lm_list[5][1],lm_list[5][2]),(lm_list[9][1],lm_list[9][2]),(66, 111, 29), 10)

        if scissors_flag:
            print("SCISSORS")
            os.system('START CHROME.EXE')
            os.system('TASKKILL /IM FIREFOX.EXE')
            three_flag = True
            scissors_flag = False

    if kill_statement:
        for i in range(0, 21):
            cv.circle(img, (lm_list[i][1], lm_list[i][2]), 20, (0,0,0), -1)
        if kill_flag:
            print("KILL")
            os.system('TASKILL /IM BRAVE.EXE')
            os.system('TASKKILL /IM CHROME.EXE')
            os.system('TASKKILL /IM FIREFOX.EXE')
            scissors_flag = False
            three_flag = False
            fist_flag = False
            kill_flag = False
            print("PROCESS TERMINATED")


    # cv.imshow("Gesture Control Test", img)
    # cv.waitKey(1)
