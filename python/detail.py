from tkinter import *
win=Tk()
win.title("www.personaldetails.com")
win.geometry("500x500+500+500")
win.state("zoomed")

def Submit():
    a=tbEntrya.get()
    b=tbEntryb.get()
    c=tbEntryc.get()
    d=tbEntryd.get()
    e=tbEntrye.get()
    labeloutput1.config(text=a)
    labeloutput2.config(text=b)
    labeloutput3.config(text=c)
    labeloutput4.config(text=d)
    labeloutput5.config(text=e)

def Clear():
    a=" "
    b=" "
    c=" "
    d=" "
    e=" "
    
    
    labeloutput1.config(text=a)
    labeloutput2.config(text=b)
    labeloutput3.config(text=c)
    labeloutput4.config(text=d)
    labeloutput5.config(text=e)


Labeltitle=Label(win,text="Personal Details Form",font=("ALGERIAN",20),fg="Blue")
Labeltitle.grid(row=0,column=25)

label1msg=Label(win,text="Name",font=("Batang",14),fg="black")
label1msg.grid(row=1,column=20,pady=10)
tbEntrya=Entry(win, width=60)
tbEntrya.grid(row=1,column=25)

label2msg=Label(win,text="Gender",font=("Batang",14),fg="black")
label2msg.grid(row=2,column=20,pady=10)
tbEntryb=Entry(win, width=60)
tbEntryb.grid(row=2,column=25)

label3msg=Label(win,text="D.O.B",font=("Batang",14),fg="black")
label3msg.grid(row=3,column=20,pady=10)
tbEntryc=Entry(win, width=60)
tbEntryc.grid(row=3,column=25)

label4msg=Label(win,text="Birth City",font=("Batang",14),fg="black")
label4msg.grid(row=4,column=20,pady=10)
tbEntryd=Entry(win, width=60)
tbEntryd.grid(row=4,column=25)

label5msg=Label(win,text="Phone No.",font=("Batang",14),fg="black")
label5msg.grid(row=5,column=20,pady=10)
tbEntrye=Entry(win, width=60)
tbEntrye.grid(row=5,column=25)

labeloutput1=Label(win,text=" ")
labeloutput1.grid(row=8,column=30,pady=15)
labeloutput2=Label(win,text=" ")
labeloutput2.grid(row=9,column=30,pady=15)
labeloutput3=Label(win,text=" ")
labeloutput3.grid(row=10,column=30,pady=15)
labeloutput4=Label(win,text=" ")
labeloutput4.grid(row=11,column=30,pady=15)
labeloutput5=Label(win,text=" ")
labeloutput5.grid(row=12,column=30,pady=15)

btnsub=Button(win,text="Submit",font=("Batang",14),fg="White",bg="Green",command=Submit)
btnsub.grid(row=7,column=1)

btnclr=Button(win,text="Clear",font=("Batang",14),fg="White",bg="Blue", command=Clear)
btnclr.grid(row=7,column=2)

btnclo=Button(win,text="Close",font=("Batang",14),fg="White",bg="Red")
btnclo.grid(row=7,column=3)

win.mainloop()