#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 22:57:20 2019

@author: cchoquet
"""

import random

class Carte :#parenthèses inutiles
    
    def __init__(self, f, c): 
        self.figure = f 
        self.couleur = c #mauvaise tabulation
        
    def affiche (self):
        s = self.figure + " de " + self.couleur 
        return(s) #mauvaise tabulation

class JeuDeCartes (): 
    
    def __init__(self):
        couleur = ["Pique","Coeur","Carreau","Trèfle"]
        valeur = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]
        #~ Construction de la liste des 52 cartes
        self.cartes=[]
        #boucle for mal indentée
        for coul in couleur: 
            for val in valeur: #replacement du while par un for
                self.cartes.append(Carte(val,coul))   #remplacement de + par la fonction append
        return

    #~ Mélange des cartes
    def battre(self): 
        random.shuffle(self.cartes)

    # Tirage la première carte de la pile
    def tirer(self):
        if ( len(self.cartes) == 0 ):
            print ("Plus aucune carte")
            return 
        else:
            t = random.randint(0, len(self.cartes)-1) 
            carte = self.cartes[t]
            del(self.cartes[t]) 
            return (carte)

    # Affichage du jeu de carte
    def afficher(self):
        #correction d'indentation
        for carte in (self.cartes):
            print (carte.affiche())

#Test :
#import CJeuDeCartes (inutile ici car un seul et même fichier)
#jeu = CJeuDeCartes.JeuDeCartes ()
jeu = JeuDeCartes ()            
jeu.afficher()
input ("Nous allons mélanger le jeu de cartes")
jeu.battre() 
jeu.afficher()
input ("Nous allons tirer les cartes une à une")
for i in range (52):
    c = jeu.tirer ()
    print ("Je viens de tirer la carte : %s" % (c.affiche()))
