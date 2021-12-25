from tkinter import *

def getval():
    print(f"User Name: {userval.get()}")
    print(f"Password: {passval.get()}")

root = Tk()
root.geometry("600x700")
user = Label(root,text="Username")
password = Label(root,text="Password")
user.grid()
password.grid()
# Variable classes in tkinter
# Booleanvar, Doublevar, Intvar, Stringvar
userval = StringVar()
passval = StringVar()

userentry = Entry(root, textvariable=userval)
passentry = Entry(root, textvariable=passval)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getval).grid(column=1)
root.mainloop()