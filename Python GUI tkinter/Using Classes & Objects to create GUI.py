from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Classes & Objects")
        self.geometry("600x500")

    def statusbar(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvariable=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("You CLicked")

    def button(self,inptext):
        Button(self,text=inptext,command=self.click).pack()

if __name__ == '__main__':
    window = GUI()
    window.statusbar()
    window.button("Submit")
    window.mainloop()