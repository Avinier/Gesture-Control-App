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
rock_flag = True
thumbs_up_flag = True
ok_flag = True

def gesture_control(img, lm_list):
    global fist_flag, three_flag, rock_flag, thumbs_up_flag, ok_flag
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [2, 6, 10, 14, 18]
    finger_positions = []
    # For 'thumbs up' gesture
    index_mcp = (lm_list[5][1], lm_list[5][2])
    pinky_mcp = (lm_list[17][1], lm_list[17][2])
    thumb_tip = (lm_list[4][1], lm_list[4][2])
    wrist = (lm_list[0][1], lm_list[0][2])

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
    rock_statement = (finger_positions == [1, 1, 0, 0, 1])
    thumbsup_statement = ((index_mcp[0] and pinky_mcp[0]) > (wrist[0] and thumb_tip[0]))
    ok_statement = dist < 20

    if fist_statement:
        for i in range(0, 21):
            cv.circle(img, (lm_list[i][1], lm_list[i][2]), 20, (35, 68, 208), -1)
        if fist_flag:
            print("FIST")
            os.system('START POWERPNT.EXE')
            fist_flag = False

    if three_statement:
        cv.line(img, (lm_list[8][1], lm_list[8][2]), (lm_list[5][1], lm_list[5][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[12][1], lm_list[12][2]), (lm_list[9][1], lm_list[9][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[16][1], lm_list[16][2]), (lm_list[13][1], lm_list[13][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[5][1], lm_list[5][2]), (lm_list[9][1], lm_list[9][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[9][1], lm_list[9][2]), (lm_list[13][1], lm_list[13][2]), (200, 125, 0), 10)

        if three_flag:
            print("THREE")
            os.system('START WINWORD.EXE')
            three_flag = False

    if rock_statement:
        cv.line(img, (lm_list[8][1], lm_list[8][2]), (lm_list[5][1], lm_list[5][2]), (66, 111, 29), 10)
        cv.line(img, pinky_mcp, (lm_list[20][1], lm_list[20][2]), (66, 111, 29), 10)
        cv.line(img, index_mcp, pinky_mcp, (66, 111, 29), 10)
        cv.line(img, pinky_mcp, wrist, (66, 111, 29), 10)
        cv.line(img, index_mcp, wrist, (66, 111, 29), 10)
        cv.line(img, wrist, (lm_list[1][1], lm_list[1][2]), (66, 111, 29), 10)
        cv.line(img, thumb_tip, (lm_list[1][1], lm_list[1][2]), (66, 111, 29), 10)

        if rock_flag:
            print("ROCK")
            os.system('START EXCEL.EXE')
            rock_flag = False

    if thumbsup_statement:
        cv.line(img, index_mcp, pinky_mcp, (170, 25, 119), 10)
        cv.line(img, thumb_tip, (lm_list[3][1], lm_list[3][2]), (170, 25, 119), 10)
        cv.line(img, (lm_list[3][1], lm_list[3][2]), wrist, (170, 25, 119), 10)
        cv.line(img, wrist, pinky_mcp, (170, 25, 119), 10)
        cv.line(img, wrist, index_mcp, (170, 25, 119), 10)

        if thumbs_up_flag:
            print("THUMBS UP")
            os.system('START ONENOTE.EXE')
            thumbs_up_flag = False
    if ok_statement:
        x1, y1 = lm_list[6][1], lm_list[6][2]
        x2, y2 = lm_list[3][1], lm_list[3][2]
        circle_dist = math.hypot(x2 - x1, y2 - y1)
        radius = circle_dist//2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv.circle(img, (cx, cy), int(radius), (198, 114, 0), 10)
        if ok_flag:
            print("OK")
            os.system('START OUTLOOK.EXE')
            ok_flag = False

    # cv.imshow("Gesture Control", img)
    # cv.waitKey(1)