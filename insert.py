import mysql.connector as c

mydb = c.connect(
  host="localhost",
  user="root",
  password="afreen",
  database="cvr"
)

mycursor = mydb.cursor()

sql = "INSERT INTO patience ( sno , name , age , gender ,problem ) VALUES (%s, %s, %s, %s, %s)"
val = [
     (1,'Afreen',20,'female','PCOD'),
     (2,'jagan',19,'male','Headache'),
     (3,'Likitha',19,'female','stomach pain'),
     (4,'Mittu',14,'male','fever'),
     (5,'Raheem'45,'male','backpain'),
     (6,'Musthafa',25,'male','handpain'),
     (7,'Ankitha',22,'female','overweight'),
     (8,'Akhila',21,'female','anxiety')
     ]
      
mycursor.execute(sql, val)

mydb.commit()

