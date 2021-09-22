import os
import cv2 as cv
import hand_tracking_module as htm

# vid = cv.VideoCapture(0)
# width_cam, height_cam = 1280, 720
# vid.set(3, width_cam)
# vid.set(4, height_cam)

rps_detector = htm.HandDetector()

fist_flag = True
scissors_flag = True
paper4_flag = True
exit_flag = True

def rps_control(img, lm_list):
    global fist_flag, scissors_flag, paper4_flag, exit_flag
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [2, 6, 10, 14, 18]
    finger_positions = []
    # For 'thumbs up' gesture
    index_mcp = (lm_list[5][1], lm_list[5][2])
    pinky_mcp = (lm_list[17][1], lm_list[17][2])
    thumb_tip = (lm_list[4][1], lm_list[4][2])
    wrist = (lm_list[0][1], lm_list[0][2])

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
    scissors_statement = (finger_positions == [0, 1, 1, 0, 0])
    paper4_statement = (finger_positions == [0, 0, 1, 1, 1])
    exit_statement = (finger_positions == [0, 0, 0, 0, 1])

    if fist_statement:
        for i in range(0, 21):
            cv.circle(img, (lm_list[i][1], lm_list[i][2]), 20, (35, 68, 208), -1)
        if fist_flag:
            print("FIST")
            os.system('START POWERPNT.EXE')
            os.system('TASKKILL /IM WINWORD.EXE')


    if scissors_statement:
        cv.line(img, (lm_list[8][1], lm_list[8][2]), (lm_list[5][1], lm_list[5][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[12][1], lm_list[12][2]), (lm_list[9][1], lm_list[9][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[16][1], lm_list[16][2]), (lm_list[13][1], lm_list[13][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[5][1], lm_list[5][2]), (lm_list[9][1], lm_list[9][2]), (200, 125, 0), 10)
        cv.line(img, (lm_list[9][1], lm_list[9][2]), (lm_list[13][1], lm_list[13][2]), (200, 125, 0), 10)

        if scissors_flag:
            print("SCISSORS")
            os.system('START WINWORD.EXE')
            os.system('TASKKILL /IM EXCEL.EXE')


    if paper4_statement:
        cv.line(img, (lm_list[8][1], lm_list[8][2]), (lm_list[5][1], lm_list[5][2]), (66, 111, 29), 10)
        cv.line(img, pinky_mcp, (lm_list[20][1], lm_list[20][2]), (66, 111, 29), 10)
        cv.line(img, index_mcp, pinky_mcp, (66, 111, 29), 10)
        cv.line(img, pinky_mcp, wrist, (66, 111, 29), 10)
        cv.line(img, index_mcp, wrist, (66, 111, 29), 10)
        cv.line(img, wrist, (lm_list[1][1], lm_list[1][2]), (66, 111, 29), 10)
        cv.line(img, thumb_tip, (lm_list[1][1], lm_list[1][2]), (66, 111, 29), 10)

        if paper4_flag:
            print("PAPER")
            os.system('START EXCEL.EXE')
            os.system('TASKKILL /IM POWERPNT.EXE')

    if exit_statement:
        for i in range(0, 21):
            cv.circle(img, (lm_list[i][1], lm_list[i][2]), 20, (255 , 255 , 0), -1)
        if exit_flag:
            print('EXIT')
            os.system('TASKKILL /IM WINWORD.EXE')
            os.system('TASKKILL /IM POWERPNT.EXE')
            os.system('TASKKILL /IM EXCEL.EXE')
            fist_flag = False
            scissors_flag = False
            paper4_flag = False
            exit_flag = False


    # cv.imshow("RPS", img)
    # cv.waitKey(1)