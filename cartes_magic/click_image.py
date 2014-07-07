import pygame, pygbutton, sys
from pygame.locals import *
from pygame.locals import *

def main():
    FPS = 30
    XMAIN=340
    YMAIN=610
    XCREATURE=0
    YCREATURE=560
    XTERRAIN=0
    YTERRAIN=370
    XSORT=505
    YSORT=370
    pygame.init()
    screen = pygame.display.set_mode((1360,760),RESIZABLE)
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
  #  background = background.convert()
    background=pygame.image.load('fond_plateau2(1220x914).jpg').convert()
    screen.blit(background, (0,0))
    pygame.display.flip()
    cpt=0
    
    ## set-up screen in these lines above ##
    image = '#016.jpg'#016a.jpg
    tab=[]
    tab1=[]
    #button = pygame.image.load('#016a.jpg').convert_alpha()
    tab.append(screen.blit(pygame.image.load('main(100x500).jpg').convert_alpha(),(340,810)))#MAIN
    #tab.append(screen.blit(pygame.image.load('creature(800x1000).jpg').convert_alpha(),(XCREATURE,YCREATURE)))#CREATURE
    tab.append(screen.blit(pygame.image.load('terrain(200x500).jpg').convert_alpha(),(XTERRAIN,YTERRAIN)))#TERRAIN
    tab.append(screen.blit(pygame.image.load('sort(200x500).jpg').convert_alpha(),(XSORT,YSORT)))#SORT

    tab.append(screen.blit(pygame.image.load('#001.jpg').convert_alpha(),(1150,460)))
    tab.append(screen.blit(pygame.image.load('#001.jpg').convert_alpha(),(1010,5)))
    i=0
    for i in range(7):
        tab1.append(screen.blit(pygame.image.load('#016a.jpg').convert_alpha(),(345+cpt,815)))
        cpt= cpt + 70
    pygame.display.flip()
    #tab=[a,b,c,d]
    ## does button need to be 'pygame.sprite.Sprite for this? ##
    ## I use 'get_rect() ##
    

    ## loop to check for mouse action and its position ##
    while 1:
        pos = pygame.mouse.get_pos()
        for carte in tab:
            if carte.collidepoint(pos):
              print(tab.index(carte))
              print('sur carte la carte')
              if tab.index(carte)== 0:
                 for carte1 in tab1:
                   if carte1.collidepoint(pos):
                      print('carte')
                      print(tab1.index(carte1))
                      break
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                ## check if cursor is on button ##
                for carte in tab:
                  if carte.collidepoint(pos):
                    print(tab.index(carte))
                    print('je passe')
                    ## exit ##
                    #return
        #screen.blit(background, (0, 0))
        #screen.blit(pygame.image.load('./cartes_magic/fond_gris2_400.jpg').convert_alpha(),(200,200))
        #screen.blit(pygame.image.load('./cartes_magic/fond_gris2_400.jpg').convert_alpha(),(100,100))
        #screen.blit(pygame.image.load('./cartes_magic/fond_gris2_400.jpg').convert_alpha(),(300,300))
        #screen.blit(pygame.image.load('#001.jpg').convert_alpha(),(1010,325))
        tab[0]
        tab[1]
        tab[2]
        pygame.display.flip()
        pygame.time.Clock().tick(30)
if __name__ == '__main__': main()
