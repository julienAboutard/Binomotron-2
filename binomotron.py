import mariadb
import random

yabinomotron = mariadb.connect(
  host="localhost",
  user="vincent",
  password="Solus4.0",
   database="Binomotron"
)

mycursor = yabinomotron.cursor()
mycursor.execute("SELECT * FROM Students")
students_list = mycursor.fetchall()

# Binomotron to students to groups

# If the list is empty, don't bother
if students_list == [] :
    exit()

# If not, while it's not empty: 
else :
    while students_list != []:
        
        # Assign to groups of 2
        if len(students_list) % 2 == 0 :
            groups = random.sample(students_list, k = 2)
            for g in groups: 
                students_list.remove(g)
            print(f" Binome : {groups[0][0]}, {groups[1][0]}")
            
        # Assign to a group of 3
        else :
            groups = random.sample(students_list, k = 3)
            for g in groups: 
                students_list.remove(g)
            print(f" Trinome : {groups[0][0]}, {groups[1][0]}, {groups[2][0]}")
    exit()