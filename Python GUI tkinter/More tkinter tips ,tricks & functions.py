from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tips & Tricks")
        self.geometry("600x500")
        self.wm_iconbitmap("3.png")
        self.configure(background="grey")
    def screen(self):
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        print(f"{self.width}X{self.height}")

    def button(self):
        Button(text="Close",command=self.destroy).pack()



if __name__ == '__main__':
    root = GUI()
    root.screen()
    root.button()
    root.mainloop()