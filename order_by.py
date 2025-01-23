import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='afreen',
    database='cvr'
)
mycursor=mydb.cursor()
sql='  select * from patience order by age ASC '
mycursor.execute(sql)
res=mycursor.fetchall()
for x in res:
    print(x)
