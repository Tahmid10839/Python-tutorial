from tkinter import *

root = Tk()
root.geometry("600x500")

f1 = Frame(root,bg="grey",borderwidth=20,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
l1 = Label(f1,text="Pycharm",fg="blue")
l1.pack(pady=200)

f2 = Frame(root,bg="grey",borderwidth=20,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l2 = Label(f2,text="Sublime Text",fg="red",font="Helvetica 19 bold")
l2.pack()

root.mainloop()