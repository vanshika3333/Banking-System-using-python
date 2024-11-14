from tkinter import *
from tkinter import messagebox
import sqlite3
win=Tk()
win.title("Banking Management System")
win.geometry("400x400")
user=StringVar()
passs=StringVar()

acno=StringVar()
name=StringVar();
contact=StringVar();
email=StringVar()
address=StringVar();
amount=StringVar();
dates=StringVar()
idtype=StringVar();
idno=StringVar();
gender=StringVar()
wdmoney=StringVar()
balance=StringVar()

conn=sqlite3.connect("mybankingdb.db");
def reset():
    user.set("")
    passs.set("")
def signup():
    username=user.get()
    password=passs.get()
    if(username==""):
        messagebox.showinfo("Banking Management","please enter the username")
    elif(password==""):
        messagebox.showinfo("Banking Management","please enter the password")
    else:
        conn.execute("create table if not exists login(username char(40),password char(40))")
        conn.execute("insert into login values(?,?)",(username,password,))
        conn.commit()
        messagebox.showinfo("Banking Management", "you are register User")
    
def signin():
    username=user.get()
    password=passs.get()
    if(username==""):
        messagebox.showinfo("Banking Management","please enter the username")
    elif(password==""):
        messagebox.showinfo("Banking Management","please enter the password")
    else:
        cursor=conn.execute("select * from login where username=? and password=?",(username,password,))
        if cursor.fetchone() is None:
            messagebox.showinfo("Banking Management","please enter the right username and password")
        else:
            messagebox.showinfo("Banking Management","you are administrator of project")
            mnframe.grid(row=0,column=0)
            lgframe.grid_forget()
def acaccount():
    acframe.grid(row=0,column=0)
    mnframe.grid_forget()
def newaccount():
    ncframe.grid(row=0,column=0)
    acframe.grid_forget()

def wcframe1():
    wcframe.grid(row=0,column=0)
    acframe.grid_forget()
    
lgframe=Frame(win)
lgframe.grid(row=0,column=0)
mnframe=Frame(win)
mnframe.grid_forget()

ncframe=Frame(win)
ncframe.grid_forget()

#-------------------main Frame coding------------

l1=Label(mnframe,text='Banking Management System').grid(row=0,column=0)
b1=Button(mnframe,text='Customer Management',command=acaccount).grid(row=1,column=1)
b2=Button(mnframe,text='Employee Management',bd=10,bg='cyan').grid(row=2,column=1)
b3=Button(mnframe,text='Complaint Management').grid(row=3,column=1)
b4=Button(mnframe,text='Suggestion Management').grid(row=4,column=1)
b5=Button(mnframe,text='Exit').grid(row=5,column=1)
b6=Button(mnframe,text='Back').grid(row=6,column=1)
#------------------main Frame close---------------

acframe=Frame(win)
acframe.grid_forget()
l1=Label(acframe,text='Banking Management System').grid(row=0,column=0)
b1=Button(acframe,text='Add New Customer',command=newaccount).grid(row=1,column=1)
b2=Button(acframe,text='Withdrawl Money',command=wcframe1).grid(row=2,column=1)
b3=Button(acframe,text='Deposit Money').grid(row=3,column=1)
b4=Button(acframe,text='See All Customer').grid(row=4,column=1)
b5=Button(acframe,text='Exit').grid(row=5,column=1)
b6=Button(acframe,text='Back').grid(row=6,column=1)

muframe=Frame(win)
muframe.grid_forget()
meframe=Frame(win)
meframe.grid_forget()
l1=Label(lgframe,text='Banking Management System',bg='cyan',bd=10,fg='blue').grid(row=0,column=0)
l2=Label(lgframe,text='username').grid(row=3,column=0)
e1=Entry(lgframe,textvariable=user).grid(row=3,column=1)
l3=Label(lgframe,text='password').grid(row=4,column=0)
e2=Entry(lgframe,textvariable=passs).grid(row=4,column=1)
b1=Button(lgframe,text='signup',command=signup).grid(row=5,column=0)
b2=Button(lgframe,text='signin',command=signin).grid(row=5,column=1)
b3=Button(lgframe,text='reset',command=reset).grid(row=5,column=2)
#-------------Add New Customer-------
def ncreset():
    acno.set("")
    name.set("")
    contact.set("")
    email.set("")
    address.set("")
    amount.set("")
    dates.set("")
    idtype.set("")
    idno.set("")
    gender.set("")

def ncsave():
    acno1=acno.get()
    name1=name.get()
    contact1=contact.get()
    email1=email.get()
    address1=address.get()
    amount1=amount.get()
    dates1=dates.get()
    idtype1=idtype.get()
    idno1=idno.get()
    gender1=gender.get()
    conn.execute("create table if not exists customer(accno char(40) not null,name char(40) not null,contacts char(30) not null,emails char(30)not null,address char(30) not null,amounts char(30) not null,datess char(30) not null,idypes char(30) not null,idnos char(30) not null,genders char(30) not null)")
    conn.execute("insert into customer values(?,?,?,?,?,?,?,?,?,?)",(acno1,name1,contact1,email1,address1,amount1,dates1,idtype1,idno1,gender1,))
    conn.commit()
    messagebox.showinfo("Banking Management","New Customer Register")
def ncsearch():
    acno1=acno.get()
    cursor=conn.execute("select * from customer where accno=?",(acno1,))
    for row in cursor:
        acno.set(row[0])
        name.set(row[1])
        contact.set(row[2])
        email.set(row[3])
        address.set(row[4])
        amount.set(row[5])
        dates.set(row[6])
        idtype.set(row[7])
        idno.set(row[8])
        gender.set(row[9])
    messagebox.showinfo("Banking management","Record Search")
def ncdelete():
    acno1=acno.get()
    conn.execute("delete from customer where accno=?",(acno1,))
    conn.commit()
    messagebox.showinfo("Banking Management","Record Deleted")
        
    

            
    
l1=Label(ncframe,text='Add New Customer',bg='cyan',fg='blue',bd=10).grid(row=0,column=0)
l2=Label(ncframe,text='Account no').grid(row=1,column=0)
e1=Entry(ncframe,textvariable=acno).grid(row=1,column=1)
l3=Label(ncframe,text='Name').grid(row=2,column=0)
e2=Entry(ncframe,textvariable=name).grid(row=2,column=1)
l4=Label(ncframe,text='contact no').grid(row=3,column=0)
e3=Entry(ncframe,textvariable=contact).grid(row=3,column=1)
l5=Label(ncframe,text='email').grid(row=4,column=0)
e4=Entry(ncframe,textvariable=email).grid(row=4,column=1)
l6=Label(ncframe,text='Address').grid(row=5,column=0)
e5=Entry(ncframe,textvariable=address).grid(row=5,column=1)
l7=Label(ncframe,text='Amount').grid(row=6,column=0)
e6=Entry(ncframe,textvariable=amount).grid(row=6,column=1)
l8=Label(ncframe,text='Date').grid(row=7,column=0)
e7=Entry(ncframe,textvariable=dates).grid(row=7,column=1)
l9=Label(ncframe,text='Id Proof').grid(row=8,column=0)
e8=Entry(ncframe,textvariable=idtype).grid(row=8,column=1)
l10=Label(ncframe,text='id No').grid(row=9,column=0)
e9=Entry(ncframe,textvariable=idno).grid(row=9,column=1)
l11=Label(ncframe,text='Gender').grid(row=10,column=0)
e10=Entry(ncframe,textvariable=gender).grid(row=10,column=1)
b1=Button(ncframe,text='Save',command=ncsave).grid(row=11,column=0)
b2=Button(ncframe,text='Update').grid(row=11,column=1)
b3=Button(ncframe,text='Delete',command=ncdelete).grid(row=11,column=2)
b4=Button(ncframe,text='Search',command=ncsearch).grid(row=11,column=3)
b5=Button(ncframe,text='Reset',command=ncreset).grid(row=11,column=4)

#------------------withdraw Money--------------
def wcsearch():
    acno1=acno.get()
    cursor=conn.execute("select * from customer where accno=?",(acno1,))
    for row in cursor:
        acno.set(row[0])
        name.set(row[1])
        contact.set(row[2])
        email.set(row[3])
        amount.set(row[5])

def balancecheck():
    amounts=amount.get()
    wdmoneys=wdmoney.get()
    if(int(amounts)<int(wdmoneys)):
        messagebox.showinfo("Banking Management","transaction is not posible")
        
wcframe=Frame(win)
wcframe.grid_forget()

l1=Label(wcframe,text='WithDraw Money',bg='cyan',fg='blue',bd=10).grid(row=0,column=0)
l2=Label(wcframe,text='Account no').grid(row=1,column=0)
e1=Entry(wcframe,textvariable=acno).grid(row=1,column=1)
l3=Label(wcframe,text='Name').grid(row=2,column=0)
e2=Entry(wcframe,textvariable=name).grid(row=2,column=1)
l4=Label(wcframe,text='contact no').grid(row=3,column=0)
e3=Entry(wcframe,textvariable=contact).grid(row=3,column=1)
l5=Label(wcframe,text='amount').grid(row=4,column=0)
e4=Entry(wcframe,textvariable=amount).grid(row=4,column=1)
l6=Label(wcframe,text='Date').grid(row=5,column=0)
e5=Entry(wcframe,textvariable=dates).grid(row=5,column=1)
l7=Label(wcframe,text='WithDraw Money').grid(row=6,column=0)
e6=Entry(wcframe,textvariable=wdmoney).grid(row=6,column=1)
l8=Label(wcframe,text='Balance').grid(row=7,column=0)
e7=Entry(wcframe,textvariable=balance).grid(row=7,column=1)
b1=Button(wcframe,text='WithDraw Money',command=ncsave).grid(row=9,column=0)
b4=Button(wcframe,text='Search',command=wcsearch).grid(row=9,column=1)
b5=Button(wcframe,text='Reset',command=balancecheck).grid(row=9,column=2)





win.mainloop()
