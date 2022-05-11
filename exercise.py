import tkinter as tk
from tkinter import *

import cx_Oracle as o


from cx_Oracle import *


# create connection

con = o.connect('C##pradeep/idevelop123@localhost:1521/pandu')


print(con.version)








# create cursor
#cur = con.cursor()


# cur.execute("create table orac(incidentnumber varchar(20) NOT NULL UNIQUE, username varchar(20) NOT NULL UNIQUE, updatedby varchar(200) NOT NULL UNIQUE)")

def submit():
    try:
        cur = con.cursor()
        first=StringVar()
        second=StringVar()
        third=StringVar()
        first = textbox1.get()
        second = textbox2.get()
        third = textbox3.get()
        print(first + "  " + second + "  " + third)

       # sql = INSERT INTO second VAlUES(%s, %s, %s)
        if (first and second and third != " "):

          cur.execute("INSERT INTO pandu1 VAlUES ('first', 'second', 'third')")

        #print(cur.execute('select * from oracle'))
          con.commit()
          var4.set("successfully added to database")
        else:
            var4.set("give some values ")




    except o.Error as err1:
        s = str(err1)
        var4.set(s)
    return True








from PIL import Image,ImageTk
window = tk.Tk()
window.geometry("1350x700+0+0")
window.title("python program")






var1 = StringVar()
incidentnumber = StringVar()
var2 = StringVar()
username = StringVar()
var3 = StringVar()
createdby = StringVar()
var4 = StringVar()

label1 = Label(window, textvariable=var1, font=("Helvetica", 18))
var1.set("incident number")
label1.grid(row=0, column=1)
textbox1 = tk.Entry(window, width=35, borderwidth=5, textvariable=incidentnumber, font=("Helvetica", 18), fg='blue')
incidentnumber.set("")
textbox1.grid(row=0, column=2, columnspan=3, padx=30)

label2 = Label(window, textvariable=var2, font=("Helvetica", 18))
var2.set("username")
label2.grid(row=1, column=1)

textbox2 = tk.Entry(window, width=35, borderwidth=5, textvariable=username, font=("Helvetica", 18), fg='blue')
username.set("")
textbox2.grid(row=1, column=2)

label3 = Label(window, textvariable=var3, font=("Helvetica", 18))
var3.set("created by")
label3.grid(row=3, column=1)
textbox3 = tk.Entry(window, width=35, borderwidth=5, textvariable=createdby, font=("Helvetica", 18), fg='blue')
createdby.set("")
textbox3.grid(row=3, column=2)

label4 = Label(window, textvariable=var4, font=("Helvetica", 18), text="")
label4.grid(row=6, column=1)

btn = Button(window, text="submit to db", pady=20, font=("Helvetica", 18), command=submit)
btn.grid(row=4, column=2)

window.title("first form")
window.geometry("600x600+0+0")
window.resizable(False, False)

window.mainloop()
