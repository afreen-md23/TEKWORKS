import mysql.connector as c

mydb = c.connect(
  host="localhost",
  user="root",
  password="afreen",
  database="cvr"
)

mycursor = mydb.cursor() 
mycursor.execute(" create table patience(sno int ,name Varchar(220) , age int , gender varchar(220) , problem varchar(220))")
mydb.commit()
