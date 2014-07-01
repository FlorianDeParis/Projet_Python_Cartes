import pygame, pygbutton, sys
from pygame.locals import *

pygame.init()



def chooseUserScene():
    continuerChoixPerso = 1
    while continuerChoixPerso:
        pygame.time.Clock().tick(30)

        fcp = pygame.display.set_mode((300, 300))
        #fond = pygame.image.load("cartes_magic/fond_gris2_300.jpg").convert()
        #fcp.blit(fond, (0,0))
        
        buttonCreatePerso = pygbutton.PygButton((75, 200, 150, 30), 'Nouveau')
        buttonChoixPerso = pygbutton.PygButton((75, 250, 150, 30), 'Chargement')
        
        groupButtons = (buttonChoixPerso, buttonCreatePerso)

        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                #buttonChoixPerso = 0
                pygame.quit()
                sys.exit()


            if 'click' in buttonChoixPerso.handleEvent(event):
                print('chargement')
                scene = scenes['loadUserScene']
                continuerChoixPerso = 0
                #continuerCreatePerso = 0

            if 'click' in buttonCreatePerso.handleEvent(event):
                print('creation')
                scene = scenes['newUserScene']
                #continuerLoadPerso = 0
                continuerChoixPerso = 0
     
                    

        for b in groupButtons:
            b.draw(fcp)

        pygame.display.update()
  
  
def newUserScene():
    continuerCreatePerso = 1
    while continuerCreatePerso:
        pygame.time.Clock().tick(30)

        f_creat = pygame.display.set_mode((300, 300))
        fond = pygame.image.load("cartes_magic/fond_gris1_300.jpg").convert()
        f_creat.blit(fond, (0,0))

        pygame.display.update()



def loadUserScene():
    continuerLoadPerso = 1
    while continuerLoadPerso:
        pygame.time.Clock().tick(30)

        f_load = pygame.display.set_mode((300, 300))
        fond = pygame.image.load("cartes_magic/fond_gris2_300.jpg").convert()
        f_load.blit(fond, (0,0))







scenes = {'chooseUser': chooseUserScene(),
          'newUser': newUserScene(),
          'loadUser' : loadUserScene()
          } 

scene = scenes['chooseUser']

def main_game():
  ending=False
  while not ending:
      clock.tick(30)
      for event in pygame.event.get():
         pygame.display.flip()
