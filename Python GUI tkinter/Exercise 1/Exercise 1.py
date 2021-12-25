
# Reading Newspaper

from tkinter import *
from PIL import Image,ImageTk
from datetime import *

root = Tk()
root.title("Newspaper")
root.geometry("1280x720")

def every_100(text):
    final_text = ""
    for i in range(0,len(text)):
        final_text += text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text
texts = []
photos= []
for i in range(0,2):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.jpg")
    # Resize Images
    image = image.resize((250,300),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,width=500,height=400)
Label(f0, text="News", font="lucida 25 bold").pack()
Label(f0, text="Date: "+str(date.today()), font="lucida 20 bold").pack()
f0.pack()

for i in range(0,2):
    f1 = Frame(root, width=500, height=200,padx=100,pady=20)
    Label(f1, text=texts[i], font="lucida 10",padx=50).pack(side="right")
    Label(f1, image=photos[i]).pack()
    f1.pack(anchor="w")

root.mainloop()
