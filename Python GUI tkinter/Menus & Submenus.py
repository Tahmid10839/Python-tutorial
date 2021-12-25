from tkinter import *

def func():
    print("Menu and Submenu")

root = Tk()
root.geometry("600x500")
root.title("Menu & Submenu")

# this is used to create no dropdown menu

'''
mymenu = Menu(root)
mymenu.add_command(label="File",command=func)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)
'''

mainmenu = Menu(root)
submenu = Menu(mainmenu,tearoff=0)
submenu.add_command(label="New Project",command=func)
submenu.add_command(label="Save",command=func)
submenu.add_separator()
submenu.add_command(label="Save As",command=func)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=submenu)

submenu2 = Menu(mainmenu,tearoff=0)
submenu2.add_command(label="New Project1",command=func)
submenu2.add_command(label="Save1",command=func)
submenu2.add_separator()
submenu2.add_command(label="Save As1",command=func)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=submenu2)

root.mainloop()