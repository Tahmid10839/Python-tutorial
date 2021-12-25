from tkinter import *

root = Tk()
root.geometry("600x700")
root.title("Tahmid GUI")

# Important Label Options
'''
text = add the text
bg = background
fg = foreground
font = sets the font
1. font = ("comicsansms",19,"bold")
2. font="comicsansms 19 bold"
padx = x padding
pady = y padding
relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE
'''

text_label = Label(text="This is about Rahim.\nHe is a student.He reads CSE at DIU", bg="blue", fg="white", padx=50, pady=60, font="comicsansms 19 bold", borderwidth=10, relief=RIDGE)

# Important Pack Options
'''
anchor = nw, ne, se, sw
side = BOTTOM, TOP, LEFT, RIGHT
fill = X, Y
padx
pady

'''

text_label.pack(side=BOTTOM, anchor="sw", fill=X, padx=45,pady=50)


root. mainloop()