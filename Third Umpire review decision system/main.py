import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import imutils
import time

# Set width and height
SET_WIDTH = 650
SET_HEIGHT = 368

stream = cv2.VideoCapture("clip.mp4")
flag = True

def play(speed):
    # print(f"You clicked on play.Speed is {speed}")
    global flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if grabbed:
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    if flag:
        canvas.create_text(132,26,fill="black",font="Times 26 bold",text="Decision Pending")
    flag = False

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor = tkinter.NW)

    # 2. Wait for 1 second
    time.sleep(1)

    # 3. Display Sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4. wait for 1.5 second
    time.sleep(1.5)
    # 5. Display out/not out image
    if decision=="Out":
        decisionimg = "out.png"
    else:
        decisionimg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionimg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending,args=("Out",))
    thread.daemon = 1
    thread.start()

def not_out():
    thread = threading.Thread(target=pending,args=("Not Out",))
    thread.daemon = 1
    thread.start()

#tkinter GUI starts here
window = tkinter.Tk()
window.title("Third umpire decision review system")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas.pack()

#Buttons to control playback
btn = tkinter.Button(window,text="<< Previous (Fast)",width=50,command=partial(play,-25))
btn.pack()
btn = tkinter.Button(window,text="<< Previous (Slow)",width=50,command=partial(play,-2))
btn.pack()
btn = tkinter.Button(window,text=">> Next (Fast)",width=50,command=partial(play,25))
btn.pack()
btn = tkinter.Button(window,text=">> Next (Slow)",width=50,command=partial(play,2))
btn.pack()
btn = tkinter.Button(window,text="Give Out",width=50,command=out)
btn.pack()
btn = tkinter.Button(window,text="Give Not Out",width=50,command=not_out)
btn.pack()
window.mainloop()