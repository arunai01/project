"""from tkinter import *

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

def division():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    lbloutput.config(text=a/b)

def module():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    lbloutput.config(text=a%b)

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

btnadd4=Button(dows,text="division",command=division)
btnadd4.grid(row=7,column=4)

btnadd5=Button(dows,text="module",command=module)
btnadd5.grid(row=7,column=5)



btnst=Button(dows,text="sumbit",command=stri)
btnst.grid(row=8,column=5)

dows.mainloop()"""

from tkinter import *
from tkinter import ttk
import tkinter as tk

details=Tk()
details.title("Aadhar ID information Details")
details.geometry("500x500")

def sumbit():
    a=tbEntrya.get()
    b=tbEntryb.get()
    labeloutput1(text=a)
    labeloutput2(text=b)




labeltitle=Label(details,text="Enter your name :")
labeltitle.grid(row=1,column=0)
labeltitle1=Label(details,text="Enter Last name ")
labeltitle1.grid(row=2,column=0)
tbEntrya=Entry(details,width=60)
tbEntrya.grid(row=1,column=1)
tbEntryb=Entry(details,width=60)
tbEntryb.grid(row=2,column=1)
var1=IntVar()
Radiobutton(details,text="Male",variable=var1).grid(row=3,column=0)
var2=IntVar()
Checkbutton(details,text="Female",variable=var2).grid(row=3,column=1)
var3=IntVar()
Checkbutton(details,text="Trasgender",variable=var3).grid(row=3,column=2)

Label(details,text="Date of birth:").grid(row=4,column=0)
e3=Entry(details)
e3.grid(row=4,column=1)

menu = Menu(details)
details.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="file",menu=filemenu)
filemenu.add_command(label="new")
filemenu.add_command(label="open")
filemenu.add_command(label="edit")
filemenu.add_separator()
filemenu.add_command(label='Exit', command=details.quit)



ttk.Label(details,text="Select Your State",
             font=("Times New Roman",10)).grid(column =0,row=5,padx=10,pady=25)

n=tk.StringVar()
statechoosen =ttk.Combobox(details,width =27,textvariable= n)

#adding combobox drop list down
statechoosen['values'] = ("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
statechoosen.grid(column = 1, row = 5) 
statechoosen.current() 
labeloutput1=Label(details,text="").grid(row=10,column=2)
labeloutput2=Label(details,text="").grid(row=11,column=2)
btnst=Button(details,text="check",command=sumbit)
btnst.grid(row=8,column=5)
btnst=Button(details,text="clear")
btnst.grid(row=9,column=5)


details.mainloop() 





# """
# mainloop()

# from tkinter import *
     
# root = Tk()
# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
#helpmenu.add_command(label='About')
#mainloop()