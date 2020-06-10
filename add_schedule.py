from tkinter import *
import sqlite3
import os
import sys
import pymysql
root = Tk()
root.geometry('500x500')
root.title("CHATBOT")
root.configure(background="#FFFFFF")
sno=IntVar()
day=StringVar()
mtime=StringVar()
etime=StringVar()
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
   item1=day.get()
   item2=mtime.get()
   item3=etime.get()
   item4=sno.get()
   
   
   db = pymysql.connect("localhost","root","root","chatbot" )
   cursor = db.cursor()
   sql = "INSERT INTO chatbot.schedule VALUES ('%d','%s', '%s', '%s' )" % (item4,item1,item2,item3)
   try:
      cursor.execute(sql)
      db.commit()
   except:
      db.rollback()

   db.close()

   


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
label_1 = Label(root, text="Enter SL NO",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_1.place(x=80,y=140)
entry_1 = Entry(root,textvar=sno)
entry_1.place(x=240,y=140)
label_1 = Label(root, text="Enter Day",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_1.place(x=80,y=190)
entry_1 = Entry(root,textvar=day)
entry_1.place(x=240,y=190)
label_1 = Label(root, text="Enter Morning Time",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_1.place(x=80,y=235)
entry_1 = Entry(root,textvar=mtime)
entry_1.place(x=240,y=235)
label_1 = Label(root, text="Enter Evening Time",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_1.place(x=80,y=290)
entry_1 = Entry(root,textvar=etime)
entry_1.place(x=240,y=290)
Button(root, text='Submit',width=20,bg='#f43130',fg='white',command=database).place(x=180,y=350)
root.mainloop()























