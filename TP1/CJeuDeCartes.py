#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 22:54:20 2019

@author: cchoquet
"""

import random

class Carte():
    
    def __init__(self, f, c): 
        self.figure = f 
        self.couleur = c
        
    def affiche (self):
        s = self.figure + " de " + self.couleur 
        return (s)

class JeuDeCartes (): 
    
    def __init__(self):
        couleur = ["Pique","Coeur","Carreau","Trèfle"]
        valeur = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]
        #~ Construction de la liste des 52 cartes
        self.cartes=[]
        for coul in couleur: 
            for val in valeur:
                self.cartes.append ( Carte(val,coul) ) 
        return

    #~ Mélange des cartes
    def battre(self): 
        random.shuffle (self.cartes)

    # Tirage la première carte de la pile
    def tirer(self):
        if ( len(self.cartes) == 0 ):
            print ("Plus aucune carte")
            return 
        else:
            t = random.randint (0, len(self.cartes)-1) 
            carte = self.cartes[t]
            del (self.cartes[t]) 
            return (carte)

    # Affichage du jeu de carte
    def afficher (self):
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
