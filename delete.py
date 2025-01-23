import mysql.connector as c

mydb = c.connect(
  host="localhost",
  user="root",
  password="afreen",
  database="cvr"
)

mycursor = mydb.cursor()

sql = " delete from patience where name='Likitha' "

mycursor.execute(sql)

mydb.commit()
