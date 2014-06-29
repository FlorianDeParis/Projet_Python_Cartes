#import pygame
#import sqlite3

from carte import carte
from joueur import joueur
#import carte

monJoueur = joueur(12,"lio",20,100)
maCarte = carte("cauchemard", 10, "ecureuil", "rouge")

print(type(maCarte) is carte)
print(type(maCarte) is joueur)


"""
#pygame.locals import *
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
"""
