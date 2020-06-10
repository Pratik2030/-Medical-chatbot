from tkinter import *
import sqlite3
import sys
import os
from PIL import ImageTk, Image
import cv2
root = Tk()
root.geometry('500x500')
root.title("CHATBOT")
root.configure(background="#FFFFFF")
root.resizable(0,0)

def run1():
    root.destroy()
    os.system('login.py')

def run2():
    root.destroy()
    os.system('signup.py')
label_01 = Label(root, text="MEDICAL CHATBOT",bg="#FFFFFF",fg='#ff8e06', width=30,font=("Sitka Text", 20, "bold"))
label_01.place(x=5,y=13)
label_11 = Label(root, text="MEDICAL CHATBOT WITH APPOINTMENT BOOKING SYSTEM",bg="#950740",fg="white",width=65,height=1,font=("bold", 10))
label_11.place(x=0,y=75)
Button(root, text='Login',width=20,bg='#f43130',fg='white',command=run1).place(x=100,y=410)
Button(root, text='Signup',width=20,bg='#f43130',fg='white',command=run2).place(x=250,y=410)
path = "ii7.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.config( width=500 )
panel.config( height=300 )
panel.config( anchor="center" )
panel.pack(side = "left",anchor="center")
root.mainloop()























