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


#BOUCLE INFINIE
general = 1

while general:
    
    
    fenetre = pygame.display.set_mode((300, 300))
    #fond = pygame.image.load("cartes_magic/fond_gris1.jpg").convert()
    #fenetre.blit(fond, (0,0))
    
    
    continuer_choixPerso = 1
    #Boucle choix perso
    while continuer_choixPerso:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_choixPerso = 0





    for event in pygame.event.get():	#Attente des événements
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            general = 0


"""
#--------- code général ---------------

fenetre = pygame.display.set_mode((800, 790))
#image de fond de la meme taille que la fenetre
fond = pygame.image.load("cartes_magic/fond_plateau.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("cartes_magic/#001.jpg").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)


#Rafraîchissement de l'écran
pygame.display.flip()




#BOUCLE INFINIE
general = 1

while general:
    
    #Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load("").convert()
	fenetre.blit(accueil, (0,0))
    
	#Rafraichissement
	pygame.display.flip()
    
	#On remet ces variables à 1 à chaque tour de boucle
	continuer_choixCarteDeck = 1
	continuer_choixPerso = 1
    continuer_choixLoadPerso = 1
    continuer_choixNewPerso = 1
    continuer_choixDeck = 1
    continuer_choixCarte = 1
        
#------------------------------------------------------------------------------------------
    #Boucle choix perso
    while continuer_choixPerso:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_choixPerso = 0

    #Boucle chargement perso
    while continuer_choixLoadPerso:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_choixLoadPerso = 0


    #Boucle choix create perso
    while continuer_choixNewPerso:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_choixNewPerso = 0

#------------------------------------------------------------------------------------------

    #Boucle choix carte deck
    while continuer_choixCarteDeck:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_choixCarteDeck = 0




    #Boucle choix deck
    while continuer_choixDeck:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_choixDeck = 0



    #Boucle choix carte
    while continuer_choixCarte:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_choixCarte = 0


#------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------
    for event in pygame.event.get():	#Attente des événements
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            general = 0





    #Re-collage
    fenetre.blit(fond,(0,0))
   
    
    #Rafraichissement
    pygame.display.flip()

fenetre = pygame.display.set_mode((640, 480))
"""

