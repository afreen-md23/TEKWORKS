import mysql.connector as c

mydb = c.connect(
  host="localhost",
  user="root",
  password="afreen",
  database="cvr"
)

mycursor = mydb.cursor()

sql = "DROP TABLE  patience"

mycursor.execute(sql) 
mydb.commit()
