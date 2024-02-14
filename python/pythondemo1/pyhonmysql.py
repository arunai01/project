import mysql.connector
con=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="a"

)
print(con)
result=con.cursorc,
result.execute("show tables")
resultshow=result.fetchall()

for x in resultshow:
    print(x)
