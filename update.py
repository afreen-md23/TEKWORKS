import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='afreen',
    database='cvr'
)
mycursor=mydb.cursor()
sql=" update patience set name='Mohammad' where sno=4 "
mycursor.execute(sql)
mydb.commit()
