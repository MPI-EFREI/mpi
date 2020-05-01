import os

#afficher les choix dispo
def afficher_menu() :  
    print("Voici la liste des automates disponibles : ")
    print("-----------------")
    print("1 ) Automate 1")
    print("-----------------")
    print("\n")
    
#selection de l'utilisateur
def menu_automate() : 
    saisie = 0
    while saisie != 1 : 
        try : 
            afficher_menu()
            choix = int(input(  "Saisir le numero de l'automate voulu\n"))
            saisie = 1
        except : 
            print("Erreur, veuillez saisir un chiffre")
    return choix

#lecture de l'automate dans le fichier puis insertion de chaque ligne dans une case d'une liste
def lire(choix_automate) :
    if choix_automate == 1 : 
        fichier = open("automate_test.txt", "r")
    
    contenu = fichier.read()
    automate = contenu.split("\n")
    
    fichier.close()
    return automate
 
#afficher l'automate explicitement 
def afficher(automate) : 
    print("Voici l'automate contenu dans le fichier :   ")
    for i in range (0, len(automate)) :
        if i == 0 : 
            print("Nombre de symboles : ", automate[i])
        elif i == 1 : 
            print("Nombre d'etats : ", automate[i])
        elif i == 2: 
            print("Nombre d'etats initiaux :", automate[i][0],"         Etats initiaux : ", end = "")
            for j in range(2, len(automate[i])) : 
                if j % 2 == 0:
                    print(automate[i][j], end = ",  " )
            print()
        elif i == 3: 
            print("Nombre d'etats finaux :", automate[i][0],"         Etats finaux : ", end = "")
            for j in range(2, len(automate[i])) : 
                if j % 2 == 0:
                    print(automate[i][j], end = ",  " )
            print()
        elif i == 4 : 
            print("Nombre de transitions : ", automate[i])
            print("Les transtions ci dessous sont de la forme <etat de depart> <symbole> <etat d'arrivee>")
        
        else :
            print(automate[i])

#test asynchrone on retourne 1 si automate asynchrone 0 sinon        
def est_un_automate_asynchrone(automate) : 
    for i in range(5, len(automate)) :
        if automate[i][1] == "*" : 
            print("L'automate est asynchrone")
            return 1;
            break; 
    
  
choix = menu_automate()
automate = lire(choix)
afficher(automate)
asynchrone = est_un_automate_asynchrone(automate)
os.system("pause")
