from tkinter import *

dows=Tk()

dows.title("opetaors")
dows.geometry("500x500")
#dows.state("zoomed")

def addition():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    lbloutput.config(text=a+b)

def subtraction():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    lbloutput.config(text=a-b)

def multiplication():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    lbloutput.config(text=a*b)

def stri():
    a=(tbEntrya.get())
    b=(tbEntryb.get())
    lbloutput.config(text=f"my name :{a}")
    lbloutput2.config(text=f"she name :{b}")


                     
lbltitle=Label(dows,text="operators")
lbltitle.grid(row=1,column=2,padx=20,pady=20)


lblmsg1=Label(dows,text="Enter tha a value :")
lblmsg1.grid(row=2,column=4,pady=30)

tbEntrya=Entry(dows,width=60)
tbEntrya.grid(row=2,column=8,pady=30)

lblmsg2=Label(dows,text="Enter the value b :")
lblmsg2.grid(row=4,column=4,pady=30)

tbEntryb=Entry(dows,width=60)
tbEntryb.grid(row=4,column=8,pady=30)


lbloutput=Label(dows,text="value")
lbloutput.grid(row=6,column=8,pady=30)

lbloutput2=Label(dows,text="")
lbloutput2.grid(row=8,column=8)

btnadd=Button(dows,text="Addition",command=addition)
btnadd.grid(row=7,column=1)

btnadd2=Button(dows,text="subtraction",command=subtraction)
btnadd2.grid(row=7,column=2)

btnadd3=Button(dows,text="multiplication",command=multiplication)
btnadd3.grid(row=7,column=3)

btnst=Button(dows,text="sumbit",command=stri)
btnst.grid(row=8,column=5)

dows.mainloop()


