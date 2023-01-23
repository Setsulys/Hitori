
from upemtk import*
from random import randint
from winsound import *


##  Plateau


def debut():
    '''
    cette fonction permet de choisir le niveau via une fenêtre qui explique les règles aux joueurs.
    renvoie le numero du niveau en nb  
    
    
    '''

    
    cree_fenetre(800,
                800)
    texte(400,100,'Bienvenue dans le jeu HITORI',ancrage = 'center', police = 'Helvetica', couleur = 'black', taille = 25,tag = 'txt')
    texte(0,200,'''         Pour y jouer c'est tres simple:
    - une même valeur ne peut apparaitre plus d'une fois sur une ligne ou colonne
    - il faut que toutes les cases blanches soient interconnectés
    - il faut que les cases noires ne soient pas connectés
    
    Un clique gauche grise la case et un clique droit jauni la case 
    Vous permetant de vous repèrer 
    Trouvez des astuces pour vous simplifier la tache !      
    ''',ancrage = 'nw', police = 'Helvetica', couleur = 'black', taille = 15,tag = 'txt')
    
    texte(0,400,'         Avant de commencer choissisez le niveau de difficuté :',ancrage='nw', police ='Helvetica' , couleur = 'black', taille = 15, tag = 'txt')
    i=1
    while i<6:
        rectangle(100*i + 25*i -50 ,450, 100*(i+1) + 25*i-50,550,couleur='black', remplissage='red', epaisseur=2, tag='hitbox_niveau')
        texte((((100*i + 25*i -50 )+(100*(i+1) + 25*i-50))/2),500,str(i),ancrage = 'center', police = 'Helvetica', couleur = 'black', taille = 24,tag ='')
        i+=1
   
    #attends que l'utilisateur rentre un nombre entre 1 et 5 pour les niveaux
    ev= 0
    while (ev != 'ClicGauche') :
        ev=attend_ev()
        
        if type_ev(ev) == 'Quitte':
            ferme_fenetre()
        
        if type_ev(ev)!= "ClicGauche":
            continue
            
        if type_ev(ev) == "ClicGauche" :
                
            
            x,y=abscisse(ev),ordonnee(ev)
            i=1
            niveau=0
            while i <6:
                if (x>(100*i + 25*i -50) and x<(100*(i+1) + 25*i-50)) and (y>450 and y<550):
                    niveau= i
                    break
                i+=1
            if niveau == 0:
                
                continue
            else :
                rectangle(100*i + 25*i -50 ,450, 100*(i+1) + 25*i-50,550,couleur='black', remplissage='yellowgreen', epaisseur=2, tag='hitbox_niveau')
                texte((((100*i + 25*i -50 )+(100*(i+1) + 25*i-50))/2),500,str(i),ancrage = 'center', police = 'Helvetica', couleur = 'black', taille = 24,tag ='')
                break
            
            


    texte(0,700,'         Parfait ! Tout est pret. Appuyer sur la grosse touche entrée pour commencer',ancrage='nw', police ='Helvetica' , couleur = 'black', taille = 15, tag = 'txt')
    
    #attends que l'utilisateurs fasse entrée
    ev=0
    while ev != 'Return' :
        ev=attend_ev()
        ty=type_ev(ev)
        
        if ty == 'Quitte':
            ferme_fenetre()
    
    
        while ty != 'Touche':
            ev=attend_ev()
            ty=type_ev(ev)
        ev=touche(ev)
        
        
        
        
        continue
    
    
    ferme_fenetre()
            
    return niveau


def init_plateau():
    
    '''
    Fonction créant un plateau et le renvoie sous forme de liste  ( nb pour case avec un nombre (plus statue de la case dans un tuple) et X pour case occupée)
    
    
    :param return value: lst
    '''
    plateau=[]
    for i in range(0,nb_ligne+2): #crée le nombre de ligne (en comptabilisant la 1ère ligne qui est juste les "chiffre indicateurs" 1,2,3... + le mur)
        plateau.append([])
        for j in range(0,nb_colonne+2):#crée le nombre de colonne (en comptabilisant la 1ère colonne qui est juste les "letrres indicatrices" A,B,C... + le mur)
            plateau[i].append(0)
            
    #remplace par X les limites du terrain
    for s in range (0,nb_ligne+2):
        plateau[s][0]='X'#1ère colonne(A,B,C...)
        
        plateau[s][nb_colonne+1]='X'#dernière colonne +1 pour créer un "mur"
     
        
    for q in range (0,nb_colonne+2):
        plateau[0][q]='X'#1ère ligne (1,2,3...)
        
        plateau[nb_ligne+1][q]='X'#dernière ligne + 1 pour créer un "mur"
        
        
        
    
    return plateau
    
    
    
def quadrillage():
    '''
    Fonction qui quadrille le plateau selon le nombre de cases et rajoute des informations et de l'hestetique.
    
    
    '''
    rectangle(-1, -1, (nb_colonne+1)*100, (nb_ligne+2)*100,couleur='white', remplissage='skyblue', epaisseur=1, tag='')
    rectangle(100, 100, (nb_colonne+1)*100, (nb_ligne+2)*100,couleur='white', remplissage='white', epaisseur=1, tag='')
    texte((nb_colonne+1)*100/2,50, 'projet: HITORI par Césaire Agonsé et Steven Ly-ieng',
          couleur='navy', ancrage='center', police='Helvetica', taille=20, tag='')
          
    #creation du quadrillage      
    x=100
    for i in range(0,nb_colonne+2):
        ligne(x, 100, x, (nb_ligne+1)*100, couleur='black', epaisseur=2, tag='ligne')
        x+=100
    y=100
    for i in range(0,nb_ligne+2):
        ligne(100, y, (nb_colonne+1)*100, y, couleur='black', epaisseur=2, tag='colonne')
        y+=100
        
    ligne(0, 100, (nb_colonne+1)*100,100 , couleur='navy', epaisseur=5, tag='')    
    ligne(100, 100,100,(nb_ligne+1)*100 , couleur='navy', epaisseur=5, tag='')
    
    #creation de la grille
    for i in range(nb_ligne):
        
        for j in range(nb_colonne):
            texte(140+100*j, 140+100*i,str(grille[i][j]),
                couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                
    #niveau
    
    texte (35,130,"niveau :" ,couleur="navy",ancrage='center', police='Helvetica', taille=15, tag='')
    texte (85,130,str(niveau) ,couleur="darksalmon",ancrage='center', police='Helvetica', taille=18, tag='')
    
    #info grille
    
    texte (30,160,"grille :" ,couleur="navy",ancrage='center', police='Helvetica', taille=15, tag='')
    texte (78,160,str(len(grille))+'x'+str(len(grille)) ,couleur="darksalmon",ancrage='center', police='Helvetica', taille=18, tag='')
    
    #bouton annuler
    rectangle(5, 220, 95, 270,couleur='navy', remplissage='darksalmon', epaisseur=2, tag='')
    texte (50,240,"annuler :" ,couleur="navy",ancrage='center', police='Helvetica', taille=15, tag='')
    
    
    #bouton indice
    rectangle(5, 320, 95, 370,couleur='navy', remplissage='darksalmon', epaisseur=2, tag='')
    texte (50,340,"indice ? :" ,couleur="navy",ancrage='center', police='Helvetica', taille=15, tag='')
    
    
    #bouton solveur
    rectangle(5, 420, 95, 470,couleur='navy', remplissage='darksalmon', epaisseur=2, tag='')
    texte (50,440,"soluce :" ,couleur="navy",ancrage='center', police='Helvetica', taille=15, tag='')
    
    #bouton retour
    rectangle(5, 520, 95, 570,couleur='navy', remplissage='darksalmon', epaisseur=2, tag='')
    texte (50,540,"retour" ,couleur="navy",ancrage='center', police='Helvetica', taille=15, tag='')
    
        
### cases 

def pixel_vers_case(x, y):
    '''
    Cette fontion convertie les coordonées en pixel vers des cases (tuple)
    '''
    x,y=x//100,y//100
    return (x,y)
    
    
def clic_gauche_ou_droit(plateau,retour,coups,noircies_soluce):
    '''
    verifie si on a fait un clic droit ou gauche en cours de jeu, si on clique sur quitter on quite le jeu.
    si on fait un clic droit sur la grille on noircie une case grâce à la fonction noircir_cases(plateau,ev,annuler_lst,coups)
    si on fait un clic gauche sur la grille on jaunie une case grâce à la fonction jaunir_cases(plateau,ev,annuler_lst,coups)
    si on clic sur un bouton une action spéciale est enclenché
    retourn des infos en tuple selon chaque fonction effectuées

    '''
    while True:
        ev=attend_ev()
        
        if type_ev(ev) == 'Quitte':
            ferme_fenetre()
        
            
        if type_ev(ev)!= "ClicGauche" and type_ev(ev) != "ClicDroit":
            continue
        
        elif type_ev(ev ) == "ClicGauche" and (5<abscisse(ev)<95) and (220<ordonnee(ev)<270):
            coups=annuler(annuler_lst,coups)
            return (coups, plateau,None,None)
            
            
        elif type_ev(ev ) == "ClicGauche" and (5<abscisse(ev)<95) and (520<ordonnee(ev)<570):
            retour = True
            return retour
        elif type_ev(ev ) == "ClicGauche" and (5<abscisse(ev)<95) and (420<ordonnee(ev)<470):
            noircies_soluce=solveur(plateau,grille,False,ensemble_indice)
            return (coups,None,None,noircies_soluce)
           
        elif type_ev(ev ) == "ClicGauche" and (5<abscisse(ev)<95) and (320<ordonnee(ev)<370):
            
            solveur(plateau,grille,True,ensemble_indice) 
        elif type_ev(ev) == "ClicGauche" :
            
            if (100<abscisse(ev)) and (100<ordonnee(ev)):
                coups+=1
            return noircir_cases(plateau,ev,annuler_lst,coups)
            
            
        elif type_ev(ev) == "ClicDroit" :
            if (100<abscisse(ev)) and (100<ordonnee(ev)):
                coups+=1
            return jaunir_cases(plateau,ev,annuler_lst,coups)
            
    
   
    

    
def noircir_cases(plateau, ev,annuler_lst,coups):
    '''
    Lorsque l'on clique sur une case de la grille du jeu grace a la fontion clic_droite_gauche case prise en compte se noircie et ses coordonées sont ajoutés dans un ensemble et s'annule si on blanchi la case en recliquant dessus. Une case jaunie peut etre noircie en faisant un clique gauche
    '''
    x,y=(abscisse(ev),ordonnee(ev))
    x,y = pixel_vers_case(x,y)
    
    if plateau[y][x]== 0 or plateau[y][x]== 'j':
        
        
        if x>0 and x<len(grille)+1 and y>0 and y<len(grille)+1:
            rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='silver', epaisseur=2, tag='')
            texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
            
            noircies.add((x,y))
            blanc.discard((x,y))
            
            if plateau[y][x]== 0:
                
                annuler_lst+=[[x,y,"n",0]]
            if plateau[y][x]== 'j':
                annuler_lst+=[[x,y,"n",'j']]
            plateau[y][x]='n'
            
            
    elif plateau[y][x]=='n':
        if x>0 and x<len(grille)+1 and y>0 and y<len(grille)+1:
            rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='white', epaisseur=2, tag='')
            texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
            plateau[y][x]= 0
            if (x,y) in noircies:
                noircies.discard((x,y))
                blanc.add((x,y))
            annuler_lst+=[[x,y,0,"n"]]
   
    
    case=x,y
    return coups,plateau,case,None
    
    
def jaunir_cases(plateau, ev,annuler_lst,coups):
    '''
     Lorsque l'on clique sur une case de la grille du jeu grace a la fontion clic_droite_gauche case prise en compte se jaunie et ses coordonées sont ajoutés dans un ensemble et s'annule si on blanchi la case en recliquant dessus
    '''
    x,y=abscisse(ev),ordonnee(ev)
    x,y = pixel_vers_case(x,y)
    if plateau[y][x] == 0 or plateau[y][x]=='n':
        
        if x>0 and x<len(grille)+1 and y>0 and y<len(grille)+1:
            rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='orange', epaisseur=2, tag='')
            texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
            
            if (x,y) in noircies :
                noircies.discard((x,y))
            if plateau[y][x]== 0:
                
                annuler_lst+=[[x,y,"j",0]]
            if plateau[y][x]== 'n':
                annuler_lst+=[[x,y,"j",'n']]
            plateau[y][x]='j'
            
            
            
    elif plateau[y][x]=='j':
        if x>0 and x<len(grille)+1 and y>0 and y<len(grille)+1:
            rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='white', epaisseur=2, tag='')
            texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
            plateau[y][x]= 0
            annuler_lst+=[[x,y,0,'j']]
    case=x,y
    return coups,plateau,case,None
    


def sans_voisines_noircies(grille, noircies):
    ''' 
    Cette fonction verifie que les cases noircies ne soient pas collées sur les axes verticales et horizontales
    retourne un booleen
    '''
    for element in noircies:
        x,y=element
        if ((x,y) in noircies) and (((x-1,y) in noircies) or ((x+1,y) in noircies) or ((x,y-1) in noircies ) or ((x,y+1) in noircies)):
            return False 
        else:
            continue 
    return True
    
def sansconflit(grille, noircies, x, y, historique):
    ''' 
    Cette fonction verifie que sur chaque ligne et chaque colones les valeurs (apres noircisement) n'appairaisent que une seule fois.
    retourne un booleen
    '''
    for o in range(len(grille)):
        x=0
        #on se place sur la ligne y
        for i in range(len(grille[y])):

            #pour chaque x de la ligne y on regarde si x apparait plusieur fois dans la ligne ou pas 
            for j in range(len(grille[y])):
            
                if grille[y][x]==grille[y][j]:
                    historique+=1
                    if (j+1,y+1) in noircies:
                        historique-=1

            #si historique (donc le nombre de fois que x apparait dans la meme ligne ) = 1 alors tout va bien            
            if historique >1 :
                return False
            historique=0
            
            
            #puis pour chaque x de la ligne y on regarde si x apparait plusieur fois dans la colonne ou pas 
            for k in range(len(grille[y])):
                
                
                if grille[y][x]==grille[k][x]:
                    historique+=1
                    if (x+1,k+1) in noircies:
                        historique-=1
                       
            #si historique (donc le nombre de fois que x apparait dans la meme ligne ) = 1 alors tout va bien 
            if historique >1 :
                return False
            historique=0
            x=x+1
        y=y+1

    return True 
    
    
    
    
    
    
def connex(grille, noircies, x, y, historique):
    '''
    Cette fonction verifie que toutes les cases blanches soient connectés. c'est à dire que aucunes case blanche n'est séparé par un mur de cases noires
    retourne un booleen
    '''
    #si jamais la première case est une case noire
    if (x,y)== (1,1) and ((1,1) in noircies):
        (x,y) = (2,1)

    historique.add((x,y))

    
    #Detecte l'élement à gauche de la zone de recherche
    if (0!= x -1) and ((x-1,y) not in noircies) and ((x-1,y) not in historique):
        connex(grille,noircies,x-1,y,historique)
    
    #Detecte l'élement au dessus de la zone de recherche
    if (0!= y -1) and ((x,y-1) not in noircies) and ((x,y-1) not in historique):
        connex(grille,noircies,x,y-1,historique)
    
    #Detecte l'élement à droite de la zone de recherche
    if (len(grille[x-1])> x ) and ((x+1,y) not in noircies) and ((x+1,y) not in historique):
        connex(grille,noircies,x+1,y,historique)
        
        
    #Detecte l'élement en dessous de la zone de recherche
    if (len(grille[y-1])> y ) and ((x,y+1) not in noircies) and ((x,y+1) not in historique):
        connex(grille,noircies,x,y+1,historique)

    
    
    
    if len(historique) == len(grille)*len(grille[0])-len(noircies):
        return True
    else:
        return False
    
     

    
def verif(plateau,noircies):
    '''
    Cette fonction fait appele aux fontions sans_voisines_noircies, connex, sansconflit
    et permet de verifier que toute les conditions soient respectés pour valider une grille 
    retourne un booleen
    '''

    
    
    if (sans_voisines_noircies(grille,noircies) == True) and (connex(grille,noircies,x=1,y=1,historique=set()) == True) and (sansconflit(grille,noircies,x=0,y=0,historique=0) == True):
        
        return True 
        
    else:
        return False

def annuler(annuler_lst,coups):
    """
    cette fonction est appelée quand on clic sur le bouton annuler. Elle permet donc d'annuler une action
    retourne une liste de tuples qui permet de conaitre la coordonée et de quelle couleur est et était la case. 
    
    """
    if annuler_lst!=[]:

        elem=annuler_lst[len(annuler_lst)-1]
        x=elem[0]
        y=elem[1]
        if elem[2]== "n":

            noircies.discard((x,y))
            blanc.add((x,y))
            if elem[3]==0:
                rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='white', epaisseur=2, tag='')
                texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                    couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                plateau[y][x]=0
            if elem[3]== "j":
                rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='orange', epaisseur=2, tag='')
                texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                    couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                plateau[y][x]='j'
                
                
        if elem[2]== 0:

            
            
            if elem[3]=='j':
                rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='orange', epaisseur=2, tag='')
                texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                    couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                plateau[y][x]='j'
            if elem[3]== "n":
                rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='silver', epaisseur=2, tag='')
                texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                    couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                blanc.discard((x,y))
                noircies.add((x,y))
                plateau[y][x]='n'
            
            
        if elem[2]== "j":
            
            

            
            if elem[3]==0:
                rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='white', epaisseur=2, tag='')
                texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                    couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                plateau[y][x]=0
            if elem[3]== "n":
                rectangle(x*100,y*100, (x+1)*100, (y+1)*100,couleur='black', remplissage='silver', epaisseur=2, tag='')
                texte(140+100*x-100, 140+100*y-100,str(grille[y-1][x-1]),
                    couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                blanc.discard((x,y))
                noircies.add((x,y))
                plateau[y][x]='n'
        
        annuler_lst.pop()
    
        if coups >=1:
            coups-=1
            return (coups)

    
        
        
    else:
        return (coups)
    
    



def bravo(coups):
    '''
    Cette fonction créée une nouvelle fenêtre ou il est affiché bravo et le nombre de coups pour arriver a finir la grille.Elle demande ensuite au joueur si il veut rejouer. Cette fonction s'affiche lorsque toutes les conditions sont respéctés pour valider une grille et que par consequant la fonction verif revoie true.
    '''
    cree_fenetre(800,
                800)
    texte(400,100,'Bravo tu as gagné en '+str(coups)+' coups !!!',ancrage = 'center', police = 'Helvetica', couleur = 'black', taille = 25,tag = 'txt')
    
    if noircies_soluce != set():
        PlaySound('huée.wav', SND_ASYNC)
        texte(400,175,"mais tu as triché en regardant la solution !!!",ancrage = 'center', police = 'Helvetica', couleur = 'red', taille = 25,tag = 'txt')
    
    elif ensemble_indice != set():
        PlaySound('huée.wav', SND_ASYNC)
        if len(ensemble_indice)>1:
            texte(400,175,"mais tu as utilisé "+str(len(ensemble_indice))+" indices.",ancrage = 'center', police = 'Helvetica', couleur = 'red', taille = 25,tag = 'txt')
        else:
            texte(400,175,"mais tu as utilisé "+str(len(ensemble_indice))+" indice.",ancrage = 'center', police = 'Helvetica', couleur = 'red', taille = 25,tag = 'txt')
    elif coups == len(noircies):
        PlaySound('applause.wav', + SND_ASYNC)
        texte(400,175,"Et c'est un perfect !!!",ancrage = 'center', police = 'Helvetica', couleur = 'red', taille = 25,tag = 'txt')
    else:
        PlaySound('clap.wav', + SND_ASYNC)
        texte(400,175,"Cherche un plus haut niveau, jeune Padawan",ancrage = 'center', police = 'Helvetica', couleur = 'red', taille = 25,tag = 'txt')
    
    texte(400,275,'Veux tu rejouer ? ',ancrage = 'center', police = 'Helvetica', couleur = 'black', taille = 25,tag = 'txt')
    
    rectangle(200, 350, 350, 450,couleur='black', remplissage='yellowgreen', epaisseur=2, tag='')
    texte (275,400,"rejouer" ,couleur="black",ancrage='center', police='Helvetica', taille=15, tag='')
    
    rectangle(450, 350, 600, 450,couleur='black', remplissage='red', epaisseur=2, tag='')
    texte (525,400,"quitter" ,couleur="black",ancrage='center', police='Helvetica', taille=15, tag='')
    
    while True:
        ev=attend_ev()
        
        if type_ev(ev) == 'Quitte':
            ferme_fenetre()
            
            
        if type_ev(ev)!= "ClicGauche":
            continue
            
        if type_ev(ev ) == "ClicGauche" and (200<abscisse(ev)<350) and (350<ordonnee(ev)<450):
            fini = False
            ferme_fenetre()
            break 
            
        if type_ev(ev ) == "ClicGauche" and (450<abscisse(ev)<600) and (350<ordonnee(ev)<450):
            fini = True
            ferme_fenetre()
            break
    return fini

def solveur(plateau,grille,indice,ensemble_indice):
    """
    fonction qui est appelée qaund on clic sur les boutons indice et soluce . Et qui permet donc de trouver la solution de la grille ou bien de divulguer un indice.
    crée dans un premier temps des données vierges, detecte toute les cases qui peuvent être noircies, appele la fonction test(lst,lst_0,i,soluce),puis colorie en vert les cases de la solution
    renvoie des infos sous forment de tuple
    """
    
    plateau_bis=init_plateau()
    
    noircies_bis=set()
    historique=0
    noircies_bis_lst=[]
    y=0
    for o in range(len(grille)):
        x=0
        #on se place sur la ligne y
        for i in range(len(grille[y])):

            #pour chaque x de la ligne y on regarde si x apparait plusieur fois dans la ligne ou pas 
            for j in range(len(grille[y])):
                if grille[y][x]==grille[y][j]:
                    historique+=1
                
            #si historique (donc le nombre de fois que x apparait dans la meme ligne ) = 1 alors tout va bien            
            if historique >1 :
                plateau_bis[y+1][x+1]="n"
                
                if (x+1,y+1) not in noircies_bis:
                    noircies_bis_lst+=[(x+1,y+1)]
                noircies_bis.add((x+1,y+1))
            historique=0
            
            
            #puis pour chaque x de la ligne y on regarde si x apparait plusieur fois dans la colonne ou pas 
            for k in range(len(grille[y])):
                
                
                if grille[y][x]==grille[k][x]:
                    historique+=1
                
                    
            #si historique (donc le nombre de fois que x apparait dans la meme ligne ) = 1 alors tout va bien 
            if historique >1 :
                plateau_bis[y+1][x+1]="n"
                
                if (x+1,y+1) not in noircies_bis:
                    noircies_bis_lst+=[(x+1,y+1)]
                noircies_bis.add((x+1,y+1))
            historique=0
            x=x+1
        y=y+1
  
    
    noircies_soluce=test(noircies_bis_lst,[],0,set())

    
    noircir_plateau(noircies_soluce,grille,plateau_bis)
    if (indice == False) :
    
        for i in range(nb_ligne):
            for j in range(nb_colonne):
                
                if (plateau_bis[i+1][j+1] == "n") and ((j+1,i+1) in noircies_soluce ):
                    rectangle((j+1)*100,(i+1)*100, (j+2)*100, (i+2)*100,couleur='black', remplissage='yellowgreen', epaisseur=2, tag='')
                    texte(140+100*(j+1)-100, 140+100*(i+1)-100,str(grille[i][j]),
                        couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                        
        return noircies_soluce

    
    else :

        while True:
            import random
            i = random.randint(0,len(grille)-1)
            
            j = random.randint(0,len(grille[i])-1)
            
            if (plateau_bis[i+1][j+1] == "n") and ((j+1,i+1) in noircies_soluce ) and ((j+1,i+1) not in ensemble_indice):
                rectangle((j+1)*100,(i+1)*100, (j+2)*100, (i+2)*100,couleur='black', remplissage='yellowgreen', epaisseur=2, tag='')
                texte(140+100*(j+1)-100, 140+100*(i+1)-100,str(grille[i][j]),
                    couleur='black', ancrage='nw', police='Helvetica', taille=24, tag='lettres')
                ensemble_indice.add((j+1,i+1))
                break
            elif verif(plateau_bis,ensemble_indice) == True:
                break
        
    
    
    
def test(lst,lst_0,i,soluce):
    """
    fonction qui test toute les possibilités d'ensembles et qui renvoie la première solution trouvée 
    """
    
    while i<len(lst):
        if (soluce != None) and (soluce!= set()):
            break
        
        lst_2=lst_0+[lst[i]]

        issue=liste_vers_emsemble(lst_2)
        

        if verif(plateau,issue) == True :
            
            soluce= issue

            return soluce
            

        
        i+=1

        soluce=test(lst,lst_2,i,soluce)
        if soluce == None:
            soluce = set()
    
    if soluce != set():
        return soluce
    
def noircir_plateau(noircies,grille,plateau_bis):
    """
    fonction qui permet de modifier les cases d'un plateau et les remplacer par des cases noirs ("n") d'un ensemble noircies
    
    
    """
    y=0
    for o in range(len(grille)):
        x=0
        #on se place sur la ligne y
        for i in range(len(grille[y])):
            
            if (x+1,y+1) in noircies:
                
                plateau_bis[y+1][x+1]="n"
            x+=1
        y+=1
    


def liste_vers_emsemble(lst):
    """
    fonction qui recoit une liste de tuples (x,y) et la convertit et la renvoie sous forme d'ensemble
    """
    ensemble= set()
    for i in range(len(lst)):
        ensemble.add(lst[i])
        
    return ensemble


###################################
######   Programme Principal  #####
###################################


if __name__ == "__main__":
    

    
##### initialisation  #######
    dico_grille={
    1:[[5, 3, 1, 5, 3, 2, 6],
    [2, 7, 4, 5, 6, 3, 1],
    [3, 4, 1, 2, 2, 5, 3],
    [4, 1, 7, 6, 5, 4, 2],
    [7, 3, 3, 2, 1, 3, 4],
    [6, 5, 1, 7, 5, 2, 3],
    [1, 2, 5, 4, 7, 1, 5]],
    2:[[8,4, 2, 8, 4, 8, 7, 5],
    [3, 2, 4, 5, 1, 7, 8, 6],
    [5, 3, 7, 4, 5, 6, 4, 1],
    [7, 5, 5, 1, 6, 3, 4, 3, ],
    [5, 1, 2, 4, 7, 5, 2, 8],
    [8, 7, 3, 2, 2, 8, 5, 5],
    [2, 6, 6, 8, 7, 4, 5, 3],
    [7, 4, 1, 2, 6, 5, 6, 7]],
    3:[[1, 7, 3, 6, 5, 2, 4],
    [1, 6, 1, 5, 3, 1, 1],
    [4, 2, 5, 6, 2, 1, 2], 
    [1, 5, 2, 1, 6, 7, 3],
    [5, 5, 1, 3, 2, 3, 4],
    [7, 3, 4, 2, 6, 6, 5],
    [6, 1, 6, 7, 7, 5, 4]],
    4:[[2, 1, 7, 4, 4, 3, 5],
    [7, 7, 4, 2, 6, 3, 4],
    [6, 5, 1, 3, 7, 7, 4],
    [4, 6, 3, 3, 1, 5, 6],
    [4, 2, 1, 1, 7, 4, 2],
    [3, 4, 2, 5, 7, 6, 1],
    [1, 3, 6, 6, 3, 6, 7]],
    5:[[1, 2, 3, 5, 5, 5],
    [4, 3, 1, 6, 2, 4],
    [3, 5, 4, 2, 6, 1],
    [5, 2, 6, 4, 1, 3],
    [1, 1, 6, 2, 3, 2],
    [6, 4, 2, 3, 1, 5]],
    55:[[2,2,1,5,3],
    [2,3,1,4,5],
    [1,1,1,3,5],
    [1,3,5,4,2],
    [5,4,3,2,1]]}
    
    
## boucle semi principale juste pour initialiser les valeurs
    
    while True:
    
        niveau = debut()
        PlaySound('puzzles.wav', SND_ASYNC)
        
       
        
        grille= dico_grille.get(niveau)
        nb_ligne,nb_colonne =len(grille),len(grille[0])
        cree_fenetre((1+nb_colonne)*100,(1+nb_ligne)*100,1000)
        
    
        
        annuler_lst=[]
        coups=0
        
        quadrillage()
        plateau = init_plateau()
        noircies=set()
        noircies_soluce=set()
        ensemble_indice=set()
        blanc=set()
        for x in range(len(grille)):
            for y in range (len(grille[x])):
                blanc.add((x,y))
                
        fini = False
        retour=False
    
####  boucle principale  #####

        while True:
            
            
            
            info=clic_gauche_ou_droit(plateau,retour,coups,noircies_soluce)
            ligne(0, 100, (nb_colonne+1)*100,100 , couleur='navy', epaisseur=5, tag='')    
            ligne(100, 100,100,(nb_ligne+1)*100 , couleur='navy', epaisseur=5, tag='')
            
            
            if info == True:
                ferme_fenetre()
                break
        
            if info[3]!= None:
                
                noircies_soluce=info[3]
            
            coups= info[0]    

            if verif(plateau,noircies)==True:
                ferme_fenetre()
                fini=bravo(coups)
                break
            
            
        if fini == True :
            break

        
    
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        