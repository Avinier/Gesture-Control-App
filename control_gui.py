from tkinter import *

root = Tk()
root.geometry("1340x720")
root.title("Gesture Control App")
root.configure(bg="#ffb6c1")

# Title Section
title = Label(root, text="GESTURE CONTROLS APP", bg="#ffb6c1")
title.pack(pady=(50, 0))

# Camera Section
cam_frame = Frame(root, width=900, height=550, bg="#ffe4e1")
cam_frame.pack(side=LEFT, padx=(50, 0))

# Buttons Section
btn_frame = Frame(root, bg="#ffb6c1")
btn_frame.pack(side=RIGHT, padx=(0, 30))

def vol_toggle():
    vol_flag = True
    print("vol_flag")
    return vol_flag

def ges_toggle():
    gesture_flag = True
    print("gesture_flag")
    return gesture_flag
def rps_toggle():
    rps_flag = True
    print("rps_flag")
    return rps_flag

btn1 = Button(btn_frame, text="VOLUME CONTROL", padx=100, pady=30, command=vol_toggle)
btn2 = Button(btn_frame, text="APP RUNNER", padx=100, pady=30, command=ges_toggle)
btn3 = Button(btn_frame, text="ROCK-PAPER-SCISSORS", padx=100, pady=30, command=rps_toggle)

btn1.pack(fill=X, pady=(0, 80))
btn2.pack(fill=X, pady=(0, 80))
btn3.pack(fill=X)

# footer_frame = Frame(root)
# footer_frame.pack(side=BOTTOM)
footer = Label(btn_frame, text="Made by Aditya and Dhruv", bg="#ffb6c1")
footer.pack(pady=(50, 0))


root.mainloop()