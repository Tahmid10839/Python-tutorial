from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i +=1

i = 0
root = Tk()
root.title("ListBox")
root.geometry("600x500")

lbx = Listbox(root)
lbx.insert(END,"First item is inserted")
lbx.pack()
Button(root,text="Add Item",command=add).pack()

root.mainloop()