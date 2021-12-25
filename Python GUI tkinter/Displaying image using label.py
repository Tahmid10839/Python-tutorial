from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("600x700")
#photo = PhotoImage(file="1.png")

#For JPG images
image = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image)
photo_label = Label(image=photo)
photo_label.pack()

root.mainloop()