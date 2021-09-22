import cv2 as cv
import numpy as np
import hand_tracking_module as htm

import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

############################################-VOLUME CONTROL-#############################################
detector = htm.HandDetector(max_hands=2, detection_confidence=0.75)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

vol_range = volume.GetVolumeRange()
mid_vol = vol_range[0] + vol_range[1] / 2

# Setting minimum and maximum vol values to variables
min_vol = vol_range[0]
max_vol = vol_range[1]

def vol_control(img, lm_list):
        x1, y1 = lm_list[4][1], lm_list[4][2]
        x2, y2 = lm_list[8][1], lm_list[8][2]

        detector.draw_dots(img, x1, y1)
        detector.draw_dots(img, x2, y2)

        # Applying distance formula to index lm and thumb lm
        length = math.hypot(x2 - x1, y2 - y1)

        # Converting the length value to range of [30, 300] to [min_vol, max_vol]
        # (the values would be -65 and 0, so that volume can be toggled)
        vol = np.interp(length, [30, 300], [min_vol, max_vol])

        # Similar conversion
        vol_bar = np.interp(length, [30, 300], [500, 150])
        vol_per = np.interp(length, [30, 300], [0, 100])

        #Sets the volume to 'vol' when program is runned
        volume.SetMasterVolumeLevel(vol, None)

        detector.draw_lines(img, x1, y1, x2, y2, length)

        # Displaying the bar
        cv.rectangle(img, (50, 150), (100, 500), (100, 50, 200), 3)
        cv.rectangle(img, (50, int(vol_bar)), (100, 500), (100, 50, 200), -1)

        # Displaying percentage
        cv.putText(img, str(int(vol_per)) + " %", (50, 550), cv.FONT_HERSHEY_PLAIN, 2, (100, 50, 200), 2)
############################################-VOLUME CONTROL-#############################################



