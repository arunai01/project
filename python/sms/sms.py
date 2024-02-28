import os
from tkinter  import *
from tkinter import ttk
from dpdemo.dpdemo import *
import mysql.connector



window=Tk()
window.title("Student Mark List")
window.geometry("500x500")
window.state("zoomed")

mydpcon=DbManupulute()


def Exit():
    window.destroy()
#menubar(file,edit,view,help)
menulist=Menu(window,tearoff=0)


def insertdp():
        
        student_name=ety_stdname.get()
        student_age=ety_stdage.get()
        std_tamil_mk=ety_tamil.get()
        std_eng_mk=ety_eng.get()
        std_maths_mk=ety_maths.get()
        std_phy_mk=ety_phy.get()
        std_che_mk=ety_chemi.get()
        std_cs_mk=ety_cs.get()


        x=mydpcon.insertvalue(student_name,student_age,std_tamil_mk,std_eng_mk,std_maths_mk,std_phy_mk,std_che_mk,std_cs_mk)
        lplconmsg.config(text=x)
        selectdates()

def selectdates():
      data=mydpcon.mydbconnection()
      result=data.cursor()
      result.execute("select * from studentmark_list")
    #    select * from ai__arun.studentmark_list;

      i=0
      for ai__arun in result:
            for j in range(len(ai__arun)):
                  lpldispaly=Entry(resultframe,width=10,fg="blue")
                  lpldispaly.grid(row=i,column=j)
                  lpldispaly.insert(END,ai__arun[j])
            i=i+1
      
      




filemenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="File",underline=0,menu=filemenu)
filemenu.add_command(label="New",underline=0,accelerator="Ctrl+N")
filemenu.add_command(label="Open",underline=0,accelerator="Ctrl+O")
filemenu.add_command(label="Save",underline=0,accelerator="Ctrl+S")
filemenu.add_command(label="Save As",underline=5,accelerator="Ctrl+Shift+S")
filemenu.add_separator()
filemenu.add_command(label="Page setup...")
filemenu.add_command(label="Print",underline=0,accelerator="Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=0,accelerator="Ctrl+Q",command=Exit)

editmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Edit",menu=editmenu)

editmenu.add_command(label="Undo",underline=0,accelerator="Ctrl+z")
editmenu.add_command(label="Redo",underline=0,accelerator="Ctrl+Shift+z")
editmenu.add_separator()
editmenu.add_command(label="Copy",underline=0,accelerator="Ctrl+c")
editmenu.add_command(label="Cut",underline=1,accelerator="Ctrl+x")
editmenu.add_command(label="Paste",underline=0,accelerator="Ctrl+v")
editmenu.add_command(label="Paste",underline=0,accelerator="Ctrl+v")
editmenu.add_command(label="Delete",underline=0,accelerator="del")
editmenu.add_separator()
editmenu.add_command(label="Find",underline=0,accelerator="Ctrl+F")
editmenu.add_command(label="Fine Next",underline=0,accelerator="F3")
editmenu.add_command(label="Replace",underline=0,accelerator="Ctrl+H")
editmenu.add_command(label="Go to...",underline=0,accelerator="Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All",underline=0,accelerator="Ctrl+A")
editmenu.add_command(label="Date/time",underline=0,accelerator="Ctrl+F5")


formatmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Format",menu=formatmenu)

formatmenu.add_command(label="Word Wrap")
formatmenu.add_command(label="Font...")

viewmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="View",menu=viewmenu)

viewmenu.add_command(label="Status bar")

aboutmenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="Help",menu=aboutmenu)

aboutmenu.add_command(label="View Help")
aboutmenu.add_separator()
aboutmenu.add_command(label="About notebook")
window.config(menu=menulist)


#image add 
imgdir1=os.path.join((os.path.join(os.path.dirname(__file__),'img')),"Welcome.gif")
gettitleimage=PhotoImage("titleimage",file=imgdir1)

titleImageFrame=Frame(window, bg="black")#, height=200)
titleImageFrame.pack(padx=10,fill="x")

lblDisplayTitleImage=Label(titleImageFrame,image=gettitleimage).pack()



#adding list tabs

tablist=ttk.Notebook(window)
tablist.pack(padx=10,pady=5)

#same size in window frame
tabinsert=ttk.Frame(tablist,width=window.winfo_screenmmwidth(),height=window.winfo_screenmmheight())
tabinsert.pack()

tabupdate=ttk.Frame(tablist,width=window.winfo_screenmmwidth(),height=window.winfo_screenmmheight())
tabupdate.pack()

tabdelete=ttk.Frame(tablist,width=window.winfo_screenmmwidth(),height=window.winfo_screenmmheight())
tabdelete.pack()

tablist.add(tabinsert,text="Insert")
tablist.add(tabupdate,text="Update")
tablist.add(tabdelete,text="Delete")

titledisplayframeintab=Frame(tabinsert,width=window.winfo_screenwidth(), height=window.winfo_screenheight())
titledisplayframeintab.pack()

lpl_insert_title=Label(titledisplayframeintab,text="Inserting Students Mark")
lpl_insert_title.grid(pady=10,row=0,columnspan=10)

lpl_std_name=Label(titledisplayframeintab,text="Studente Name")
lpl_std_name.grid(pady=10,row=1,column=1)
ety_stdname=Entry(titledisplayframeintab)
ety_stdname.grid(pady=10,row=1,column=2)

lpl_std_age=Label(titledisplayframeintab,text="Studente age")
lpl_std_age.grid(pady=10,row=2,column=1)
ety_stdage=Entry(titledisplayframeintab)
ety_stdage.grid(pady=10,row=2,column=2)



lpl_tamil_mrk=Label(titledisplayframeintab,text="Tamil")
lpl_tamil_mrk.grid(pady=10,row=3,column=1)
ety_tamil=Entry(titledisplayframeintab)
ety_tamil.grid(pady=10,row=3,column=2)


lpl_eng_mrk=Label(titledisplayframeintab,text="eng")
lpl_eng_mrk.grid(pady=10,row=4,column=1)
ety_eng=Entry(titledisplayframeintab)
ety_eng.grid(pady=10,row=4,column=2)

lpl_maths_mrk=Label(titledisplayframeintab,text="maths")
lpl_maths_mrk.grid(pady=10,row=5,column=1)
ety_maths=Entry(titledisplayframeintab)
ety_maths.grid(pady=10,row=5,column=2)

lpl_phy_mrk=Label(titledisplayframeintab,text="phy")
lpl_phy_mrk.grid(pady=10,row=6,column=1)
ety_phy=Entry(titledisplayframeintab)
ety_phy.grid(pady=10,row=6,column=2)

lpl_chemi_mrk=Label(titledisplayframeintab,text="chemi")
lpl_chemi_mrk.grid(pady=10,row=7,column=1)
ety_chemi=Entry(titledisplayframeintab)
ety_chemi.grid(pady=10,row=7,column=2)

lpl_cs_mrk=Label(titledisplayframeintab,text="Computer_Science")
lpl_cs_mrk.grid(pady=10,row=8,column=1)
ety_cs=Entry(titledisplayframeintab)
ety_cs.grid(pady=10,row=8,column=2)



btn_insert=Button(titledisplayframeintab,text="Insert",command=insertdp)
btn_insert.grid(row=9,column=1)

btn_update=Button(titledisplayframeintab,text="clear")
btn_update.grid(row=9,column=2)

btn_clear=Button(titledisplayframeintab,text="Exit",command=Exit)
btn_clear.grid(row=9,column=3)

lplconmsg=Label(titledisplayframeintab,text="")
lplconmsg.grid(row=10,column=2,pady=20)

resultframe=Frame(titledisplayframeintab,width=800,height=600,bg="black")
resultframe.grid(row=11,columnspan=6)

#update
titledisplayframeintab=Frame(tabupdate,width=window.winfo_screenwidth(), height=window.winfo_screenheight())
titledisplayframeintab.pack()

lpl_insert_title=Label(titledisplayframeintab,text="Update Students Mark")
lpl_insert_title.grid(pady=10,row=0,columnspan=10)

lpl_std_name1=Label(titledisplayframeintab,text="Studente Name")
lpl_std_name1.grid(pady=10,row=1,column=1)
ety_stdname1=Entry(titledisplayframeintab)
ety_stdname1.grid(pady=10,row=1,column=2)

lpl_std_age1=Label(titledisplayframeintab,text="Student age")
lpl_std_age1.grid(pady=10,row=2,column=1)
ety_stdage1=Entry(titledisplayframeintab)
ety_stdage1.grid(pady=10,row=2,column=2)



lpl_tamil_mrk1=Label(titledisplayframeintab,text="Tamil")
lpl_tamil_mrk1.grid(pady=10,row=3,column=1)
ety_tamil1=Entry(titledisplayframeintab)
ety_tamil1.grid(pady=10,row=3,column=2)


lpl_eng_mrk1=Label(titledisplayframeintab,text="eng")
lpl_eng_mrk1.grid(pady=10,row=4,column=1)
ety_eng1=Entry(titledisplayframeintab)
ety_eng1.grid(pady=10,row=4,column=2)

lpl_maths_mrk1=Label(titledisplayframeintab,text="maths")
lpl_maths_mrk1.grid(pady=10,row=5,column=1)
ety_maths1=Entry(titledisplayframeintab)
ety_maths1.grid(pady=10,row=5,column=2)

lpl_phy_mrk1=Label(titledisplayframeintab,text="phy")
lpl_phy_mrk1.grid(pady=10,row=6,column=1)
ety_phy1=Entry(titledisplayframeintab)
ety_phy1.grid(pady=10,row=6,column=2)

lpl_chemi_mrk1=Label(titledisplayframeintab,text="chemi")
lpl_chemi_mrk1.grid(pady=10,row=7,column=1)
ety_chemi1=Entry(titledisplayframeintab)
ety_chemi1.grid(pady=10,row=7,column=2)

lpl_cs_mrk1=Label(titledisplayframeintab,text="Computer_Science")
lpl_cs_mrk1.grid(pady=10,row=8,column=1)
ety_cs1=Entry(titledisplayframeintab)
ety_cs1.grid(pady=10,row=8,column=2)

lpl_S_no=Label(titledisplayframeintab,text="S_no")
lpl_S_no.grid(pady=10,row=9,column=1)
ety_S_no=Entry(titledisplayframeintab)
ety_S_no.grid(pady=10,row=9,column=2)




btn_insert=Button(titledisplayframeintab,text="Update",command=insertdp)
btn_insert.grid(row=10,column=1)

btn_update=Button(titledisplayframeintab,text="clear")
btn_update.grid(row=10,column=2)

btn_clear=Button(titledisplayframeintab,text="Exit",command=Exit)
btn_clear.grid(row=10,column=3)




window.mainloop()