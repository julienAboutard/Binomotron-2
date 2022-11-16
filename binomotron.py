# import mariadb
import mysql.connector
import random, sys, os.path, json

yabinomotron = mysql.connector.connect(
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

# Query to get the list of students 
mycursor.execute("SELECT First_name, Last_name FROM Students")
students_list = mycursor.fetchall()

mycursor.execute("SELECT id FROM Briefs")
brief_list_temp = mycursor.fetchall()
brief_list =[x[0] for x in brief_list_temp]

# Function Binomotron to put students into random groups for each brief
def binomotron(brief_id) :
    
    if brief_id not in brief_list :
        return f"Il n'existe pas de briefs ayant l'id {brief_id}"
    
    # Query to get the group's length to create groups
    mycursor.execute(f"SELECT Group_Length FROM Briefs where id = {brief_id}")
    group_length=mycursor.fetchone()[0]

    # If the list is empty, the user needs to know
    if students_list == [] :
        return "La table Students est vide ou n'est pas accessible"

    # If it's not empty: 
    else :
        groups_list = []

        if group_length >= len(students_list) :
            groups_list.append([student for student in students_list])

        elif group_length >= len(students_list)/2 and group_length < len(students_list):
            group = []
            for i in range(len(students_list)//2) :
                student = random.choice(students_list)
                group.append(student)
                students_list.remove(student)
            groups_list.append(group)
            groups_list.append([student for student in students_list])
        else :
            while students_list != []:
            
                # Assign to groups of required length
                if len(students_list) >= group_length :
                    groups = random.sample(students_list, k = group_length)
                    groups_list.append(groups) 
                    for g in groups:
                        students_list.remove(g)
                # Assign randomly the rest to other groups
                else :
                    for student in students_list:
                        group =[]
                        while len(group) != group_length :
                            group = random.choice(groups_list)
                        group.append(student)
                        students_list.remove(student)

        # Writing to update groups_list.json
        with open("groups_list.json", 'r') as file :
            group_dictionnary=json.load(file)

        group_dictionnary["Liste des groupes"].update({f"{brief_id}": groups_list})

        with open("groups_list.json", "w") as file :
            json.dump(group_dictionnary, file, indent=4)
    
        return groups_list
    
# Function to get from the JSON the list of groups (if it exists) for a brief's given id
def get_list(brief_id) :

    brief_key=f'{brief_id}'

    if brief_id not in brief_list :
        return f"Il n'existe pas de briefs ayant l'id {brief_id}"

    elif os.path.exists('groups_list.json') :
        with open('groups_list.json', 'r') as file :
            group_dictionnary = json.load(file)
        if brief_key in group_dictionnary['Liste des groupes'].keys() :
            return group_dictionnary['Liste des groupes'].get(brief_key)
        else :
            return f"Il n'existe pas de liste de groupes pour le brief n°{brief_id}"
    else :
        return "Vous n'avez pas encore créé de liste de groupes pour un quelconque brief"
    
    return True
    
# Function to do a print of the groups : displaying the first name of each member of a group 
def print_groups(list_of_groups) :
    
    for group in list_of_groups :
        print("Groupe : " +  ' , '.join(x[0] for x in group))
    
    return None   

# Command line arguments and options    
options = [opt for opt in sys.argv[1:] if opt.startswith("--")]
arguments = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
file = sys.argv[0]

if arguments == [] and options ==[] :
    raise SystemExit(f'Usage: {file} (--list/--create) <id_Brief> OR {file} --help for more help')

# Case where --help is used by the user
if '--help' in options and (len(options) > 1 or len(arguments) == 0):
    print("Pour afficher une liste de groupes pour un brief donné utiliser l'option --list suivie du numéro du brief voulu.")
    print("Pour créer une liste de groupe pour un brief donné utiliser l'option --create suivie du numéro du brief voulu.")
    sys.exit(1)
elif '--help' in options and (len(options) > 1 or len(arguments) != 0) :
    raise SystemExit(f'Usage: {file} (--list/--create) <id_Brief> OR {file} --help for more help')


# To call the Binomotron using command lines: python binomotron.py --create(or --list) <id_brief>(a number, type int)
# We check if id_brief is indeed a numerical argument
if not arguments[0].isnumeric() :
    print("Veuillez renseigner l'id du brief sous forme de nombre")
    sys.exit(1)

else :
    
    brief_id=int(arguments[0])
    
    # Read a command line only if the options (--create/--list) and the argument (<id_brief>) are unique
    # --list is used to get the list of groups for a given brief if this list exists
    if "--list" in options and (len(arguments)==1 and len(options)==1):
        liste = get_list(brief_id)
        if type(liste) == list : 
            print_groups(liste)
            sys.exit(1)
        else : 
            print(liste)
            sys.exit(1)
    
    # --create is used to create a list of groups for a given brief if the groups do not yet exist
    # If the groups already exist, we print a message + the content of the list    
    elif '--create' in options and (len(arguments)==1 and len(options)==1):
        liste = get_list(brief_id)
        if type(liste) == list :
            print("Vous avez déjà créé une liste de groupes pour ce brief\n")
            print('Voici la liste : \n')
            print_groups(liste)
            sys.exit(1)
        else :
            liste = binomotron(brief_id)
            if type(liste) == list : 
                print_groups(liste)
                sys.exit(1)
            else : 
                print(liste)
                sys.exit(1)

    # If no condition is met, print an error message asking the user to use --list or --create with a brief id
    else :
        raise SystemExit(f'Usage: {file} (--list/--create) <id_Brief> OR {file} --help for more help')