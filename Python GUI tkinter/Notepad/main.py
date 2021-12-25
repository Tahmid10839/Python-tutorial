from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file= None
    textarea.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0,END)
        f = open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])

        if file=="":
            file = None
        else:
            # Save as a new file
            f = open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()
def quitapp():
    root.destroy()


def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Tahmid")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("600x500")

    # Add textarea
    textarea = Text(root,font="lucida 13")
    file = None
    textarea.pack(expand=True,fill=BOTH)

    # Create a menubar
    menubar = Menu(root)

    # Filemenu starts
    filemenu = Menu(menubar,tearoff=0)
    # To open a new file
    filemenu.add_command(label="New",command=newfile)

    # To open already existed file
    filemenu.add_command(label="Open",command=openfile)

    # To save the current file
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quitapp)
    menubar.add_cascade(label="File",menu=filemenu)
    # Filemenu Ends

    # Edit menu Starts
    editmenu = Menu(menubar,tearoff=0)

    # To give a feature of cut,copy & paste
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    menubar.add_cascade(label="Edit",menu=editmenu)

    # Edit menu Ends

    # Help Menu Starts
    helpmenu = Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)
    # Help menu Ends

    root.config(menu=menubar)

    # Adding Scrollbar
    scrollbary = Scrollbar(textarea)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbary.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbary.set)

    scrollbarx = Scrollbar(textarea,orient=HORIZONTAL)
    scrollbarx.pack(side=BOTTOM,fill=X)
    scrollbarx.config(command=textarea.xview)
    textarea.config(xscrollcommand=scrollbarx.set,wrap="none")

    root.mainloop()