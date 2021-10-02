from tkinter import *
# from mttkinter import mtTkinter
# import threading
import main_control as msc


root = Tk()
root.geometry("1340x720")
root.title("Gesture Control App")
root.configure(bg="#ffb6c1")

# Title Sectiontitle = Label(root, text="GESTURE CONTROLS APP", bg="#ffb6c1")
title.pack(pady=(50, 0))

# Camera Section
cam_frame = Frame(root, width=900, height=550, bg="#ffe4e1")
cam_frame.pack(side=LEFT, padx=(50, 0))

# Buttons Section
btn_frame = Frame(root, bg="#ffb6c1")
btn_frame.pack(side=RIGHT, padx=(0, 30))

# def run_main(event):
#     msc.main()

def vol_toggle():
    msc.set_volflag(True)
    msc.set_gestureflag(False)
    msc.set_rpsflag(False)
    msc.main()
    print("----Volume Toggle Over----")

def ges_toggle():
    msc.set_volflag(False)
    msc.set_gestureflag(True)
    msc.set_rpsflag(False)
    msc.main()
    print("----Gesture Toggle Over----")

def rps_toggle():
    msc.set_volflag(False)
    msc.set_gestureflag(False)
    msc.set_rpsflag(True)
    msc.main()
    print("----RPS Toggle Over----")

btn1 = Button(btn_frame, text="VOLUME CONTROL", padx=100, pady=30, command=vol_toggle)
btn2 = Button(btn_frame, text="APP RUNNER", padx=100, pady=30, command=ges_toggle)
btn3 = Button(btn_frame, text="ROCK-PAPER-SCISSORS", padx=100, pady=30, command=rps_toggle)

# btn1.bind("<Button-1>", run_main)
# btn2.bind("<Button-1>", run_main)
# btn3.bind("<Button-1>", run_main)

btn1.pack(fill=X, pady=(0, 80))
btn2.pack(fill=X, pady=(0, 80))
btn3.pack(fill=X)

# footer_frame = Frame(root)
# footer_frame.pack(side=BOTTOM)
footer = Label(btn_frame, text="Made by Aditya and Dhruv", bg="#ffb6c1")
footer.pack(pady=(50, 0))

# def run():
root.mainloop()

# run()