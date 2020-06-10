from tkinter import *
import sqlite3
import os
import sys
from PIL import ImageTk, Image
import cv2
import pymysql
root = Tk()
root.geometry('480x500')
root.title("CHATBOT")
root.configure(background="#FFFFFF")
root.resizable(0,0)
label_0 = Label(root, text="MEDICAL CHATBOT",bg="#FFFFFF",fg='#ff8e06', width=23,font=("Sitka Text", 20, "bold"))
label_0.place(x=40,y=20)
def home():
   root.destroy()
   os.system('admin_home.py')
   
def logout():
   root.destroy()
   os.system('home.py')

def database():
   item1='x';
   item2='x';
   item3='x';
   item4='x';
   check=0
   db = pymysql.connect("localhost","root","root","chatbot" )
   print("check1")
   cursor = db.cursor()
   print("check2")
   sql = "SELECT * FROM chatbot.schedule" 
   try:
      print("check3")
      cursor.execute(sql)
      print("check4")
      
      result_set = cursor.fetchall()
      u=23
      s=90
      i=1;
      for row in result_set:
         name1=row[0]
         name2=row[1]
         name3=row[2]
         name4=row[3]
         label_4 = Label(root, text=name1,fg="#000000",bg="#FCCD04", width=13,font=("", 9))
         label_4.place(x=0,y=s+(u*i))
         label_5 = Label(root, text=name2,fg="#000000",bg="#FCCD04", width=17,font=("", 9))
         label_5.place(x=100,y=s+(u*i))
         label_6 = Label(root, text=name3,fg="#000000",bg="#FCCD04", width=17,font=("", 9))
         label_6.place(x=228,y=s+(u*i))
         label_7 = Label(root, text=name4,fg="#000000",bg="#FCCD04", width=17,font=("", 9))
         label_7.place(x=356,y=s+(u*i))
        
         i=i+1;
     
 
   except:
      db.rollback()

Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=65)
label_11 = Label(root, text="View Schedule",bg="#FCCD04",width=31,height=1,font=("bold", 10))
label_11.place(x=118,y=65)
Button(root, text='Logout',width=15,bg='#FCCD04',height=1,fg='black',command=logout).place(x=375,y=65)

label_1 = Label(root, text="Sl No",fg="#FFFFFF",bg="#950740", width=13,font=("bold", 9))
label_1.place(x=0,y=90)
label_2 = Label(root, text='Day',fg="#FFFFFF",bg="#950740", width=17,font=("bold", 9))
label_2.place(x=100,y=90)
label_3 = Label(root, text='Morning Time',fg="#FFFFFF",bg="#950740", width=17,font=("bold", 9))
label_3.place(x=228,y=90)
label_4 = Label(root, text='Evening Time',fg="#FFFFFF",bg="#950740", width=17,font=("bold", 9))
label_4.place(x=356,y=90)
database()
root.mainloop()

























