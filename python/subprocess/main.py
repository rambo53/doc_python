import subprocess
import os

'''
Permet d'intéragir avec le shell de la machine hôte en lui passant des commandes
capture est pour retourner dans ma variable le résultat de ma commande
universal est pour décoder et afficher le résultat comme un affichage terminal standard

stdout affiche le résultat de ma commande
stderr affiche un message en cas d'erreur de commande
'''	



exit = False

while exit!=True:
    cmd = input(os.getcwd()+"> ")
        
    if "cd" in cmd:
        try:
            os.chdir(cmd.split(" ")[1])
        except FileNotFoundError:
            print("Dossier inexistant.")
            
    elif cmd == "exit":
        exit = True
    else:
        resultat = subprocess.run(cmd, shell=True, capture_output=True, universal_newlines=True)

        print(resultat.stdout)

        print(resultat.stderr)
