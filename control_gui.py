from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import main_control as msc

root = Tk()
root.geometry('950x550')
root.title('Gesture Application')
root['bg'] = "#2c3647"

primary_col = "#2c3647"
secondary_col = "#4286f4"

# Button Functions
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


def vol_inactive(event):
    VolBut.config(image=volBut_img)

def app_inactive(event):
    AppBut.config(image=appBut_img)

def rps_inactive(event):
    RpsBut.config(image=rpsBut_img)


def vol_active(event):
    VolBut.config(image=volBut_img_active)

def app_active(event):
    AppBut.config(image=appBut_img_active)

def rps_active(event):
    RpsBut.config(image=rpsBut_img_active)


# Title Frame
frame1 = Frame(root, bg=primary_col)
frame1.pack()

GesRog = Label(frame1, text='Gesture Recognition App', bg=primary_col, fg='#FFF')
GesRog['font'] = font.Font(family='Product Sans', size=30)
GesRog.grid(row=0, column=1, padx=10, pady=(15, 30))

# Content Frame
frame2 = Frame(root, bg=primary_col)
frame2.pack()

Cirleimg = Image.open('mode-logos/volumecontrol_logo.png')
Cirleimg = Cirleimg.resize((150, 150))
CircleImageTK = ImageTk.PhotoImage(Cirleimg)
CirleLabel1 = Label(frame2, image=CircleImageTK, bg=primary_col)
CirleLabel1.image = CircleImageTK
CirleLabel1.grid(row=1, column=0, padx=50)

Cirleimg = Image.open('mode-logos/appopener_logo.png')
Cirleimg = Cirleimg.resize((150, 150))
CircleImageTK = ImageTk.PhotoImage(Cirleimg)
CirleLabel2 = Label(frame2, image=CircleImageTK, bg=primary_col)
CirleLabel2.image = CircleImageTK
CirleLabel2.grid(row=1, column=1, padx=50)

Cirleimg = Image.open('mode-logos/rps_logo.png')
Cirleimg = Cirleimg.resize((150, 150))
CircleImageTK = ImageTk.PhotoImage(Cirleimg)
CirleLabel3 = Label(frame2, image=CircleImageTK, bg=primary_col)
CirleLabel3.image = CircleImageTK
CirleLabel3.grid(row=1, column=2, padx=50)


VolCon = Label(frame2, text='Volume Control', bg=primary_col, fg='#FFF')
VolCon['font'] = font.Font(family='Open Sans Bold', size=15, slant='roman')
VolCon.grid(row=2, column=0, pady=(5, 10))

AppCon = Label(frame2, text='App Control', bg=primary_col, fg='#FFF')
AppCon['font'] = font.Font(family='Open Sans Bold', size=15)
AppCon.grid(row=2, column=1, pady=(5, 10))

RpsCon = Label(frame2, text='RPS Control', bg=primary_col, fg='#FFF')
RpsCon['font'] = font.Font(family='Open Sans Bold', size=15)
RpsCon.grid(row=2, column=2, pady=(5, 10))

VolConBox = Text(frame2, width=24, height=6, bg="#222", fg="#fff", bd=0)
VolConBox.insert('end', ' This mode tracks the hands     and changes the volume     based on specific gestures.')
VolConBox.insert('end', '                                                   ')
VolConBox.insert('end', '     Hand-tracking achieved by     OpenCV and Mediapipe.')
VolConBox['state'] = DISABLED
VolConBox['font'] = font.Font(family='Open Sans', size=10)
VolConBox.grid(row=3, column=0, pady=(0,15))

AppConBox = Text(frame2, width=24, height=6, bg="#222", fg="#fff", bd=0)
AppConBox.insert('end', '   This mode opens specific       apps on invoking certain           hand gestures only.')
AppConBox.insert('end', '                                                   ')
AppConBox.insert('end', '                Powerpoint | Word | Excel       | OneNote | Outlook')

AppConBox['state'] = DISABLED
AppConBox['font'] = font.Font(family='Open Sans', size=10)
AppConBox.grid(row=3, column=1, pady=(0,15))

RpsConBox = Text(frame2, width=24, height=6, bg="#222", fg="#fff", bd=0)
RpsConBox.insert('end', 'Open and close applications    using symbols of   Rock,                 Paper & Scissors')
RpsConBox.insert('end', '                                                   ')
RpsConBox.insert('end', '                      Spotify | Brave | Teams')
RpsConBox['state'] = DISABLED
RpsConBox['font'] = font.Font(family='Open Sans', size=10)
RpsConBox.grid(row=3, column=2, pady=(0, 15))

VolBut_img = Image.open("btn-imgs/volcontrol_logo.png")
volBut_img = VolBut_img.resize((150, 40))
volBut_img = ImageTk.PhotoImage(volBut_img)

VolBut_img_active = Image.open("btn-imgs/volcontrol_active.png")
volBut_img_active = VolBut_img_active.resize((150, 40))
volBut_img_active = ImageTk.PhotoImage(volBut_img_active)

VolBut = Button(frame2, image=volBut_img, bg=primary_col, bd=0, activebackground=primary_col, command=vol_toggle)
VolBut.grid(row=4, column=0, pady=10)

AppBut_img = Image.open("btn-imgs/app-opener_logo.png")
appBut_img = AppBut_img.resize((150, 40))
appBut_img = ImageTk.PhotoImage(appBut_img)

AppBut_img_active = Image.open("btn-imgs/appopener_active.png")
appBut_img_active = AppBut_img_active.resize((150, 40))
appBut_img_active = ImageTk.PhotoImage(appBut_img_active)

AppBut = Button(frame2, image=appBut_img, bg=primary_col, bd=0, activebackground=primary_col, command=ges_toggle)
AppBut.grid(row=4, column=1, pady=10)

RpsBut_img = Image.open("btn-imgs/rpscontrol_logo.png")
rpsBut_img = RpsBut_img.resize((150, 40))
rpsBut_img = ImageTk.PhotoImage(rpsBut_img)

RpsBut_img_active = Image.open("btn-imgs/rpscontrol_active.png")
rpsBut_img_active = RpsBut_img_active.resize((150, 40))
rpsBut_img_active = ImageTk.PhotoImage(rpsBut_img_active)

RpsBut = Button(frame2, image=rpsBut_img, bg=primary_col, bd=0, activebackground=primary_col, command=rps_toggle)
RpsBut.grid(row=4, column=2, pady=10)

VolBut.bind("<Enter>", vol_active)
AppBut.bind("<Enter>", app_active)
RpsBut.bind("<Enter>", rps_active)

VolBut.bind("<Leave>", vol_inactive)
AppBut.bind("<Leave>", app_inactive)
RpsBut.bind("<Leave>", rps_inactive)

MadeBy = Label(root, text="Made by Aditya and Dhruv", bg=primary_col)
MadeBy['font'] = font.Font(family='Product Sans', size=13)
MadeBy.pack(pady=(15,0))

root.mainloop()