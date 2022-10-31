import mariadb
import random

yabinomotron = mariadb.connect(
  host="localhost",
  user="vincent",
  password="CuissonLente",
   database="Binomotron"
)

mycursor = yabinomotron.cursor()
mycursor.execute("SELECT * FROM Students")
students_list = mycursor.fetchall()

# Binomotron to put students into random groups for each brief

# If the list is empty, don't bother
if students_list == [] :
    exit()

# If not, while it's not empty: 
else :
    
    group_length = 4
    groups_list = []
    
    while students_list != []:
        
        # Assign to groups
        if len(students_list) % group_length == 0 :
            groups = random.sample(students_list, k = group_length)
            print(groups)
            for g in groups:
                groups_list.append(g) 
                students_list.remove(g)
            #print(f" Binome : {groups[0][0]}, {groups[1][0]}")
            
        # Assign the rest to another group
        else :
            alternative_length = group_length - 1 if group_length > 2 else group_length + 1
            groups = random.sample(students_list, k = alternative_length)
            print(groups)
            for g in groups:
                groups_list.append(g) 
                students_list.remove(g)
            #print(f" Trinome : {groups[0][0]}, {groups[1][0]}, {groups[2][0]}")
    for group in groups_list:
        group_name = ' '.join(x[0] for x in group)
        print(group_name)
    
    exit()