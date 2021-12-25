from tkinter import *
import tkinter.messagebox as tmsg

def getdollars():
    tmsg.showinfo("Dollars",f"We have credited {myslider2.get()} dollars to your account")

root = Tk()
root.title("Slider")
root.geometry("600x500")

# Vertical Slider
#myslider = Scale(root, from_=0,to=100)
#myslider.pack()

Label(root,text="How many dollars do you want?").pack()
myslider2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(20)
myslider2.pack()
Button(root,text="Get Dollars",command=getdollars).pack()


root.mainloop()