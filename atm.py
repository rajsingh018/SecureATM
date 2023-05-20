# !/usr/bin/python3
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import random
import db_connection1 as db

connection = db.mysql_connect()
cursor = connection.cursor()
expression = ''
expressio = ''
expres = ''
expre = ''
expr = ''
shuffledList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def acc():
    n = atmid.get()
    cursor.execute("select * from customer where account_no=" + str(n))
    accountDetails = cursor.fetchone()
    connection.commit()
    tk.Label(p2, text='Acount Balance', font=("Times New Roman", 25), fg='black', bg='yellow').place(relx=0.68, rely=0.25)
    tk.Label(p2, text=accountDetails[5], font=("Times New Roman", 20), fg='black', bg='yellow').place(relx=0.71, rely=0.3)
def passw():
    fr(p5)
    n = atmid.get()
    cursor.execute("select * from customer where account_no=" + str(n))
    accountDetails = cursor.fetchone()

    pi = int(pin.get())
    print(pi)
    print((accountDetails[6]))
    print(type(pi))
    print(type(accountDetails[6]))
    p = int(pi)
    print(type(p))
    if p == accountDetails[6]:
        print("current balance : ₹", accountDetails[5])
        q = wa.get()
        a = int(q)
        print(q)
        if a < accountDetails[5]:
            withdrawStr = str(a)
            cursor.execute(
                "update customer set amount=amount-" + withdrawStr + " where account_no=" + str(accountDetails[0]))
            connection.commit()
            fr(p6)
    else:
        tk.Label(p5, text='INCORRECT PIN', bg='yellow').place(relx=.22, rely=.22)
def info(a, b):
    tk.Label(p2, text='Account Holder -', bg='light blue', font=("Times New Roman", 20)).place(relx=.07, rely=.2)
    tk.Label(p2, text='Phone Number -', bg='light blue', font=("Times New Roman", 20)).place(relx=.07, rely=.27)
    tk.Label(p2, text=a, bg='light blue', font=("Times New Roman", 20)).place(relx=.3, rely=.2)
    tk.Label(p2, text=b, bg='light blue', font=("Times New Roman", 20)).place(relx=.3, rely=.27)
def fr(frame):
    frame.tkraise()
def ch_atmid():
    n = atmid.get()
    cursor.execute("select * from customer where account_no=" + str(n))
    accountDetails = cursor.fetchone()
    if accountDetails != None:
        print(accountDetails[1], accountDetails[2])
        atmid.set(n)
        info(accountDetails[1], accountDetails[2])
        fr(p2)
    else:
        bak = tk.Label(p1, text='USER NOT FOUND', bg='yellow')
        bak.place(relx=.2,rely=.33)
def withdraw():
    n = atmid.get()
    cursor.execute("select * from customer where account_no=" + str(n))
    accountDetails = cursor.fetchone()
    q=wa.get()
    a=int(q)
    passw()


def deposite():
    n = atmid.get()
    cursor.execute("select * from customer where account_no=" + str(n))
    accountDetails = cursor.fetchone()
    q=da.get()
    deposited = str(q)
    cursor.execute("update customer set amount=amount+" + deposited + " where account_no=" + str(accountDetails[0]))
    connection.commit()
    fr(p6)
def clear():
    global expression
    expression = ""
    atmid.set("")
def clear2():
    global expressio
    expressio = ""
    da.set("")

def clear3():
    global expres
    expres = ""
    wa.set("")
def clear5():
    global expre
    expre = ""
    pin.set("")

def press2(num):

    # point out the global expression variable
    global expressio

    # concatenation of string
    expressio = expressio + str(num)

    # update the expression by using set method
    da.set(expressio)

def pres3(num):

    # point out the global expression variable
    global expres

    # concatenation of string
    expres = expres + str(num)

    # update the expression by using set method
    wa.set(expres)

def pres5(num):
    global expre
    expre = expre + str(num)

    # update the expression by using set method
    pin.set(expre)

def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    atmid.set(expression)

win=tk.Tk()
win.title("ATM")
win.geometry('650x550')
win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)
atmid = tk.StringVar()
da = tk.IntVar()
wa = tk.StringVar()
pin = tk.StringVar()

img1 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn1.JPG"))
img2 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn2.JPG"))
img3 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn3.JPG"))
img4 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn4.JPG"))
img5 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn5.JPG"))
img6 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn6.JPG"))
img7 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn7.JPG"))
img8 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn8.JPG"))
img9 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn9.JPG"))
img0 = ImageTk.PhotoImage(Image.open("/Users/divyanshyadav/Downloads/btn10.JPG"))

#*****************************PAGE1****************************
p1=tk.Frame(win, bg='light blue')
h1=tk.Label(p1, text="ATM",font=("Times New Roman",85), fg='black', bg='light blue')
atmidl=tk.Label(p1, text='Enter Your Account Number',bg='light blue', font=("Times New Roman", 20)).place(anchor='center', relx=.3, rely=.25)
atmide=tk.Entry(p1, textvariable=atmid, width=25,highlightbackground='light blue').place(anchor='center', relx=.3, rely=.3)
bak=tk.Label(p1, text='', bg='dark grey')
bak.pack(ipadx=120, ipady=300, side='right')
ba=tk.Label(p1, text='', bg='#0390fc')
ba.pack(ipadx=200, ipady=150, side='bottom')

button1 = tk.Button(p1, text=' 1 ', fg='black', highlightbackground='#0390fc', command=lambda: press(1), height=1, width=7)
button1.place(relx=.05, rely=.45)

button2 = tk.Button(p1, text=' 2 ', fg='black', highlightbackground='#0390fc', command=lambda: press(2), height=1, width=7)
button2.place(relx=.25, rely=.45)

button3 = tk.Button(p1, text=' 3 ', fg='black', highlightbackground='#0390fc', command=lambda: press(3), height=1, width=7)
button3.place(relx=.45, rely=.45)

button4 = tk.Button(p1, text=' 4 ', fg='black', highlightbackground='#0390fc', command=lambda: press(4), height=1, width=7)
button4.place(relx=.05, rely=.55)

button5 = tk.Button(p1, text=' 5 ', fg='black', highlightbackground='#0390fc', command=lambda: press(5), height=1, width=7)
button5.place(relx=.25, rely=.55)

button6 = tk.Button(p1, text=' 6 ', fg='black', highlightbackground='#0390fc', command=lambda: press(6), height=1, width=7)
button6.place(relx=.45, rely=.55)

button7 = tk.Button(p1, text=' 7 ', fg='black', highlightbackground='#0390fc', command=lambda: press(7), height=1, width=7)
button7.place(relx=.05, rely=.65)

button8 = tk.Button(p1, text=' 8 ', fg='black', highlightbackground='#0390fc', command=lambda: press(8), height=1, width=7)
button8.place(relx=.25, rely=.65)

button9 = tk.Button(p1, text=' 9 ', fg='black', highlightbackground='#0390fc', command=lambda: press(9), height=1, width=7)
button9.place(relx=.45, rely=.65)

button0 = tk.Button(p1, text=' 0 ', fg='black', highlightbackground='#0390fc', command=lambda: press(0), height=1, width=7)
button0.place(relx=.25, rely=.75)
clear = tk.Button(p1, text='CLEAR', highlightbackground='dark grey', font=("Times New Roman", 15), width=20, command=clear)
clear.place(relx=.67, rely=.55)

clear = tk.Button(p1, text='EXIT', highlightbackground='dark grey', font=("Times New Roman", 15), width=20, command=lambda:win.destroy())
clear.place(relx=.67, rely=.65)

#*****************************PAGE2****************************
p2=tk.Frame(win,bg='light blue')
h2=tk.Label(p2, text="ATM", font=("Times New Roman", 65), fg='black', bg='light blue')


bak=tk.Label(p2, text='', bg='dark grey')
bak.pack(ipadx=120, ipady=300, side='right')
ba=tk.Label(p2, text='', bg='#0390fc')
ba.pack(ipadx=200, ipady=150, side='bottom')
clear = tk.Button(p2, text='EXIT', highlightbackground='dark grey', font=("Times New Roman",15), width=20, command=lambda:win.destroy())
clear.place(relx=.67, rely=.65)

#*****************************PAGE3****************************
p3=tk.Frame(win,bg='light blue')
h3=tk.Label(p3, text="ATM", font=("Times New Roman", 65), fg='black', bg='light blue')

dal=tk.Label(p3, text='Enter amount to Deposite', bg='light blue',font=("Times New Roman", 20)).place(anchor='center', relx=.3, rely=.25)
dae=tk.Entry(p3, textvariable=da,width=25, highlightbackground='light blue').place(anchor='center', relx=.3, rely=.3)
bak=tk.Label(p3, text='', bg='dark grey')
bak.pack(ipadx=120,ipady=300,side='right')
ba=tk.Label(p3, text='', bg='#0390fc')
ba.pack(ipadx=200, ipady=150, side='bottom')

button1 = tk.Button(p3, text=' 1 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(1), height=1, width=7)
button1.place(relx=.05, rely=.45)

button2 = tk.Button(p3, text=' 2 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(2), height=1, width=7)
button2.place(relx=.25, rely=.45)

button3 = tk.Button(p3, text=' 3 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(3), height=1, width=7)
button3.place(relx=.45, rely=.45)

button4 = tk.Button(p3, text=' 4 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(4), height=1, width=7)
button4.place(relx=.05, rely=.55)

button5 = tk.Button(p3, text=' 5 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(5), height=1, width=7)
button5.place(relx=.25, rely=.55)

button6 = tk.Button(p3, text=' 6 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(6), height=1, width=7)
button6.place(relx=.45, rely=.55)

button7 = tk.Button(p3, text=' 7 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(7), height=1, width=7)
button7.place(relx=.05, rely=.65)

button8 = tk.Button(p3, text=' 8 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(8), height=1, width=7)
button8.place(relx=.25, rely=.65)

button9 = tk.Button(p3, text=' 9 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(9), height=1, width=7)
button9.place(relx=.45, rely=.65)

button0 = tk.Button(p3, text=' 0 ', fg='black', highlightbackground='#0390fc',command=lambda: press2(0), height=1, width=7)
button0.place(relx=.25, rely=.75)
clear = tk.Button(p3, text='CLEAR',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:clear2())
clear.place(relx=.67, rely=.55)

back = tk.Button(p3, text='BACK',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:fr(p2))
back.place(relx=.67, rely=.75)

exit = tk.Button(p3, text='EXIT',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:win.destroy())
exit.place(relx=.67, rely=.65)


#*****************************PAGE4****************************
p4=tk.Frame(win,bg='light blue')
h4=tk.Label(p4,text="ATM",font=("Times New Roman",65),fg='black',bg='light blue')

wal=tk.Label(p4,text='Enter amount to Withdraw',bg='light blue',font=("Times New Roman",20)).place(anchor='center', relx=.3, rely=.25)
wae=tk.Entry(p4,textvariable=wa,width=25,highlightbackground='light blue').place(anchor='center', relx=.3, rely=.3)
bak=tk.Label(p4,text='', bg='dark grey')
bak.pack(ipadx=120, ipady=300, side='right')
ba=tk.Label(p4, text='', bg='#0390fc')
ba.pack(ipadx=200, ipady=150, side='bottom')

button1 = tk.Button(p4, text=' 1 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(1), height=1, width=7)
button1.place(relx=.05, rely=.45)

button2 = tk.Button(p4, text=' 2 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(2), height=1, width=7)
button2.place(relx=.25, rely=.45)

button3 = tk.Button(p4, text=' 3 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(3), height=1, width=7)
button3.place(relx=.45, rely=.45)

button4 = tk.Button(p4, text=' 4 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(4), height=1, width=7)
button4.place(relx=.05, rely=.55)

button5 = tk.Button(p4, text=' 5 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(5), height=1, width=7)
button5.place(relx=.25, rely=.55)

button6 = tk.Button(p4, text=' 6 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(6), height=1, width=7)
button6.place(relx=.45, rely=.55)

button7 = tk.Button(p4, text=' 7 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(7), height=1, width=7)
button7.place(relx=.045, rely=.65)

button8 = tk.Button(p4, text=' 8 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(8), height=1, width=7)
button8.place(relx=.25, rely=.65)

button9 = tk.Button(p4, text=' 9 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(9), height=1, width=7)
button9.place(relx=.45, rely=.65)

button0 = tk.Button(p4, text=' 0 ', fg='black', highlightbackground='#0390fc',command=lambda: pres3(0), height=1, width=7)
button0.place(relx=.25, rely=.75)

back = tk.Button(p4, text='BACK',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:fr(p2))
back.place(relx=.67, rely=.75)

clear = tk.Button(p4, text='CLEAR',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:clear3())
clear.place(relx=.67, rely=.55)

exit = tk.Button(p4, text='EXIT',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:win.destroy())
exit.place(relx=.67, rely=.65)

#*****************************PAGE5****************************
p5=tk.Frame(win,bg='light blue')
h5=tk.Label(p5,text="ATM",font=("Times New Roman",39),fg='black',bg='light blue')

tk.Label(p5, text='Enter Your PIN', bg='light blue', font=("Times New Roman", 20)).place(anchor='center', relx=.3, rely=.3)
pine=tk.Entry(p5, textvariable=pin,show="*", width=25, highlightbackground='light blue').place(anchor='center', relx=.3, rely=.36)
newFrame = Frame(p5, bg='Light blue')
newFrame.grid(column=6)
bak=tk.Label(p5, text='', bg='dark grey')
bak.pack(anchor='s', ipadx=120, ipady=225, side='right')
ba=tk.Label(p5, text='', bg='#0390fc')
ba.pack(ipadx=200, ipady=150, side='bottom')


random.shuffle(shuffledList)
globalList = shuffledList

lst = [(globalList[0], img1),
           (globalList[1], img2),
           (globalList[2], img3),
           (globalList[3], img4),
           (globalList[4], img5),
           (globalList[5], img6),
           (globalList[6], img7),
           (globalList[7], img8),
           (globalList[8], img9),
           (globalList[9], img0)]

for i in range(2):
        bgColor = ""
        for j in range(10):
            bgColor = lst[j][0]
            lstimg = lst[j][1]
            if i == 0:
                e = Label(newFrame, height=45, width=45, image=lstimg)
                e.grid(row=i, column=j)
                e = Text(newFrame, height=2, width=5, fg='Black', font=('Times New Roman', 13), padx=5, pady=1)
                e.grid(row=i+1, column=j)
                e.insert(END, lst[j][i])

button1 = tk.Button(p5, text=' 1 ',image=img1, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[0]))
button1.place(relx=.07, rely=.47)

button2 = tk.Button(p5, text=' 2 ',image=img2, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[1]))
button2.place(relx=.25, rely=.47)

button3 = tk.Button(p5, text=' 3 ',image=img3, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[2]))
button3.place(relx=.43, rely=.47)

button4 = tk.Button(p5, text=' 4 ',image=img4, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[3]))
button4.place(relx=.07, rely=.6)

button5 = tk.Button(p5, text=' 5 ',image=img5, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[4]))
button5.place(relx=.25, rely=.6)

button6 = tk.Button(p5, text=' 6 ',image=img6, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[5]))
button6.place(relx=.43, rely=.6)

button7 = tk.Button(p5, text=' 7 ',image=img7, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[6]))
button7.place(relx=.07, rely=.73)

button8 = tk.Button(p5, text=' 8 ',image=img8, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[7]))
button8.place(relx=.25, rely=.73)

button9 = tk.Button(p5, text=' 9 ',image=img9, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[8]))
button9.place(relx=.43, rely=.73)

button0 = tk.Button(p5, text=' 0 ',image=img0, fg='black', highlightbackground='#0390fc',command=lambda: pres5(globalList[9]))
button0.place(relx=.25, rely=.85)
back = tk.Button(p5, text='BACK',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:fr(p4))
back.place(relx=.67, rely=.75)

clear = tk.Button(p5, text='CLEAR',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:clear5())
clear.place(relx=.67, rely=.55)

exit = tk.Button(p5, text='EXIT',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:win.destroy())
exit.place(relx=.67, rely=.85)
#*****************************PAGE6****************************
p6=tk.Frame(win, bg='light blue')
h6=tk.Label(p6, text="THANK YOU", font=("Times New Roman", 65), fg='black', bg='light blue')
tk.Label(p6, text="VISIT AGAIN", font=("Times New Roman", 65), fg='black', bg='light blue').place(relx=.2, rely=.2)

for frame in (p1, p2, p3, p4, p5, p6):
    frame.grid(row=0, column=0, sticky='nsew')

fr1=tk.Button(p1,text='ENTER',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:ch_atmid())
fr1.place(relx=.67, rely=.45)


fr2=tk.Button(p2,text='DEPOSITE',highlightbackground='black',font=("Times New Roman",15),height=5,width=20,command=lambda:fr(p3))
fr2.place(relx=.15, rely=.43)
fr2=tk.Button(p2,text='WITHDRAW',highlightbackground='black',font=("Times New Roman",15),height=5,width=20,command=lambda:fr(p4))
fr2.place(relx=.15, rely=.615)
fr2=tk.Button(p2,text='CHECK BALANCE',highlightbackground='black',font=("Times New Roman",15),height=5,width=20,command=lambda:acc())
fr2.place(relx=.15, rely=.8)

fr3=tk.Button(p3,text='ENTER',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:deposite())
fr3.place(relx=.67, rely=.45)

fr4=tk.Button(p4,text='ENTER',highlightbackground='dark grey',font=("Times New Roman",15),width=20,command=lambda:withdraw())
fr4.place(relx=.67, rely=.45)

fr5=tk.Button(p5, text='ENTER', highlightbackground='dark grey',font=("Times New Roman", 15), width=20, command=lambda:passw())
fr5.place(relx=.67, rely=.65)

exit = tk.Button(p6, text='EXIT',fg='black',highlightbackground='light blue', font=("Times New Roman", 15),width=20,command=lambda:win.destroy())
exit.place(relx=.35, rely=.65)

h1.place(anchor='center', relx=.3, rely=.1)
h2.pack()
h3.pack()
h4.pack()
h5.place(relx=0.82, rely=0.03)
h6.pack()
fr(p1)
win.mainloop()
