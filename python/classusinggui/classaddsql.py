from tkinter import *
import mysql.connector

app1=Tk()
app1.title("+2 Students Mark List")
app1.geometry("500x500")

class manuplate1():

    def __init__(self)
        btnsub=Button(app1,text="insert",font=("Batang",14),fg="White",bg="Green",command=self.insert)
        btnsub.grid(row=2,column=3)
      




my=Tk()

my.title("Marksheet")
my.geometry("500x700")

def DBconnection():
    dpcon=mysql.connector.connect(
        host="192.168.1.240",
        user="AIBATCH01",
        password="AI@123",
        database="ai__arun")
    
    return dpcon


def insert1():
    a=tbEntrya.get()
    b=tbEntryb.get()
    c=tbEntryc.get()
    d=tbEntryd.get()
    e=tbEntrye.get()
    f=tbEntryf.get()
    g=tbEntryg.get()
    h=tbEntryh.get()

    e_con=DBconnection()
    result=e_con.cursor()
    statement="insert into studentmark_list(Name,age,tamil,English,maths,physics,chemistry,computer_science) value(%s,%s,%s,%s,%s,%s,%s,%s);"
    valuepass=(a,b,c,d,e,f,g,h)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount,"row insert")

    lploutput1.config(text=a)
    lploutput2.config(text=b)
    lploutput3.config(text=c)
    lploutput4.config(text=d)
    lploutput5.config(text=e)
    lploutput6.config(text=f)
    lploutput7.config(text=g)
    lploutput8.config(text=h)


lpltitle1=Label(my,text="Name",font=("Times of roman",14)).grid(row=1,column=1)
tbEntrya=Entry(my,width=20)
tbEntrya.grid(row=1,column=2)

lpltitle2=Label(my,text="Age",font=("Times of roman",14))
lpltitle2.grid(row=2,column=1)
lpltitle3=Label(my,text="Tamil",font=("Times of roman",14))
lpltitle3.grid(row=3,column=1)
lpltitle4=Label(my,text="English",font=("Times of roman",14))
lpltitle4.grid(row=4,column=1)
lpltitle5=Label(my,text="Maths",font=("Times of roman",14))
lpltitle5.grid(row=5,column=1)
lpltitle6=Label(my,text="physics",font=("Times of roman",14))
lpltitle6.grid(row=6,column=1)
lpltitle7=Label(my,text="Chemistry",font=("Times of roman",14))
lpltitle7.grid(row=7,column=1)
lpltitle8=Label(my,text="Compuetr science",font=("Times of roman",10))
lpltitle8.grid(row=8,column=1)
lpltitle9=Label(my,text="S-no")
lpltitle9.grid(row=9,column=1)

tbEntryb=Entry(my,width=20)
tbEntryb.grid(row=2,column=2)
tbEntryc=Entry(my,width=20)
tbEntryc.grid(row=3,column=2)
tbEntryd=Entry(my,width=20)
tbEntryd.grid(row=4,column=2)
tbEntrye=Entry(my,width=20)
tbEntrye.grid(row=5,column=2)
tbEntryf=Entry(my,width=20)
tbEntryf.grid(row=6,column=2)
tbEntryg=Entry(my,width=20)
tbEntryg.grid(row=7,column=2)
tbEntryh=Entry(my,width=15)
tbEntryh.grid(row=8,column=2)
tbEntryi=Entry(my,width=15)
tbEntryi.grid(row=9,column=2)

lploutput1=Label(my,text="")
lploutput1.grid(row=9,column=3)
lploutput2=Label(my,text="")
lploutput2.grid(row=10,column=3)
lploutput3=Label(my,text="")
lploutput3.grid(row=11,column=3)
lploutput4=Label(my,text="")
lploutput4.grid(row=12,column=3)
lploutput5=Label(my,text="")
lploutput5.grid(row=13,column=3)
lploutput6=Label(my,text="")
lploutput6.grid(row=14,column=3)
lploutput7=Label(my,text="")
lploutput7.grid(row=15,column=3)
lploutput8=Label(my,text="")
lploutput8.grid(row=16,column=3)
lploutput9=Label(my,text="")
lploutput9.grid(row=17,column=3)





btnsub=Button(my,text="insert",font=("Batang",14),fg="White",bg="Green",command=insert1).grid(row=10,column=1)


my.mainloop()
