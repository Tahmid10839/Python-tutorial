from tkinter import *

def tahmid(event):
    print(f"You clicked on the button at {event.x},{event.y}")

root = Tk()
root.title("Tahmid")
root.geometry("600x700")
widget = Button(root,text="Please click")
widget.pack()
widget.bind("<Button-1>",tahmid)
widget.bind("<Double-1>",quit)

root.mainloop()