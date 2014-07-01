import pygame, pygbutton, sys
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
    
    continuerChoixPerso = 1
    continuerCreatePerso = 1
    continuerLoadPerso = 1

    
    #Boucle choix perso
    while continuerChoixPerso:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        fcp = pygame.display.set_mode((300, 300))
        #fond = pygame.image.load("cartes_magic/fond_gris2_300.jpg").convert()
        #fcp.blit(fond, (0,0))
    
        buttonCreatePerso = pygbutton.PygButton((75, 200, 150, 30), 'Nouveau')
        buttonChoixPerso = pygbutton.PygButton((75, 250, 150, 30), 'Chargement')
    
        groupButtons = (buttonChoixPerso, buttonCreatePerso)

        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                buttonChoixPerso = 0
                pygame.quit()
                sys.exit()


            if 'click' in buttonChoixPerso.handleEvent(event):
                print('chargement')
                continuerChoixPerso = 0
                continuerCreatePerso = 0

            if 'click' in buttonCreatePerso.handleEvent(event):
                print('creation')
                continuerLoadPerso = 0
                continuerChoixPerso = 0
 
                

        for b in groupButtons:
            b.draw(fcp)

        pygame.display.update()



 
 
    #Boucle choix perso
    while continuerCreatePerso:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        f_creat = pygame.display.set_mode((300, 300))
        fond = pygame.image.load("cartes_magic/fond_gris1_300.jpg").convert()
        f_creat.blit(fond, (0,0))


 
 
    #Boucle choix perso
    while continuerLoadPerso:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        f_load = pygame.display.set_mode((300, 300))
        fond = pygame.image.load("cartes_magic/fond_gris2_300.jpg").convert()
        f_load.blit(fond, (0,0))




    for event in pygame.event.get():	#Attente des événements
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            general = 0
            pygame.quit()
            sys.exit()


