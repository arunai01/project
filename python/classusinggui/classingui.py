from tkinter import *
import mysql.connector

app=Tk()
app.title("Student mark List")
app.geometry("300x200")

def DBconnection():
        dpcon=mysql.connector.connect(
        host="192.168.1.240",
        user="AIBATCH01",
        password="AI@123",
        database="ai__arun")
    
        return dpcon

class manuplate:
    def __init__(self):
        #frametop=Frame(app, bg="black",width=800, height=300, padx=10,pady=10)
        #frametop.pack(side = TOP)
        btninsert=Button(app,text="INSERT",command=self.insert)
        btninsert.grid(padx=10, pady=10)
        #btnupdate=Button(frametop,text="UPDATE").pack(padx=10, pady=10)
        #btndelete=Button(frametop,text="DELETE").pack(padx=10, pady=10)

    

    def insert(self):
        my=Tk()
        my.title("update into MySQL DB Demo")
        my.geometry("500x500") 

        frameright=Frame(my, bg="black",width=800, height=800, padx=30,pady=30)
        frameright.grid(row=30,column=30)


        btnsub1=Button(frameright,text="create",font=("Batang",14),fg="White",bg="Green",command=my)
        btnsub1.grid(row=15,column=1)



        lpltitle1=Label(frameright,text="Name",font=("Times of roman",14))
        lpltitle1.grid(row=1,column=1)
        name=Entry(frameright,width=20)
        name.grid(row=1,column=2)

        lpltitle2=Label(frameright,text="Age",font=("Times of roman",14))
        lpltitle2.grid(row=2,column=1)
        lpltitle3=Label(frameright,text="Tamil",font=("Times of roman",14))
        lpltitle3.grid(row=3,column=1)
        lpltitle4=Label(frameright,text="English",font=("Times of roman",14))
        lpltitle4.grid(row=4,column=1)
        lpltitle5=Label(frameright,text="Maths",font=("Times of roman",14))
        lpltitle5.grid(row=5,column=1)
        lpltitle6=Label(frameright,text="physics",font=("Times of roman",14))
        lpltitle6.grid(row=6,column=1)
        lpltitle7=Label(frameright,text="Chemistry",font=("Times of roman",14))
        lpltitle7.grid(row=7,column=1)
        lpltitle8=Label(frameright,text="Compuetr science",font=("Times of roman",10))
        lpltitle8.grid(row=8,column=1)
        lpltitle9=Label(frameright,text="S-no")
        lpltitle9.grid(row=9,column=1)

        age=Entry(frameright,width=20)
        age.grid(row=2,column=2)
        tamil=Entry(frameright,width=20)
        tamil.grid(row=3,column=2)
        english=Entry(frameright,width=20)
        english.grid(row=4,column=2)
        maths=Entry(frameright,width=20)
        maths.grid(row=5,column=2)
        physics=Entry(frameright,width=20)
        physics.grid(row=6,column=2)
        chemistry=Entry(frameright,width=20)
        chemistry.grid(row=7,column=2)
        cs=Entry(frameright,width=15)
        cs.grid(row=8,column=2)
        tbEntryi=Entry(frameright,width=15)
        tbEntryi.grid(row=9,column=2)

        lploutput1=Label(my,text="")
        lploutput1.grid(row=9,column=3)
        lploutput2=Label(frameright,text="")
        lploutput2.grid(row=10,column=3)
        lploutput3=Label(frameright,text="")
        lploutput3.grid(row=11,column=3)
        lploutput4=Label(frameright,text="")
        lploutput4.grid(row=12,column=3)
        lploutput5=Label(frameright,text="")
        lploutput5.grid(row=13,column=3)
        lploutput6=Label(frameright,text="")
        lploutput6.grid(row=14,column=3)
        lploutput7=Label(frameright,text="")
        lploutput7.grid(row=15,column=3)
        lploutput8=Label(frameright,text="")
        lploutput8.grid(row=16,column=3)
        lploutput9=Label(my,text="")
        lploutput9.grid(row=17,column=3)



        a=name.get()
        b=age.get()
        c=tamil.get()
        d=english.get()
        e=maths.get()
        f=physics.get()
        g=chemistry.get()
        h=cs.get()

        e_con=DBconnection()
        result=e_con.cursor()
        #statement="insert into studentmark_list(Name,age,tamil,English,maths,physics,chemistry,computer_science) value(%s,22,%s,%s,%s,77,%s,%s);"

        statement="insert into stdname(a,b,c,d,e,f,g,h) values(" + str(name) + "," + str(age) + ","+str(tamil) + "," + str(english) +","+ str(maths) + "," + str(physics)+","+ str(chemistry) + "," + str(cs)+ ");"
        #valuepass=(a,c,d,e,g,h)
        result.execute(statement)
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


       
        my.mainloop()



run=manuplate()
app.mainloop()