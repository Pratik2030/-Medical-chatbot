from tkinter import *
import sqlite3
import os
import sys
import pymysql
root = Tk()
root.geometry('500x500')
root.title("CHATBOT")
root.configure(background="#FFFFFF")
fname=StringVar()
lname=StringVar()
mname=StringVar()
contact=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
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



def validate():
   if(fname.get()!="" and  lname.get()!="" and  Email.get()!="" and  uname.get()!="" and  pwd.get()!=""):
      if(uname.get()!=pwd.get()):
         #print(uname.get())
         #print(pwd.get())
         if len(pwd.get()) > 8:
            #print("Make sure your password is at lest 8 letters")
            if any(char.isupper() for char in pwd.get()):
               if any(char.isdigit() for char in pwd.get()):
                  if any(char.islower() for char in pwd.get()):
                     #call to storedata
                     database()
                  else:
                     popupmsg("password must have a small letter ")
               else:
                  popupmsg("password must have a digit ")
            else:
               popupmsg("password must have a capital letter")
         else:
            popupmsg("password length must > 9 ")
      else:
         popupmsg("uname & password can not be same ")
   else:
      popupmsg("any of the field can not be empty ")
   


def database():
   name1=fname.get()
   name2=lname.get()
   name3=mname.get()
   contact1=contact.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   uname1=uname.get()
   pwd1=pwd.get()
   gnd="x"
   db = pymysql.connect("localhost","root","root","chatbot" )
   cursor = db.cursor()

   if(gender==1):
      gnd="Male"
   else:
      gnd="Female"

   sql = "INSERT INTO chatbot.user(fname, mname, lname, contact, email, gender, uname, pwd, location) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )" % (name1,name3,name2,contact1,email,gnd,uname1,pwd1,country)
   try:
      cursor.execute(sql)
      db.commit()
   except:
      db.rollback()

   db.close()

   

def home():
   root.destroy()
   os.system('home.py')
   
def signup():
   root.destroy()
   os.system('signup.py')   
   
label_01 = Label(root, text="MEDICAL CHATBOT",bg="#FFFFFF",fg='#ff8e06', width=30,font=("Sitka Text", 20, "bold"))
label_01.place(x=5,y=13)
Button(root, text='Home',width=15,height=1,bg='#950740',fg='white',command=home).place(x=0,y=67)
label_11 = Label(root, text="User Registration Form",bg="#950740",fg='white',width=33,height=1,font=("bold", 10))
label_11.place(x=118,y=67)
Button(root, text='Signup',width=15,bg='#950740',height=1,fg='white',command=signup).place(x=391,y=67)
label_1 = Label(root, text="First Name",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_1.place(x=80,y=120)
entry_1 = Entry(root,textvar=fname)
entry_1.place(x=240,y=120)
label_1 = Label(root, text="Middle Name",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_1.place(x=80,y=155)
entry_1 = Entry(root,textvar=mname)
entry_1.place(x=240,y=155)
label_1 = Label(root, text="Last Name",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_1.place(x=80,y=190)
entry_1 = Entry(root,textvar=lname)
entry_1.place(x=240,y=190)
label_1 = Label(root, text="Contact",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_1.place(x=80,y=230)
entry_1 = Entry(root,textvar=contact)
entry_1.place(x=240,y=230)
label_2 = Label(root, text="Email",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_2.place(x=68,y=270)
entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=270)
label_3 = Label(root, text="Gender",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_3.place(x=70,y=310)
Radiobutton(root, text="Male",padx = 5,bg="#FFFFFF",fg="#000000", variable=var, value=1).place(x=235,y=310)
Radiobutton(root, text="Female",padx = 20,bg="#FFFFFF",fg="#000000", variable=var, value=2).place(x=290,y=310)
label_4 = Label(root, text="City",bg="#FFFFFF",fg="#000000",width=20,font=("bold", 10))
label_4.place(x=70,y=350)
list1 = ['Mumbai','Pune','Nagpur','Aurangabad','Nashik','Satara'];
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your city') 
droplist.place(x=240,y=350)
label_22 = Label(root, text="Username",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_22.place(x=80,y=390)
entry_22 = Entry(root,textvar=uname)
entry_22.place(x=240,y=390)
label_33 = Label(root, text="Password",width=20,bg="#FFFFFF",fg="#000000",font=("bold", 10))
label_33.place(x=80,y=430)
entry_33 = Entry(root,textvar=pwd)
entry_33.place(x=240,y=430)
Button(root, text='Submit',width=20,bg='#f43130',fg='white',command=validate).place(x=180,y=460)
root.mainloop()























