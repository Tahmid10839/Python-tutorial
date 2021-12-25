from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order Received",f"We have received your order for {var.get()}.Thanks for ordering.")

root = Tk()
root.title("RadioButtons")
root.geometry("600x500")

var = StringVar()
var.set("Apple")
Label(root,text="What would you like to have you sir?",font="lucida 19 bold").pack()
radio = Radiobutton(root,text="Burger",variable=var,value="Burger",font="lucida 10 bold").pack(anchor="w")
radio2 = Radiobutton(root,text="Sandwich",variable=var,value="Sandwich",font="lucida 10 bold").pack(anchor="w")
Button(root,text="Order Now",command=order).pack()

root.mainloop()