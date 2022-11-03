import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="vincent",
  password="CuissonLente",
  database="Binomotron"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT First_name, Last_name FROM Students")

group_list = mycursor.fetchall()

for i in range(1, mycursor.rowcount//3):
  binome = random.sample(group_list, k=3)
  for j in binome:
    group_list.remove(j)
  print(binome)
print(group_list)
