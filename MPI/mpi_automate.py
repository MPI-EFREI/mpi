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
            print("L'automate est asynchrone car : ", automate[i][0], automate[i][1], automate[i][2])
            return 1;
            break;
        
#table de transitions
def table_transitions(automate) :
    
    #construire une liste à la taille nécessaire selon l'automate
    
    colonnes = int(automate[0])
    colonnes = colonnes +3
    
    lignes = int(automate[1])
    lignes = lignes+1
    
    table = [] 
    for i in range(lignes):
            table.append([""] * colonnes)
            
    #mettre les noms des colonnes en haut du tableau
            
    for i in range (0, (colonnes+1)) : 
        if i == 0 :
            table[0][i] = "E"
            table[0][i+1] = "S"
            
        if i == colonnes-2 :
            table[0][i] = "a"
            table[0][i+1] = "b"
            
    #mettre la liste des états existants
            
    for i in range (1, lignes) : 
        table[i][2] = i-1
    
    #liste des entrees
    
    cases = int(automate[2][0]) 
    entrees = [] 
    entrees.append([""] * cases)
    
    #savoir quels etats sont des entrees et les mettre dans la liste
    
    e=0
    for i in range(0, cases): 
        entrees[0][i] = automate[2][e+2]
        e = e+2
    
    #liste des sorties
    
    cases2 = int(automate[3][0]) 
    sorties = [] 
    sorties.append([""] * cases2)
    
    #savoir quels etats sont des sorties et les mettre dans la liste
    
    s=0
    for i in range(0, cases2): 
        sorties[0][i] = automate[3][s+2]
        s = s+2
    
    #faire correspondre les entrees et les sorties avec les etats dans la table

    
    for i in range(1, lignes) :
        for j in range(0, cases) :
            if int(table[i][2]) == int(entrees[0][j]) :
                table[i][0] = "e"
            if int(table[i][2]) == int(sorties[0][j]) :
                table[i][1] = "s"
                
                
    i=1
    k=5
    compt=0
    
    while k<15 :
            
        if int(automate[k][0]) == int(table[i][2])  :
            
            if str(automate[k][1]) == str(table[0][3]) :
                print("a")
                table[i][3] = int(automate[k][2])
                k=k+1
                
                    
                
            elif str(automate[k][1]) == str(table[0][4]) :
                print("b")
                table[i][4] = int(automate[k][2])
                k=k+1
                
                
            else :
                print("*")
                k=k+1
            
        else :
            i=i+1
        
    print(table)
    print(k)
    return table
           
                
                

def afficher_table(table):
    
    #afficher la table sous forme de tableau
    
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if table[i][j] == '':
                print(" ", end = " | ")
            else :
                print(table[i][j], end = " | ")
        print("\n------------------")
        



####  MAIN  ####
  
choix = menu_automate()
automate = lire(choix)
afficher(automate)
asynchrone = est_un_automate_asynchrone(automate)
transitions = table_transitions(automate)
afficher_table(transitions)
print(transitions)
os.system("pause")