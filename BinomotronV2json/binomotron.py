# import mariadb
import mysql.connector
import random
import json
import os.path

# Function to create from a list of students some random groups with a group's length given
def binomotron(brief_id) :

    yabinomotron=mysql.connector.connect(
    # yabinomotron = mariadb.connect(
    host="localhost",
    user="vincent",
    password="CuissonLente",
    database="Binomotron"
    )

    mycursor = yabinomotron.cursor()

    # Creating groups_list.json if not exist
    if not os.path.exists("groups_list.json"):
        with open("groups_list.json", "w") as file:
            json.dump({"Liste des groupes" : {}}, file, indent=4)
    else :
        pass
    
    # Query to get the list of students 
    mycursor.execute("SELECT First_name, Last_name FROM Students")
    students_list = mycursor.fetchall()

    mycursor.execute("SELECT id FROM Briefs")
    list_brief_temp = mycursor.fetchall()
    list_brief =[x[0] for x in list_brief_temp]

    if brief_id not in list_brief :
        msg = f"Il n'existe pas de briefs ayant l'id {brief_id}"
        return msg
    else :
        pass
    # Query to get the group's length to create groupes
    mycursor.execute(f"SELECT Group_Length FROM Briefs where id = {brief_id}")
    group_length=mycursor.fetchone()

    mycursor.close()

    length = group_length[0]

    

    # Binomotron to students to groups
    group_list=[]
    # If the list is empty, don't bother
    if students_list == [] :
        msg = "La table Students est vide ou n'est pas accessible"
        return msg
    # If not, while it's not empty: 
    else :
        while students_list != []:
            
            # Assign to groups of length
            if len(students_list) % length == 0 :
                groups = random.sample(students_list, k = length)
                group_list.append(groups)
                for g in groups: 
                    students_list.remove(g)
                
            # Assign to a group of length+1 or length-1
            else :
                length_exep= length-1 if length>2 else length+1
                groups = random.sample(students_list, k = length_exep)
                group_list.append(groups)
                for g in groups: 
                    students_list.remove(g)

        # Writing to update groups_list.json
        with open("groups_list.json", 'r') as file :
            group_dict=json.load(file)

        group_dict["Liste des groupes"].update({f"{brief_id}": group_list})

        with open("groups_list.json", "w") as file :
            json.dump(group_dict, file, indent=4)
    
        return group_list

# Function to get from the JSON the list of groups (if it exists) for a brief's id given 
def recuparation_liste(brief_id) :

    brief_key=f'{brief_id}'

    yabinomotron=mysql.connector.connect(
    # yabinomotron = mariadb.connect(
    host="localhost",
    user="user",
    password="1234",
    database="binomotrontest"
    )

    mycursor = yabinomotron.cursor()

    mycursor.execute("SELECT id FROM Briefs")
    list_brief_temp = mycursor.fetchall()
    mycursor.close()
    list_brief =[x[0] for x in list_brief_temp]

    if brief_id not in list_brief :
        msg = f"Il n'existe pas de briefs ayant l'id {brief_id}"
        return msg
    elif os.path.exists('groups_list.json') :
        with open('groups_list.json', 'r') as file :
            group_dict = json.load(file)
        if brief_key in group_dict['Liste des groupes'].keys() :
            brief_groupl = group_dict['Liste des groupes'].get(brief_key)
            return brief_groupl
        else :
            msg = f"Il n'existe pas de liste de groupes pour le briefs ayant l'id {brief_id}"
            return msg
    else :
        msg = "Vous n'avez pas encore créer de liste de groupes pour un quelconque brief"
        return msg
    
    return True

# Function to do a proper print : display First name of each member of a group 
def proper_print(list_of_groups) :
    
    for group in list_of_groups :
        groupe = ' '.join(x[0] for x in group)
        print(groupe)
    
    return None