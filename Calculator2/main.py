import math as m
from tkinter import *
from tkinter.messagebox import *
import pyttsx3
import threading

class PlayAudio:
    def __init__(self,voice="female",speakstatus=True):
        self.voice = "female"
        self.speakstatus = speakstatus
        self.speakwords = {
            '0':'zero',
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four',
            '5':'five',
            '6':'six',
            '7':'seven',
            '8':'eight',
            '9':'nine',
            '+':'plus',
            '-':'minus',
            'X':'multiply',
            '/':'divide',
            '.':'dot',
            '=':'equal to',
            'torad':'Radian',
            'todeg':'Degree',
            '√':'square root',
            'x!':'factorial',
            'sinθ':'sine',
            'cosθ':'cos',
            'tanθ':'tan',
            '^':'power'

        }
        self.engine = pyttsx3.init()
        v = self.engine.getProperty('voices')
        self.engine.setProperty('voice',v[1].id)

    def speak(self,content):
        if self.speakstatus==True:
            self.engine.say(self.speakwords[content])
            self.engine.runAndWait()

ob = PlayAudio()
audio = False
def audio_click():
   global audio
   audio = True

# Some useful variables
font = ("Verdana",22,"bold underline")
font2 = ("Verdana",20,"bold")

# Some Functions
def clicked(event):
    b = event.widget
    text = b["text"]
    if audio == True:
        t = threading.Thread(target=ob.speak,args=(text,))
        t.start()
    if text == "X":
        textfield.insert(END,"*")
        return

    if text == "=":
        try:
            ex = textfield.get()
            ans = eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,ans)
        except Exception as e:
            showerror("Error",e)
        return
    if text == "<--":
        ex = textfield.get()
        ex = ex[0:len(ex)-1]
        textfield.delete(0,END)
        textfield.insert(0,ex)
        return
    if text == "AC":
        textfield.delete(0,END)
        return

    textfield.insert(END,text)


# Creating a window
window = Tk()
window.title("My Calculator")
window.geometry("460x550")
#window.wm_iconbitmap("img/cal1.png")

# Photo Label
pic = PhotoImage(file="img/cal2.png")
photolabel = Label(window, image=pic)
photolabel.pack(pady=15)

# Heading Label
headlabel = Label(window,text="My Calculator",font=font)
headlabel.pack(pady=10)

# TextField
textfield = Entry(window,font=font2,justify=RIGHT)
textfield.pack(padx=10,pady=10,fill=X)

# Buttons
buttonframe = Frame(window)
buttonframe.pack()

# Adding Buttons

clearbtn = Button(buttonframe, text="<--", font=font2,width=11,relief=RIDGE,activebackground="blue",activeforeground="white")
clearbtn.grid(row=4, column=0,columnspan=2,padx=5,pady=5)

allclearbtn = Button(buttonframe, text="AC", font=font2,width=11,relief=RIDGE,activebackground="blue",activeforeground="white")
allclearbtn.grid(row=4, column=2,columnspan=2,padx=5,pady=5)


temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonframe, text=str(temp), font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
        btn.grid(row=i, column=j,padx=5,pady=5)
        temp += 1
        btn.bind("<Button-1>",clicked)

zerobtn = Button(buttonframe, text="0", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
zerobtn.grid(row=3, column=0,padx=5,pady=5)

dotbtn = Button(buttonframe, text=".", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
dotbtn.grid(row=3, column=1,padx=5,pady=5)

equalbtn = Button(buttonframe, text="=", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
equalbtn.grid(row=3, column=2,padx=5,pady=5)

plusbtn = Button(buttonframe, text="+", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
plusbtn.grid(row=0, column=3,padx=5,pady=5)

minusbtn = Button(buttonframe, text="-", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
minusbtn.grid(row=1, column=3,padx=5,pady=5)

multiplybtn = Button(buttonframe, text="X", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
multiplybtn.grid(row=2, column=3,padx=5,pady=5)

dividebtn = Button(buttonframe, text="/", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
dividebtn.grid(row=3, column=3,padx=5,pady=5)

# Binding all buttons

zerobtn.bind("<Button-1>",clicked)
dotbtn.bind("<Button-1>",clicked)
plusbtn.bind("<Button-1>",clicked)
minusbtn.bind("<Button-1>",clicked)
multiplybtn.bind("<Button-1>",clicked)
dividebtn.bind("<Button-1>",clicked)
equalbtn.bind("<Button-1>",clicked)
clearbtn.bind("<Button-1>",clicked)
allclearbtn.bind("<Button-1>",clicked)

# Scientific Calculator

scframe = Frame(window)


sqrtbtn = Button(scframe, text="√", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
sqrtbtn.grid(row=0, column=0,padx=5,pady=5)

powbtn = Button(scframe, text="^", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
powbtn.grid(row=0, column=1,padx=5,pady=5)

factbtn = Button(scframe, text="x!", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
factbtn.grid(row=0, column=2,padx=5,pady=5)

radbtn = Button(scframe, text="torad", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
radbtn.grid(row=0, column=3,padx=5,pady=5)

degbtn = Button(scframe, text="todeg", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
degbtn.grid(row=1, column=0,padx=5,pady=5)

sinbtn = Button(scframe, text="sinθ", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
sinbtn.grid(row=1, column=1,padx=5,pady=5)

cosbtn = Button(scframe, text="cosθ", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
cosbtn.grid(row=1, column=2,padx=5,pady=5)

tanbtn = Button(scframe, text="tanθ", font=font2,width=5,relief=RIDGE,activebackground="blue",activeforeground="white")
tanbtn.grid(row=1, column=3,padx=5,pady=5)

# Functions

def enterclick(event):
    e = Event()
    e.widget = equalbtn
    clicked(e)

textfield.bind("<Return>",enterclick)

def normal_calc():
    scframe.pack_forget()
    window.geometry("460x550")
    global audio
    audio = False

def sc_click():
    buttonframe.pack_forget()
    scframe.pack()
    buttonframe.pack()
    window.geometry("460x690")
    global audio
    audio = False

def calculate_sc(event):
    btn = event.widget
    text= btn["text"]
    ans = ""
    ex = textfield.get()
    if audio == True:
        t = threading.Thread(target=ob.speak,args=(text,))
        t.start()

    if text == "torad":
        ans = str(m.radians(float(ex)))
    elif text=="todeg":
        ans = str(m.degrees(float(ex)))
    elif text == "x!":
        ans = str(m.factorial(int(ex)))
    elif text == "sinθ":
        ans = str(m.sin(m.radians(float(ex))))
    elif text == "cosθ":
        ans = str(m.cos(m.radians(float(ex))))
    elif text == "tanθ":
        ans = str(m.tan(m.radians(float(ex))))
    elif text == "√":
        ans = str(m.sqrt(int(ex)))
    elif text == "^":
        base,pow = ex.split(",")
        ans = str(m.pow(int(base),int(pow)))
    textfield.delete(0,END)
    textfield.insert(0,ans)

# Binding sc buttons
sqrtbtn.bind("<Button-1>",calculate_sc)
radbtn.bind("<Button-1>",calculate_sc)
degbtn.bind("<Button-1>",calculate_sc)
factbtn.bind("<Button-1>",calculate_sc)
sinbtn.bind("<Button-1>",calculate_sc)
cosbtn.bind("<Button-1>",calculate_sc)
tanbtn.bind("<Button-1>",calculate_sc)
powbtn.bind("<Button-1>",calculate_sc)



# Menus

menubar = Menu(window)
mode = Menu(menubar,tearoff=0)
mode.add_radiobutton(label="Normal Calculator",command=normal_calc)
mode.add_radiobutton(label="Scientific Calculator",command=sc_click)
mode.add_radiobutton(label="Audio",command=audio_click)
menubar.add_cascade(label="Mode",menu=mode)
window.config(menu=menubar)

window.mainloop()