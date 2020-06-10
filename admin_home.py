from tkinter import *
import sqlite3
import sys
import os
from PIL import ImageTk, Image
import cv2
root = Tk()
root.geometry('600x500')
root.title("CHATBOT")
root.configure(background="#FFFFFF")
root.resizable(0,0)
uname=StringVar()
pwd=StringVar()
def run1():
    root.destroy()
    os.system('admin_home.py')

def run2():
    root.destroy()
    os.system('view_appointments.py')

def run3():
    root.destroy()
    os.system('add_schedule.py')
    
def run4():
    root.destroy()
    os.system('view_schedule.py')

def run5():
    root.destroy()
    os.system('home.py')
    
label_01 = Label(root, text="MEDICAL CHATBOT",bg="#FFFFFF",fg='#ff8e06', width=30,font=("Sitka Text", 20, "bold"))
label_01.place(x=35,y=13)
Button(root, text='HOME',width=17,bg='#950740',fg='white',command=run1).place(x=1,y=73)
Button(root, text='APPOINTMENTS',width=17,bg='#950740',fg='white',command=run2).place(x=127,y=73)
Button(root, text='ADD SCHEDULE',width=17,bg='#950740',fg='white',command=run3).place(x=255,y=73)
Button(root, text='VIEW SCHEDULE',width=17,bg='#950740',fg='white',command=run4).place(x=380,y=73)
Button(root, text='LOGOUT',width=17,bg='#950740',fg='white',command=run5).place(x=500,y=73)
path = "ii7.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img,bg="#AC3B61")
panel.config( width=600 )
panel.config( height=297 )
panel.config( anchor="center" )
panel.place(x=8,y=10)
panel.pack(side = "left",anchor="center")
root.mainloop()
























