from tkinter import *

root = Tk()
root.title("ScrollBar")
root.geometry("600x500")
# For Listbox
'''
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
lbx = Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    lbx.insert(END,f"Item {i}")

lbx.pack(fill="both")
scrollbar.config(command=lbx.yview)
'''
# For Text

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text = Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)

scrollbar.config(command=text.yview)
root.mainloop()