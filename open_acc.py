# !/usr/bin/python3
from tkinter import *
import db_connection1 as db

connection = db.mysql_connect()
cursor = connection.cursor()

accno = {}

def det():
    global accno
    accno['name'] = name.get()
    accno['phone'] = num.get()
    accno['address'] = add.get()
    accno['adhar'] = adhar.get()
    of = 'yes'
    print(accno)
    fr(p2)
def fin():
    global accno

    i = 2000
    accno['amount'] = int(amm.get())
    if accno['amount'] >= i:
            accno['accno'] = atmid.get()
            print(accno)
            pin = pini.get()
            print(accno)
            cursor.execute("insert into customer(account_no,name,phone,address,adhar,amount,pin) values(" + str(
                accno['accno']) + ",'" + accno['name'] + "'," + str(accno['phone']) + ",'" + accno[
                               'address'] + "'," + str(accno['adhar']) + "," +
                           str(accno['amount']) + "," + str(pin) + ")")
            connection.commit()
            print("****NEW ACCOUNT OPENED****")
    else:
        print("can not open account")
    print(accno)
    fr(p3)

def fr(frame):
    frame.tkraise()

win=Tk()
win.title("BANK")
win.geometry('650x550')
win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)

atmid = StringVar()
name = StringVar()
num = StringVar()
add = StringVar()
adhar = StringVar()
amm = StringVar()
pini = StringVar()
p1=Frame(win, bg='light blue')
h1=Label(p1, text="BANK",font=("Times New Roman",85), fg='black', bg='light blue')

namel=Label(p1, text='Enter Your Name',bg='light blue', font=("Times New Roman", 17)).place(anchor='center', relx=.2, rely=.23)
namee=Entry(p1, textvariable=name, width=25,highlightbackground='light blue').place(anchor='center', relx=.5, rely=.23)
numb=Label(p1, text='Phone Number',bg='light blue', font=("Times New Roman", 17)).place(anchor='center', relx=.2, rely=.33)
numbe=Entry(p1, textvariable=num, width=25,highlightbackground='light blue').place(anchor='center', relx=.5, rely=.33)
addl=Label(p1, text='Enter Your Address',bg='light blue', font=("Times New Roman", 17)).place(anchor='center', relx=.2, rely=.43)
adde=Entry(p1, textvariable=add, width=25,highlightbackground='light blue').place(anchor='center', relx=.5, rely=.43)
adharl=Label(p1, text='Enter Your Adhar Number',bg='light blue', font=("Times New Roman", 17)).place(anchor='center', relx=.19, rely=.53)
adahre=Entry(p1, textvariable=adhar, width=25,highlightbackground='light blue').place(anchor='center', relx=.5, rely=.53)
fr1=Button(p1, text='ENTER', highlightbackground='light blue',font=("Times New Roman", 15), width=20,command=lambda : det())
fr1.place(relx=.67, rely=.75)

p2=Frame(win, bg='light blue')
h2=Label(p2, text="BANK",font=("Times New Roman",85), fg='black', bg='light blue')
amml=Label(p2, text='Enter Ammount Deposited',bg='light blue', font=("Times New Roman", 17)).place(anchor='center', relx=.19, rely=.23)
amme=Entry(p2, textvariable=amm, width=25,highlightbackground='light blue').place(anchor='center', relx=.5, rely=.23)
pinb=Label(p2, text='Enter PIN Number',bg='light blue', font=("Times New Roman", 17)).place(anchor='center', relx=.2, rely=.33)
pine=Entry(p2, textvariable=pini, show="*", width=25,highlightbackground='light blue').place(anchor='center', relx=.5, rely=.33)
atmidl=Label(p2, text='Enter Account Number',bg='light blue', font=("Times New Roman", 17)).place(anchor='center', relx=.2, rely=.43)
atmidle=Entry(p2, textvariable=atmid, width=25,highlightbackground='light blue').place(anchor='center', relx=.5, rely=.43)
fr2=Button(p2, text='ENTER', highlightbackground='light blue',font=("Times New Roman", 15), width=20,command=lambda : fin())
fr2.place(relx=.67, rely=.75)


p3=Frame(win, bg='light blue')
h3=Label(p3, text="THANK YOU", font=("Times New Roman", 65), fg='black', bg='light blue')
Label(p3, text="VISIT AGAIN", font=("Times New Roman", 65), fg='black', bg='light blue').place(relx=.2, rely=.2)

exit1 = Button(p1, text='EXIT',fg='black',highlightbackground='light blue', font=("Times New Roman", 15),width=20,command=lambda:win.destroy())
exit1.place(relx=.67, rely=.68)

exit2 = Button(p2, text='EXIT',fg='black',highlightbackground='light blue', font=("Times New Roman", 15),width=20,command=lambda:win.destroy())
exit2.place(relx=.67, rely=.65)

exit = Button(p3, text='EXIT',fg='black',highlightbackground='light blue', font=("Times New Roman", 15),width=20,command=lambda:win.destroy())
exit.place(relx=.35, rely=.65)


for frame in (p1, p2, p3):
    frame.grid(row=0, column=0, sticky='nsew')

h1.pack()
h2.pack()
h3.pack()
fr(p1)
win.mainloop()