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
    
    def updatetvalue(self,S_no,name,age,tamil,english,maths,physics,chemistry,computer_science):
        student_S_no=S_no
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

         # Replace CONCAT with regular string concatenation
        update_query = (
        "UPDATE students "
        "SET name = name + %s, age = age + %s, tamil = tamil + %s, "
        "english = english + %s, maths = maths + %s, "
        "physics = physics + %s, chemistry = chemistry + %s, "
        "computer_science = computer_science + %s "
        "WHERE S_no = %s"
        )

        values = (student_name, student_age, std_tamil_mk, std_eng_mk, std_maths_mk,
              std_phy_mk, std_che_mk, std_cs_mk, student_S_no)

        result.execute(update_query, values)

    # Commit the changes
        data.commit()
