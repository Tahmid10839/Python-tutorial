from tkinter import *

def hello():
    print("Hello World")

root = Tk()
root.geometry("600x700")

frame = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1 = Button(frame,fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT)
b2 = Button(frame,fg="red",text="Print Now")
b2.pack(side=LEFT,padx=23)
b3 = Button(frame,fg="red",text="Print Now")
b3.pack(side=LEFT)
b4 = Button(frame,fg="red",text="Print Now")
b4.pack(side=LEFT,padx=23)

root.mainloop()