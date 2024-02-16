import mysql.connector
con=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai__arun"

)
print(con)
result=con.cursor()
#result.execute("show tables")
# result.execute("select*from arun_data")
# result.execute("describe arun_data")
# result.execute("update arun_data "set" address = "3/4 thirupur" "where" s_no=2")
# resultshow=result.fetchall()

for x in resultshow:
    print(x)
