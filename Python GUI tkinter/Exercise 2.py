
# Create a GUI window which takes as input width and height
# and upon clicking apply, it should be able to change its size accordingly

from tkinter import *

def update():
    print("Updating GUI")
    root.geometry(f"{width.get()}x{height.get()}")

root = Tk()

root.title("Width and Height")
root.geometry("600x400")

Label(root,text="Width:").grid(row=0,column=0)
Label(root,text="Height:").grid(row=1,column=0)

width = StringVar()
height = StringVar()

Entry(root,textvariable=width).grid(row=0,column=1)
Entry(root,textvariable=height).grid(row=1,column=1)

Button(root,text="Apply",command=update).grid(row=2,column=1)

root.mainloop()