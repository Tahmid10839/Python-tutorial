from tkinter import *

def getval():
    print(f"{nameval.get(),phoneval.get(),genderval.get(),paymentval.get(),serviceval.get()}")
    with open("records.txt","a") as f:
        f.write(f"{nameval.get(),phoneval.get(),genderval.get(),paymentval.get(),serviceval.get()}\n")

root = Tk()
root.geometry("600x500")

Label(root,text="Welcome to Travel Form",font="comicsanms 13 bold",pady=15).grid(row=0,column=1)
Label(root,text="Name:").grid(row=1,column=0)
Label(root,text="Phone:").grid(row=2,column=0)
Label(root,text="Gender:").grid(row=3,column=0)
Label(root,text="Payment Mode:").grid(row=4,column=0)

nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
paymentval = StringVar()
serviceval = IntVar()

Entry(root,textvariable=nameval).grid(row=1,column=1)
Entry(root,textvariable=phoneval).grid(row=2,column=1)
Entry(root,textvariable=genderval).grid(row=3,column=1)
Entry(root,textvariable=paymentval).grid(row=4,column=1)

# CheckButtons
Checkbutton(text="Want to prebook your meals?",variable=serviceval).grid(row=5,column=1)

# Buttons
Button(text="Submit",command=getval).grid(row=6,column=1)

root.mainloop()