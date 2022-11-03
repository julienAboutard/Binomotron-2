from ast import arg
import sys
from binomotron import binomotron, recuparation_liste, proper_print

opts = [opt for opt in sys.argv[1:] if opt.startswith("--")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
file = sys.argv[0]

# On attend en command line sous cette forme python main.py --create(or --list) <id_brief>(sous forme de nombre entier)
# On vérifie en premier lieu si l'argument id_brief est bien un nombre entier
if not args[0].isnumeric() :
    print("Veuillez renseigner l'id du brief sous forme de nombre")
    exit()
else :
    brief_id=int(args[0])
    # On prend en compte une command line seulement si l'option(--create/--liste) et l'argument(<id_brief>) sont bien unique
    # L'option --list permet de récupérer la liste des groupes pour un brief donné si elle existe
    if "--list" in opts and (len(args)==1 and len(opts)==1):
        liste = recuparation_liste(brief_id)
        if type(liste) == list : 
            proper_print(liste)
        else : 
            print(liste)
    
    # L'option --create permet de créer une liste de groupe pour un brief donné si elle n'existe pas 
    # Si cette liste existe on envoie un message pour prévenir et on l'affiche(on n'écrase pas la liste déjà créée)
    elif '--create' in opts and (len(args)==1 and len(opts)==1):
        liste = recuparation_liste(brief_id)
        if type(liste) == list :
            print("Vous avez déjà créer un liste de groupe pour ce brief\n")
            print('Voici la liste : \n')
            proper_print(liste)
        else :
            liste = binomotron(brief_id)
            if type(liste) == list : 
                proper_print(liste)
            else : 
                print(liste)

    # Si on ne rentre dans aucune des conditions précédentes on affiche un message d'erreur demandant à l'utilisateur de corriger sa command 
    else :
        raise SystemExit(f'Usage: {file} (--list/--create) <id_Brief>')