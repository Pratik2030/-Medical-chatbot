from tkinter import *
import sqlite3
import os
import sys
import cv2
import pymysql
from PIL import ImageTk, Image
root = Tk()
root.geometry('500x500')
root.title("CHATBOT")
root.configure(background="#FFFFFF")
root.resizable(0,0)
uname=StringVar()
pwd=StringVar()



def popupmsg(msg):
   popup=Tk()
   popup.wm_title("!")
   popup.resizable(0,0)
   label=Label(popup,text=msg,width=30,font=("bold", 10))
   label.pack(side="top",fill="x",pady=10)
   B1=Button(popup,text="OK",command=popup.destroy)
   B1.pack()
   popup.mainloop()

def database():
   name1=uname.get()
   name2=pwd.get()
   check=0
   db = pymysql.connect("localhost","root","root","chatbot" )
   print("check1")
   cursor = db.cursor()
   print("check2")
   sql = "SELECT uname FROM chatbot.user WHERE uname='"+name1+"' AND pwd='"+name2+"'" 
   try:
      print("check3")
      cursor.execute(sql)
      print("check4")
      result_set = cursor.fetchall()
      print("check5")

      for row in result_set:
        print(row)
        check=check+1
      
   except:
      db.rollback()

   if(check==0):
      popupmsg("Login Not Successful ")
   if(check==1):
      print("****************Login  successfull")
      root.destroy()
      os.system('admin_home.py')

   db.close()


def forgotpwd():
   root.destroy()
   os.system('forgot_pwd.py')

def home():
   root.destroy()
   os.system('home.py')
   
def signup():
   root.destroy()
   os.system('signup.py')
  

label_01 = Label(root, text="MEDICAL CHATBOT",bg="#FFFFFF",fg='#ff8e06', width=30,font=("Sitka Text", 20, "bold"))
label_01.place(x=5,y=13)
Button(root, text='Home',width=15,height=1,bg='#950740',fg='white',command=home).place(x=0,y=67)
label_11 = Label(root, text="User Login Form",bg="#950740",fg='white',width=33,height=1,font=("bold", 10))
label_11.place(x=118,y=67)
Button(root, text='Signup',width=15,bg='#950740',height=1,fg='white',command=signup).place(x=391,y=67)
label_0 = Label(root, text="Login Form",bg="#AC3B61",fg="#FFFFFF", width=20,font=("bold", 12))
label_0.place(x=130,y=381)
label_1 = Label(root, text="UserName",bg="#FFFFFF",fg="#000000",width=20,font=("bold", 10))
label_1.place(x=100,y=410)
entry_1 = Entry(root,textvar=uname)
entry_1.place(x=240,y=410)
label_2 = Label(root, text="Password",bg="#FFFFFF",fg="#000000",width=20,font=("bold", 10))
label_2.place(x=100,y=440)
entry_2 = Entry(root,textvar=pwd)
entry_2.place(x=240,y=440)
Button(root, text='Submit',width=20,bg='#f43130',fg='white',command=database).place(x=190,y=470)
path = "ii7.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img,bg="#AC3B61")
panel.config( width=500 )
panel.config( height=310 )
panel.config( anchor="center" )
panel.place(x=8,y=10)
panel.pack(side = "left",anchor="center")
root.mainloop()























