from tkinter import *

my=Tk()

my.title("Marksheet")
my.geometry("500x700")

def insert1():
    a=tbEntrya.get()
    b=tbEntryb.get()
    c=tbEntryc.get()
    d=tbEntryd.get()
    e=tbEntrye.get()
    f=tbEntryf.get()
    g=tbEntryg.get()
    lploutput1.config(text=a)
    lploutput2.config(text=b)
    lploutput3.config(text=c)
    lploutput4.config(text=d)
    lploutput5.config(text=e)
    lploutput6.config(text=f)
    lploutput7.config(text=g)


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
lpltitle6=Label(my,text="Science",font=("Times of roman",14))
lpltitle6.grid(row=6,column=1)
lpltitle7=Label(my,text="Social Science",font=("Times of roman",14))
lpltitle7.grid(row=7,column=1)

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

lploutput1=Label(my,text="My name is :")
lploutput1.grid(row=9,column=3)
lploutput2=Label(my,text="My name is :")
lploutput2.grid(row=10,column=3)
lploutput3=Label(my,text="My name is :")
lploutput3.grid(row=11,column=3)
lploutput4=Label(my,text="My name is :")
lploutput4.grid(row=12,column=3)
lploutput5=Label(my,text="My name is :")
lploutput5.grid(row=13,column=3)
lploutput6=Label(my,text="My name is :")
lploutput6.grid(row=14,column=3)
lploutput7=Label(my,text="My name is :")
lploutput7.grid(row=15,column=3)



btnsub=Button(my,text="insert",font=("Batang",14),fg="White",bg="Green",command=insert1).grid(row=8,column=1)


my.mainloop()


