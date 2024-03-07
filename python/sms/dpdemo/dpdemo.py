import mysql.connector
from tkinter import *

class DbManupulute:
    def __init__(self):
        print("Wlcome to DpManupulate")

    def returnmsg(self):
        return "connected"

    def mydbconnection(self):
        con=mysql.connector.connect(
            host="192.168.1.240",
            user="AIBATCH01",
            password="AI@123",
            database="ai__arun"
        )
        return con
    
    def insertvalue(self,name,age,tamil,english,maths,physics,chemistry,computer_science):
        student_name=name
        student_age=age
        std_tamil_mk=tamil
        std_eng_mk=english
        std_maths_mk=maths
        std_phy_mk=physics
        std_che_mk=chemistry
        std_cs_mk=computer_science

        data=self.mydbconnection()
        result=data.cursor()

        stmts="INSERT INTO studentmark_list(name,age,tamil,english,maths,physics,chemistry,computer_science) VALUES("+'"'+student_name+'"'+","+str(student_age)+","+str(std_tamil_mk)+","+str(std_eng_mk)+","+str(std_maths_mk)+","+str(std_phy_mk)+","+str(std_che_mk)+","+str(std_cs_mk)+");"

        result.execute(stmts)
        print(stmts)

        data.commit()

        return(str(result.rowcount)+"row inserted")
    
    


    def updatevalue(self, S_no, Name, age, tamil, English, maths, physics, chemistry, computer_science):
        # Assuming you have a database connection stored in self.connection

        data1=self.mydbconnection()
        result1=data1.cursor()


        # Constructing SQL update statement with string concatenation
        update1 = (
            "UPDATE ai__arun.studentmark_list "
            "SET "
            "`S_no` = " + str(S_no) + ", "
            "`Name` = '" + Name + "', "
            "`age` = " + str(age) + ", "
            "`tamil` = " + str(tamil) + ", "
            "`English` = " + str(English) + ", "
            "`maths` = " + str(maths) + ", "
            "`physics` = " + str(physics) + ", "
            "`chemistry` = " + str(chemistry) + ", "
            "`computer_science` = " + str(computer_science) + " "
            "WHERE `S_no` = " + str(S_no)
        )

        # Create a cursor and execute the update query
        #cursor= self.DBconnection.cursor()
        result1.execute(update1)

        print(update1)

        data1.commit()

        # Commit changes to the database
        #self.connection.commit()

    def delevalue(self,S_no):
        data2=self.mydbconnection()
        result2=data2.cursor()


        delete_stmts=(
            "DELETE FROM studentmark_list "
            "WHERE `S_no` = " + str(S_no)

        )
        result2.execute(delete_stmts)
        print(delete_stmts)

        data2.commit()






        