from tkinter import *
import mysql.connector

app=Tk()
app.title("Insert into my sql DBdemo")
app.geometry("500x500")



frametop=Frame(app,bg="black",width=500,height=100)
frametop.pack(side = TOP )

#frameright=Frame(app,bg="red",width=500,height=500)
#frameright.pack(side =RIGHT)

frameleft=Frame(app,bg="yellow",width=500,height=500,padx=30,pady=30)
frameleft.pack(side =LEFT)



lpl_title_of_operation=Label(frameleft,text="Insert Into MYSQL DBDemo")
lpl_title_of_operation.grid(row=0,columnspan=5)

lplname=Label(frameleft,text="name")
lplname.grid(row=2,column=1,padx=30,pady=30)

lpltamil=Label(frameleft,text="Tamil")
lpltamil.grid(row=3,column=1,padx=30,pady=30)



app.mainloop()
