import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

#outer boby
root = tkinter.Tk()
root.geometry('550x400')
root.resizable(0,0)
root.title('Library_Management_System')
root.configure(background ='black')

#variables
Usn = StringVar()
Pwd = StringVar()
Bat = StringVar()
BookName = StringVar()
Writer = StringVar()
StuName = StringVar()
StuPwd = StringVar()
Batch = StringVar()
Usnn = StringVar()
Pwdd = StringVar()

#Values
Usnn = "admin"
Pwdd = "admin"
#Fuctions

def allfield():
    messagebox.showinfo('Error','All field are requered')

def check1():
    messagebox.showinfo('U Rock It','login successful')

def check2():
    messagebox.showinfo('LOL','Unsuccessful')

#popup window
def login():
    #if(Usn==Usnn and Pwd==Pwdd):
        B3 = Button(root, text='Access',width=15,bg='black',fg='green', command=access)
        B3.place(x=250,y=260)
        check1()
    #else:
       # check2()





def NewUser():
    root3 = tkinter.Tk()
    root3.geometry('300x300')
    root3.resizable(0,0)
    root3.configure(background = 'black')
    root3.title('New_User')
    #label
    l4 = Label(root3, text='New User', width=15,bg='black',fg='green', font=('Arial',18,'bold'))
    l4.place(x=45,y=20)

    l5 = Label(root3, text='Name', width=10,bg='black',fg='green', font=('Arial',15,'bold'))
    l5.place(x=20,y=70)

    e3 = Entry(root3, textvar=StuName, width=8,bg='black',fg='green', font=('Arial',15,'bold'))
    e3.place(x=150,y=70)

    l6 = Label(root3, text='Password', width=10,bg='black',fg='green', font=('Arial',15,'bold'))
    l6.place(x=30,y=120)

    e4 = Entry(root3, textvar=StuPwd, width=8,bg='black',fg='green', font=('Arial',15,'bold'))
    e4.place(x=150,y=120)

    l7 = Label(root3, text='Batch', width=10,bg='black',fg='green', font=('Arial',15,'bold'))
    l7.place(x=30,y=170)

    e5 = Entry(root3, textvar=Bat, width=8,bg='black',fg='green', font=('Arial',15,'bold'))
    e5.place(x=150,y=170)

    B4 = Button(root3, text='Submit',width=15,bg='black',fg='green', command=database2)
    B4.place(x=50,y=220)




def access():
    root2 = tkinter.Tk()
    root2.geometry('200x200')
    root2.resizable(0,0)
    root2.configure(background ='black')
    root2.title('Options')

    #functions
    def issue():
        root4 = tkinter.Tk()
        root4.geometry('200x200')
        root4.resizable(0,0)
        root4.configure(background ='black')
        root4.title('Issue')

        l9 = Label(root2, text='Availabel Books', width=15,bg='black',fg='green', font=('Arial',12,'bold'))
        l9.place(x=40,y=40)


    def returnn():
        root5 = tkinter.Tk()
        root5.geometry('200x200')
        root5.resizable(0,0)
        root5.configure(background ='black')
        root5.title('Return')

        l10 = Label(root2, text='Return Book', width=15,bg='black',fg='green', font=('Arial',12,'bold'))
        l10.place(x=40,y=40)

    #Label
    l8 = Label(root2, text='Availabel Options', width=15,bg='black',fg='green', font=('Arial',12,'bold'))
    l8.place(x=40,y=40)

    b5 = Button(root2, text='Issue', command=issue, width=10,bg='black',fg='green', font=('Arial',12,'bold'))
    b5.place(x=50,y=80)

    b6 = Button(root2, text='Return', command=returnn, width=10,bg='black',fg='green', font=('Arial',12,'bold'))
    b6.place(x=50,y=120)

#database
def database1():
    bk1 = "CS"
    bk2 = "CN"
    bk3 = "OS"
    bk4 = "CA"
    wr1 = "A"
    wr2 = "B"
    wr3 = "C"
    wr4 = "D"
    conn =sqlite3.connect('Books.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('INSERT INTO Books (BookName,Writer) VALUES(?,?)',(BookName,Writer))
        conn.commit()

def database2():
    Name = StuName.get()
    Pass = StuPwd.get()
    StuBatch = Bat.get()
    if Name==' ' and Pwd==' ' and Batch==' ':
        allfield()
    else:
        conn =sqlite3.connect('Details.db')
        with conn:
            cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Details (Name Text, Pass Text, Batch Text)')
            cursor.execute('INSERT INTO Details (Name,Pass,Batch) VALUES(?,?,?)',(Name,Pass,Batch))
            conn.commit()
        


#inner boby
l1 = Label(root, text='Library_Management_System', width=25,bg='black',fg='green', font=('Arial',15,'bold'))
l1.place(x=150,y=50)

l2 = Label(root, text='StuName', width=15,bg='black',fg='green', font=('Arial',15,'bold'))
l2.place(x=90,y=110)

e1 = Entry(root,textvar=Usn, width=15,bg='black',fg='green', font=('Arial',15,'bold'))
e1.place(x=280,y=110)
Usn = e1.get()

l3 = Label(root, text='StuPwd', width=15,bg='black',fg='green', font=('Arial',15,'bold'))
l3.place(x=90,y=180)

e2 = Entry(root,textvar=Pwd, show='*', width=15,bg='black',fg='green', font=('Arial',15,'bold'))
e2.place(x=280,y=180)
Pwd = e2.get()

B1 = Button(root, text='Login',width=15,bg='black',fg='green',command=login)
B1.place(x=180,y=220)

B2 = Button(root, text='NewUser',width=15,bg='black',fg='green',command=NewUser)
B2.place(x=180,y=300)


root.mainloop()
