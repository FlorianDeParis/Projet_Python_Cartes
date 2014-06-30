import pygame
#import sqlite3

"""
from carte import *
from joueur import *
#import carte

monJoueur = joueur(12,"lio",20,100)
maCarte = carte("cauchemard", 10, "ecureuil", "rouge")

print(type(maCarte) is carte)
print(type(maCarte) is joueur)
"""


#pygame.locals import *
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((800, 790))
#image de fond de la meme taille que la fenetre
fond = pygame.image.load("cartes_magic\fond_plateau.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("cartes_magic\#001.jpg").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)


#Rafraîchissement de l'écran
pygame.display.flip()




#BOUCLE INFINIE
continuer = 1

while continuer:
    for event in pygame.event.get():	#Attente des événements
        if event.type == QUIT:
            continuer = 0
    
        #si c'est un event souris
        if event.type == MOUSEMOTION:
            if event.buttons[0] == 1:
                continuer = 0
                 
            if event.button == 1:	#Si clic gauche
                #On change les coordonnées du perso
                perso_x = event.pos[0]
                perso_y = event.pos[1]
             
        #si c'est un event clavier
        if event.type == KEYDOWN:


    #Re-collage
    fenetre.blit(fond, (0,0))
    #fenetre.blit(perso, position_perso)
    fenetre.blit(perso, (perso_x, perso_y))
    
    #Rafraichissement
    pygame.display.flip()
        