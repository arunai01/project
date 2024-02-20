from tkinter import *
import mysql.connector

app=Tk()
app.title("Student mark List")
app.geometry("300x200")

class manuplate:
    def __init__(self):
        frametop=Frame(app, bg="black",width=800, height=300, padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT",command=self.insert).pack(padx=10, pady=10)
        btnupdate=Button(frametop,text="UPDATE").pack(padx=10, pady=10)
        btndelete=Button(frametop,text="DELETE").pack(padx=10, pady=10)
    def insert(self):
        win=Tk()
        win.title("Insert into my sql DBdemo")
        win.geometry("500x500")



        frametop=Frame(win,bg="black",width=500,height=100)
        frametop.pack(side = TOP )

        #frameright=Frame(app,bg="red",width=500,height=500)
        #frameright.pack(side =RIGHT)

        frameleft=Frame(win,bg="yellow",width=500,height=500,padx=30,pady=30)
        frameleft.pack(side =LEFT)



        lpl_title_of_operation=Label(frameleft,text="Insert Into MYSQL DBDemo")
        lpl_title_of_operation.grid(row=0,columnspan=5)

        lplname=Label(frameleft,text="name")
        lplname.grid(row=2,column=1,padx=30,pady=30)

        lpltamil=Label(frameleft,text="Tamil")
        lpltamil.grid(row=3,column=1,padx=30,pady=30)



        app.mainloop()

run=manuplate()
app.mainloop()