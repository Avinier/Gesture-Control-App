import cv2 as cv
import mediapipe as mp
import time


class HandDetector():
    # Base constructor with fine-tuning variables
    def __init__(self, mode=False, max_hands=1, detection_confidence=0.75, tracking_confidence=0.75):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.detection_confidence, self.tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    # Function to detect hands
    def detect_hands(self, img, landmarks=True):
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if landmarks:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return img

    # Function to find co-ordinates of lms and draw dots over lms
    def position_hands(self, img, hand_num=0, dots=True):
        lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_num]
            for id, lm in enumerate(my_hand.landmark):
                height, width, channels = img.shape
                x, y = int(lm.x * width), int(lm.y * height)
                lm_list.append([id, x, y])
                if dots:
                    cv.circle(img, (x, y), 10, (200, 0, 250), -1)

        return lm_list

    # Draw dots over specified lms
    def draw_dots(self, img, x, y):
        cv.circle(img, (x, y), 15, (200, 0, 250), -1)

    # Drawing lines connecting specified landmarks and color changing dots
    def draw_lines(self, img, x1, y1, x2, y2, length):
        cv.line(img, (x1, y1), (x2, y2), (200, 0, 250), 3)
        cx, cy = (x1+x2) // 2, (y1+y2) // 2
        cv.circle(img, (cx, cy), 15, (200, 100, 250), -1)

        if length < 50:
            cv.circle(img, (cx, cy), 15, (50, 200, 100), -1)
        elif length >= 300:
            cv.circle(img, (cx, cy), 15, (50, 50, 250), -1)


# Dummy code
def main():
    vid = cv.VideoCapture(0)
    current_time = 0
    prev_time = 0
    detector = HandDetector()
    while True:
        success, img = vid.read()
        img = detector.detect_hands(img)
        lm_list = detector.position_hands(img)
        if len(lm_list) != 0:
            print(lm_list[4])
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        cv.putText(img, str(int(fps)) + " fps", (10, 70), cv.FONT_HERSHEY_PLAIN, 2, (100, 50, 200), 3)
        cv.imshow("Image", img)
        cv.waitKey(1)

if __name__ == "__main__":
    main()
