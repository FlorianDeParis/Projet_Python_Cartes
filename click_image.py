import pygame, pygbutton, sys,carte,joueur
from pygame.locals import *
from pygame.locals import *
from carte import *
from joueur import *
from connection import *
from All_fonction import *
import socket, sys, pickle
from joueur import *
XMAIN=260
YMAIN=640
XMAINAD=260
YMAINAD=0
XCREATURE=0
YCREATURE=557
XCREATUREAD=0
YCREATUREAD=103
XTERRAIN=0
YTERRAIN=408
XTERRAINAD=0
YTERRAINAD=187
XSORT=505
YSORT=408
XSORTAD=505
YSORTAD=187
XPIOCHEJOUEUR=5
YPIOCHEJOUEUR=660
XPIOCHEADVERSE=0
YPIOCHEADVERSE=5
XVISUELJO=1010
YVISUELJO=420
XVISUELAD=1010
YVISUELAD=2
TABJOUEUR=[]
TABJOUEUR.append('')
TABJOUEUR.append('')
CONNECT=''
CPTUNIQUECARTE=0

######connexion



HOST = ''
PORT = 40000

################################### change position carte adverse ##########################################
def changePositionAD(background,joueurAD):
	for cartePose in joueurAD.cartePose:
		if (type(cartePose) is creature) or (type(deck[i])is sort):
			cartePose.x=cartePose.x 
			if (cartePose.y>(409+72)):
				cartePose.y=cartePose.y - (225+72)
			else:
				cartePose.y=cartePose.y - 225
			cartePose.rec = background.blit(pygame.image.load(cartePose.url_img).convert_alpha(),(cartePose.x,cartePose.x))
		if (type(cartePose) is terrain):
			cartePose.x=cartePose.x
			cartePose.y=cartePose.y - 379
			cartePose.rec = background.blit(pygame.image.load(cartePose.url_img).convert_alpha(),(cartePose.x,cartePose.x))

################################ fin change position carte adverse ##########################################"
################################ blit all element##########################################"
def refrechelementPose(background,array)
	i=o
	for i in array:
		carte.rec=background.blit(pygame.image.load(i.url_img).convert_alpha(),(i.x,i.y))
#################################" donne les coordonnees au carte ###############################
################################ blit carte	 ##########################################"
def blitCarte(background,carte):
	carte.rec=background.blit(pygame.image.load(carte.url_img).convert_alpha(),(carte.x,carte.y))
#################################" donne les coordonnees au carte #########################################""
def takePosition(background,carte,posx,posy):
	carte.x=posx
	carte.y=posy
	carte.rec=background.blit(pygame.image.load(carte.url_img).convert_alpha(),(carte.x,carte.y))
############################# fin donne les coordonnees au carte #########################################
#################################" change active l'image ou non#########################################""
def activeDeactive(background,carte,posx,posy,urlImg):
	carte.x=posx
	carte.y=posy
	carte.rec=background.blit(pygame.image.load(urlImg).convert_alpha(),(carte.x,carte.y))
############################# fin donne les coordonnees au carte #########################################

##########################"" fenetre dialogue noir##########################################################
def nouvelleFenetre(screen):
	pygame.draw.rect(screen, (0,0,0),(1010, 350,220,70))
	#screen.blit(text1,(1010, 350))
	pygame.display.flip()
##########################"" fenetre dialogue noir##########################################################
##########################"" fenetre visuel carte noir##########################################################
def nouvelleFenetreVisuel(screen):
	pygame.draw.rect(screen, (0,0,0),(XVISUELJO,YVISUELJO,220,300))
	#screen.blit(text1,(1010, 350))
	pygame.display.flip()
##########################"" fenetre visuel carte noir##########################################################

################################################ fenetre de dialogue ###########################################
def fenetreDialoge(screen,text):
	i=0
	pos=0
	pos1=0
	Arraytext=[]
	font = pygame.font.Font(None, 30)
	text1 = font.render('', 1, (150, 10, 150))
	textpos = text1.get_rect()
	longeur=len(text)
	for x in text:
		if(x =='\n'):
			Arraytext.append(text[pos:(i)])
			pos=i+1
		
		elif( x==text[-1]):
			Arraytext.append(text[pos:-1])
		i=i+1
	for y in Arraytext:
		font = pygame.font.Font(None, 30)
		text1 = font.render(y, 1, (150, 10, 150))
		textpos = text1.get_rect()
		screen.blit(text1,(1010, 350+pos1))
		pos1=pos1+25
	pygame.display.flip()
##################################fin de fenetre de dialogue ##################################################

#######################""initilisation background plateau ############################################
def initAffichage(joueur):
	
	pygame.init()
	#screen = pygame.display.set_mode((1220,720),RESIZABLE)
	pygame.mouse.set_visible(1)
	#background = pygame.Surface(screen.get_size())
	#background = background.convert()
	background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
	
    #partie joueur
	background.blit(pygame.image.load('main(100x500).jpg').convert_alpha(),(XMAIN,YMAIN))#MAIN
	background.blit(pygame.image.load('fond_gris2(80x1000).jpg').convert_alpha(),(XCREATURE,YCREATURE))#CREATURE
	background.blit(pygame.image.load('creature(145x500).jpg').convert_alpha(),(XTERRAIN,YTERRAIN))#TERRAIN
	background.blit(pygame.image.load('creature(145x500).jpg').convert_alpha(),(XSORT,YSORT))#SORT
	#background.blit(pygame.image.load('#001.jpg').convert(),(XPIOCHEJOUEUR,YPIOCHEJOUEUR))# pioche joueur
	#background.blit(pygame.image.load('#001.jpg').convert_alpha(),(XPIOCHEADVERSE,YPIOCHEADVERSE))# pioche adverse
	button1=pygbutton.PygButton((XPIOCHEJOUEUR+70, YPIOCHEJOUEUR, 70, 30), 'DECK: '+str(len(joueur[0].bibliotheque)))
	button1.bgcolor = (255,0,0)
	button=pygbutton.PygButton((XPIOCHEJOUEUR+140	, YPIOCHEJOUEUR, 70, 30), 'CIMET: '+str(len(joueur[0].cimetiere)))
	button.bgcolor = (255,0,0)
	button2=pygbutton.PygButton((XPIOCHEJOUEUR+840, YPIOCHEJOUEUR+30, 60, 30), 'FIN')
	button2.bgcolor = (255,0,0)
	button3=pygbutton.PygButton((XPIOCHEJOUEUR+800, YPIOCHEJOUEUR, 150, 30), 'PHASE SUIVANTE')
	button3.bgcolor = (255,0,0)
	font = pygame.font.Font(None, 36)
	text = font.render('VIE: '+joueur[0].pointDeVie, 1, (150, 10, 150))
	textpos = text.get_rect()
	background.blit(text,(XPIOCHEJOUEUR+90, YPIOCHEJOUEUR+30))
    
	button1.draw(background)#####DECK
	button.draw(background)#####CIMET
	button2.draw(background)####FIN
	button3.draw(background)#####PHASE SUIVANTE
	if joueur[0].main!=[]:
		for arraymain in joueur[0].main:
			background.blit(pygame.image.load(arraymain.url_img).convert(),(arraymain.x,arraymain.y))

	if joueur[0].cartePose!=[]:
		for arrayCartePose in joueur[0].cartePose:
			background.blit(pygame.image.load(arrayCartePose.url_img).convert(),(arrayCartePose.x,arrayCartePose.y))
 
	#screen.blit(background, (0,0))

    #partie adverse
	background.blit(pygame.image.load('main(100x500).jpg').convert_alpha(),(XMAINAD,YMAINAD))#MAIN
	background.blit(pygame.image.load('fond_gris2(80x1000).jpg').convert_alpha(),(XCREATUREAD,YCREATUREAD))#CREATURE
	background.blit(pygame.image.load('creature(145x500).jpg').convert_alpha(),(XTERRAINAD,YTERRAINAD))#TERRAIN
	background.blit(pygame.image.load('creature(145x500).jpg').convert_alpha(),(XSORTAD,YSORTAD))#SORT
	#background.blit(pygame.image.load('#001.jpg').convert(),(XPIOCHEJOUEUR,YPIOCHEJOUEUR))# pioche joueur
	#background.blit(pygame.image.load('#001.jpg').convert_alpha(),(XPIOCHEADVERSE,YPIOCHEADVERSE))# pioche adverse
	buttonDeckAD=pygbutton.PygButton((XPIOCHEADVERSE+70, YPIOCHEADVERSE+30, 70, 30), 'DECK: '+str(len(joueur[1].bibliotheque)))
	buttonDeckAD.bgcolor = (255,0,0)
	buttonCimeAD=pygbutton.PygButton((XPIOCHEADVERSE+140, YPIOCHEADVERSE+30, 70, 30), 'CIMET: '+str(len(joueur[1].cimetiere)))
	buttonCimeAD.bgcolor = (255,0,0)
	#buttonFinAD=pygbutton.PygButton((XPIOCHEJOUEURADVERSAIRE+840, YPIOCHEJOUEURADVERSAIRE+30, 60, 30), ' ')
	#buttonFinAD.bgcolor = (255,0,0)
	#buttonPhaseAD=pygbutton.PygButton((XPIOCHEJOUEURADVERSAIRE+800, YPIOCHEJOUEURADVERSAIRE, 30, 30), ' ')
	#buttonPhaseAD.bgcolor = (255,0,0)
	font = pygame.font.Font(None, 36)
	vieAD = font.render('VIE: '+joueur[1].pointDeVie, 1, (150, 10, 150))
	vieADpos = text.get_rect()
	background.blit(vieAD,(XPIOCHEADVERSE+90, YPIOCHEADVERSE+0))

	buttonDeckAD.draw(background)
	buttonCimeAD.draw(background)
	#button2.draw(background)
	#button3.draw(background)
	if joueur[1].main!=[]:
		for arraymain in joueur[1].main:
			background.blit(pygame.image.load(Deck1a.gif).convert(),(arraymain.x,80))

	if joueur[1].cartePose!=[]:
		for arrayCartePose in joueur[0].cartePose:
			background.blit(pygame.image.load(arrayCartePose.url_img).convert(),(arrayCartePose.x,arrayCartePose.y))    
	#fin adverse	

	pygame.display.flip()
	return(background)
#######################""fin   initilisation background plateau ############################################


#################################"debut main#################################################################
def main():
    import pygame, pygbutton, sys,carte,joueur
    from carte import *
    from joueur import *
    
    Arrayjoueur=[]
    Arrayjoueur.append(joueur(1,'paul','12',1000))
    Arrayjoueur.append(joueur(1,'allan','40',5000))
    
    maCarte0 = carte("cauchemard", 10, "#016a.jpg","rouge")
    maCarte1 = carte("cauchemard", 10, "#017a.jpg","rouge")
    maCarte2 = carte("cauchemard", 10, "#018a.jpg","rouge")
    maCarte3 = carte("cauchemard", 10, "#017a.jpg","rouge")
    maCarte4 = carte("cauchemard", 10, "#017a.jpg","rouge")
    maCarte5 = carte("cauchemard", 10, "#017a.jpg","rouge")
    maCarte6 = carte("cauchemard", 10, "#017a.jpg","rouge")
    maCarte7 = carte("cauchemard", 10, "#017a.jpg","rouge")
    Arrayjoueur[0].bibliotheque =[maCarte0,maCarte1,maCarte2,maCarte3]
    Arrayjoueur[1].bibliotheque =[maCarte4,maCarte5,maCarte6,maCarte7]


    pygame.init()
    screen = pygame.display.set_mode((1220,720),RESIZABLE)
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background=pygame.image.load('fond_plateau2(1000x720).jpg')
    screen.blit(background, (0,0))
    pygame.display.flip()




    #####################################  acceuil  ##########################################
    flag=0
    flagClk1=0
    flagVal=0
    while flag!=1:
		#print('principal')
		pos = pygame.mouse.get_pos()
		if(flagClk1==0):
			chargJO=pygbutton.PygButton((300, 300, 150, 150), 'Charger Joueur')
			#buttoncharJO=chargJO.get_rect()
			chargJO.bgcolor = (255,0,0)
			creerJO=pygbutton.PygButton((500, 300, 150, 150), 'Creer Joueur')
			creerJO.bgcolor = (255,0,0)
			chargJO.draw(background)
			creerJO.draw(background)
		for event0 in pygame.event.get():
			#print('etape1')
			#print(event0)
			if event0.type == QUIT:
				pygame.quit()
				sys.exit()
			#if event.type == pygame.MOUSEBUTTONUP and event.chargJO == 1:
			if 'click' in chargJO.handleEvent(event0) :
				#print('je passe')
				flagClk1=1
				flagVal=0
				background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
				while(flagVal==0):
					#print('second boucle')
					fenetreDialoge(screen,'Choix du joueur\n')
					retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
					retour.bgcolor = (255,0,0)
					retour.draw(background)
					valide=pygbutton.PygButton((900, 70, 60, 30), 'Valide ')
					valide.bgcolor = (255,0,0)
					valide.draw(background)
					UserS=selectUser()  ### select all user string
					cptYJO=0
					UserSql=[]
					for User in UserS :
						UserSql.append(pygbutton.PygButton((400, 100+cptYJO, 200, 30), 'Perso:'+User[1]+' XP:'+str(User[2])))
						cptYJO =cptYJO+50
					for User1 in UserSql:
						User1.bgcolor = (255,0,0)
						User1.draw(background)
					for event1 in pygame.event.get():
						#print('etape2')
						#print(event1)
						if event1.type == QUIT:
							pygame.quit()
							sys.exit()
					
						if 'click' in retour.handleEvent(event1) :
							flagClk1=0
							flagVal=1
							nouvelleFenetre(screen)
							background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
							screen.blit(background, (0, 0))
							pygame.display.flip()
						
						for elem in UserSql:####choix joueur
							
							#print('choix joueur')
							if 'click' in elem.handleEvent(event1) :
								index=UserSql.index(elem)
								TABJOUEUR[0]=joueur(index,UserS[index][1],'20',UserS[index][2])
								flagVal=1
								fenetreDialoge(screen,TABJOUEUR[0].nom)
								background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
								nouvelleFenetre(screen)
								flagDeck=0
								while flagDeck==0:####choix deck 
									
									fenetreDialoge(screen,'choix du DECK\n')
									retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
									retour.bgcolor = (255,0,0)
									retour.draw(background)
									vert=pygbutton.PygButton((350, 100, 100, 100), 'VERT ')#VERT 
									vert.bgcolor = (255,0,0)
									vert.draw(background)
									bleu=pygbutton.PygButton((350, 250, 100, 100), 'BLEU ')# BLEU 
									bleu.bgcolor = (255,0,0)
									bleu.draw(background)
									rouge=pygbutton.PygButton((500, 100, 100, 100), 'ROUGE ')#ROUGE 
									rouge.bgcolor = (255,0,0)
									rouge.draw(background)
									blanc=pygbutton.PygButton((500, 250, 100, 100), 'BLANC ')# BLANC 
									blanc.bgcolor = (255,0,0)
									blanc.draw(background)
									noir=pygbutton.PygButton((350, 400, 100, 100), 'NOIR ')#NOIR
									noir.bgcolor = (255,0,0)
									noir.draw(background)
									nouveauDeck=pygbutton.PygButton((500, 400, 100, 100), 'Plus Deck ')#plus de deck
									nouveauDeck.bgcolor = (255,0,0)
									nouveauDeck.draw(background)
									for event1 in pygame.event.get():
										#print('etape2')
										#print(event1)
										if event1.type == QUIT:
											pygame.quit()
											sys.exit()
					
										if 'click' in retour.handleEvent(event1) :
											
											flagVal=0
											flagDeck=1
											nouvelleFenetre(screen)
											background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
											screen.blit(background, (0, 0))
											pygame.display.flip()

										if 'click' in vert.handleEvent(event1) :
											arrayCarteTemp = select_all_carte_type(vert) # carte du mm deck
											background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
											
											flagDeck=1
											flagViewCarte=0
											
											while flagViewCarte==0: ######## visuel de carte du deck
												
												background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
												nouvelleFenetre(screen)
												retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
												retour.bgcolor = (255,0,0)
												retour.draw(background)
												valide=pygbutton.PygButton((900, 70, 60, 30), 'Valide ')
												valide.bgcolor = (255,0,0)
												valide.draw(background)
												posx=2
												posy=110
												for carteDeck in arrayCarteTemp:
													takePosition(background,carteDeck,posx,posy)
													posx= posx+55
													if posx >= 970:
														posx=0
														posy=posy+78
												pos = pygame.mouse.get_pos()#######visuel boucle
												for carte in arrayCarteTemp:
													if carte.rec.collidepoint(pos):
													  #if arrayCarteTemp.index(carte)== 0 :
														urlGrand= carte.url_img[0:-5]+".jpg"
														screen.blit(pygame.image.load(urlGrand).convert_alpha(),(XVISUELJO,YVISUELJO))
														break
													else:
													  screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
												for event1 in pygame.event.get():
													if event1.type == QUIT:
														pygame.quit()
														sys.exit()
					
													if 'click' in retour.handleEvent(event1) :
														flagDeck=0
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														screen.blit(background, (0, 0))
														pygame.display.flip()
													if 'click' in valide.handleEvent(event1) :
														TABJOUEUR[0].bibliotheque=deck_mix_first(arrayCarteTemp)
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
														retour.bgcolor = (255,0,0)
														retour.draw(background)
														connect=pygbutton.PygButton((400, 250, 100, 100), 'Eberger ')#####eberger
														connect.bgcolor = (255,0,0)
														connect.draw(background)
														rechercher=pygbutton.PygButton((400, 400,100, 100), 'Rechercher ')#####rechercher
														rechercher.bgcolor = (255,0,0)
														rechercher.draw(background)
														flagConnect=0
														while flagConnect==0:##########connection
															for event1 in pygame.event.get():
																if event1.type == QUIT:
																	pygame.quit()
																	sys.exit()
					
																if 'click' in retour.handleEvent(event1) :
																	flagViewCarte=0
																	flagConnect=1
																	nouvelleFenetre(screen)
																	nouvelleFenetreVisuel(screen)
																	background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
																	screen.blit(background, (0, 0))
																	pygame.display.flip()
																if 'click' in connect.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='connect'
																if 'click' in rechercher.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='rechercher'
															screen.blit(background, (0, 0))
															pygame.display.flip()
														screen.blit(background, (0, 0))
														pygame.display.flip()
												screen.blit(background, (0, 0))
												pygame.display.flip()
											screen.blit(background, (0, 0))
											pygame.display.flip()

										if 'click' in bleu.handleEvent(event1) :
											arrayCarteTemp = select_all_carte_type(bleu) # carte du mm deck
											background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
											
											flagDeck=1
											flagViewCarte=0
											
											while flagViewCarte==0: ######## visuel de carte du deck
												
												background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
												nouvelleFenetre(screen)
												retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
												retour.bgcolor = (255,0,0)
												retour.draw(background)
												valide=pygbutton.PygButton((900, 70, 60, 30), 'Valide ')
												valide.bgcolor = (255,0,0)
												valide.draw(background)
												posx=2
												posy=110
												for carteDeck in arrayCarteTemp:
													takePosition(background,carteDeck,posx,posy)
													posx= posx+55
													if posx >= 970:
														posx=0
														posy=posy+78
												pos = pygame.mouse.get_pos()#######visuel boucle
												for carte in arrayCarteTemp:
													if carte.rec.collidepoint(pos):
													  #if arrayCarteTemp.index(carte)== 0 :
														urlGrand= carte.url_img[0:-5]+".jpg"
														screen.blit(pygame.image.load(urlGrand).convert_alpha(),(XVISUELJO,YVISUELJO))
														break
													else:
													  screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
												for event1 in pygame.event.get():
													if event1.type == QUIT:
														pygame.quit()
														sys.exit()
					
													if 'click' in retour.handleEvent(event1) :
														flagDeck=0
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														screen.blit(background, (0, 0))
														pygame.display.flip()
													if 'click' in valide.handleEvent(event1) :
														TABJOUEUR[0].bibliotheque=deck_mix_first(arrayCarteTemp)
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
														retour.bgcolor = (255,0,0)
														retour.draw(background)
														connect=pygbutton.PygButton((400, 250, 100, 100), 'Eberger ')#####eberger
														connect.bgcolor = (255,0,0)
														connect.draw(background)
														rechercher=pygbutton.PygButton((400, 400,100, 100), 'Rechercher ')#####rechercher
														rechercher.bgcolor = (255,0,0)
														rechercher.draw(background)
														flagConnect=0
														while flagConnect==0:##########connection
															for event1 in pygame.event.get():
																if event1.type == QUIT:
																	pygame.quit()
																	sys.exit()
					
																if 'click' in retour.handleEvent(event1) :
																	flagViewCarte=0
																	flagConnect=1
																	nouvelleFenetre(screen)
																	nouvelleFenetreVisuel(screen)
																	background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
																	screen.blit(background, (0, 0))
																	pygame.display.flip()
																if 'click' in connect.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='connect'
																if 'click' in rechercher.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='rechercher'
															screen.blit(background, (0, 0))
															pygame.display.flip()
														screen.blit(background, (0, 0))
														pygame.display.flip()
												screen.blit(background, (0, 0))
												pygame.display.flip()
											screen.blit(background, (0, 0))
											pygame.display.flip()

										if 'click' in rouge.handleEvent(event1) :
											arrayCarteTemp = select_all_carte_type(rouge) # carte du mm deck
											background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
											
											flagDeck=1
											flagViewCarte=0
											
											while flagViewCarte==0: ######## visuel de carte du deck
												
												background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
												nouvelleFenetre(screen)
												retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
												retour.bgcolor = (255,0,0)
												retour.draw(background)
												valide=pygbutton.PygButton((900, 70, 60, 30), 'Valide ')
												valide.bgcolor = (255,0,0)
												valide.draw(background)
												posx=2
												posy=110
												for carteDeck in arrayCarteTemp:
													takePosition(background,carteDeck,posx,posy)
													posx= posx+55
													if posx >= 970:
														posx=0
														posy=posy+78
												pos = pygame.mouse.get_pos()#######visuel boucle
												for carte in arrayCarteTemp:
													if carte.rec.collidepoint(pos):
													  #if arrayCarteTemp.index(carte)== 0 :
														urlGrand= carte.url_img[0:-5]+".jpg"
														screen.blit(pygame.image.load(urlGrand).convert_alpha(),(XVISUELJO,YVISUELJO))
														break
													else:
													  screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
												for event1 in pygame.event.get():
													if event1.type == QUIT:
														pygame.quit()
														sys.exit()
					
													if 'click' in retour.handleEvent(event1) :
														flagDeck=0
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														screen.blit(background, (0, 0))
														pygame.display.flip()
													if 'click' in valide.handleEvent(event1) :
														TABJOUEUR[0].bibliotheque=deck_mix_first(arrayCarteTemp)
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
														retour.bgcolor = (255,0,0)
														retour.draw(background)
														connect=pygbutton.PygButton((400, 250, 100, 100), 'Eberger ')#####eberger
														connect.bgcolor = (255,0,0)
														connect.draw(background)
														rechercher=pygbutton.PygButton((400, 400,100, 100), 'Rechercher ')#####rechercher
														rechercher.bgcolor = (255,0,0)
														rechercher.draw(background)
														flagConnect=0
														while flagConnect==0:##########connection
															for event1 in pygame.event.get():
																if event1.type == QUIT:
																	pygame.quit()
																	sys.exit()
					
																if 'click' in retour.handleEvent(event1) :
																	flagViewCarte=0
																	flagConnect=1
																	nouvelleFenetre(screen)
																	nouvelleFenetreVisuel(screen)
																	background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
																	screen.blit(background, (0, 0))
																	pygame.display.flip()
																if 'click' in connect.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='connect'
																if 'click' in rechercher.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='rechercher'
															screen.blit(background, (0, 0))
															pygame.display.flip()
														screen.blit(background, (0, 0))
														pygame.display.flip()
												screen.blit(background, (0, 0))
												pygame.display.flip()
											screen.blit(background, (0, 0))
											pygame.display.flip()

										if 'click' in blanc.handleEvent(event1) :
											arrayCarteTemp = select_all_carte_type(blanc) # carte du mm deck
											background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
											
											flagDeck=1
											flagViewCarte=0
											
											while flagViewCarte==0: ######## visuel de carte du deck
												
												background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
												nouvelleFenetre(screen)
												retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
												retour.bgcolor = (255,0,0)
												retour.draw(background)
												valide=pygbutton.PygButton((900, 70, 60, 30), 'Valide ')
												valide.bgcolor = (255,0,0)
												valide.draw(background)
												posx=2
												posy=110
												for carteDeck in arrayCarteTemp:
													takePosition(background,carteDeck,posx,posy)
													posx= posx+55
													if posx >= 970:
														posx=0
														posy=posy+78
												pos = pygame.mouse.get_pos()#######visuel boucle
												for carte in arrayCarteTemp:
													if carte.rec.collidepoint(pos):
													  #if arrayCarteTemp.index(carte)== 0 :
														urlGrand= carte.url_img[0:-5]+".jpg"
														screen.blit(pygame.image.load(urlGrand).convert_alpha(),(XVISUELJO,YVISUELJO))
														break
													else:
													  screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
												for event1 in pygame.event.get():
													if event1.type == QUIT:
														pygame.quit()
														sys.exit()
					
													if 'click' in retour.handleEvent(event1) :
														flagDeck=0
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														screen.blit(background, (0, 0))
														pygame.display.flip()
													if 'click' in valide.handleEvent(event1) :
														TABJOUEUR[0].bibliotheque=deck_mix_first(arrayCarteTemp)
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
														retour.bgcolor = (255,0,0)
														retour.draw(background)
														connect=pygbutton.PygButton((400, 250, 100, 100), 'Eberger ')#####eberger
														connect.bgcolor = (255,0,0)
														connect.draw(background)
														rechercher=pygbutton.PygButton((400, 400,100, 100), 'Rechercher ')#####rechercher
														rechercher.bgcolor = (255,0,0)
														rechercher.draw(background)
														flagConnect=0
														while flagConnect==0:##########connection
															for event1 in pygame.event.get():
																if event1.type == QUIT:
																	pygame.quit()
																	sys.exit()
					
																if 'click' in retour.handleEvent(event1) :
																	flagViewCarte=0
																	flagConnect=1
																	nouvelleFenetre(screen)
																	nouvelleFenetreVisuel(screen)
																	background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
																	screen.blit(background, (0, 0))
																	pygame.display.flip()
																if 'click' in connect.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='connect'
																if 'click' in rechercher.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='rechercher'
															screen.blit(background, (0, 0))
															pygame.display.flip()
														screen.blit(background, (0, 0))
														pygame.display.flip()
												screen.blit(background, (0, 0))
												pygame.display.flip()
											screen.blit(background, (0, 0))
											pygame.display.flip()

										if 'click' in noir.handleEvent(event1) :
											arrayCarteTemp = select_all_carte_type(noir) # carte du mm deck
											background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
											
											flagDeck=1
											flagViewCarte=0
											
											while flagViewCarte==0: ######## visuel de carte du deck
												
												background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
												nouvelleFenetre(screen)
												retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
												retour.bgcolor = (255,0,0)
												retour.draw(background)
												valide=pygbutton.PygButton((900, 70, 60, 30), 'Valide ')
												valide.bgcolor = (255,0,0)
												valide.draw(background)
												posx=2
												posy=110
												for carteDeck in arrayCarteTemp:
													takePosition(background,carteDeck,posx,posy)
													posx= posx+55
													if posx >= 970:
														posx=0
														posy=posy+78
												pos = pygame.mouse.get_pos()#######visuel boucle
												for carte in arrayCarteTemp:
													if carte.rec.collidepoint(pos):
													  #if arrayCarteTemp.index(carte)== 0 :
														urlGrand= carte.url_img[0:-5]+".jpg"
														screen.blit(pygame.image.load(urlGrand).convert_alpha(),(XVISUELJO,YVISUELJO))
														break
													else:
													  screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
												for event1 in pygame.event.get():
													if event1.type == QUIT:
														pygame.quit()
														sys.exit()
					
													if 'click' in retour.handleEvent(event1) :
														flagDeck=0
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														screen.blit(background, (0, 0))
														pygame.display.flip()
													if 'click' in valide.handleEvent(event1) :
														TABJOUEUR[0].bibliotheque=deck_mix_first(arrayCarteTemp)
														flagViewCarte=1
														nouvelleFenetre(screen)
														nouvelleFenetreVisuel(screen)
														background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
														retour=pygbutton.PygButton((70, 70, 60, 30), 'Retour ')
														retour.bgcolor = (255,0,0)
														retour.draw(background)
														connect=pygbutton.PygButton((400, 250, 100, 100), 'Eberger ')#####eberger
														connect.bgcolor = (255,0,0)
														connect.draw(background)
														rechercher=pygbutton.PygButton((400, 400,100, 100), 'Rechercher ')#####rechercher
														rechercher.bgcolor = (255,0,0)
														rechercher.draw(background)
														flagConnect=0
														while flagConnect==0:##########connection
															for event1 in pygame.event.get():
																if event1.type == QUIT:
																	pygame.quit()
																	sys.exit()
					
																if 'click' in retour.handleEvent(event1) :
																	flagViewCarte=0
																	flagConnect=1
																	nouvelleFenetre(screen)
																	nouvelleFenetreVisuel(screen)
																	background=pygame.image.load('fond_plateau2(1000x720).jpg').convert()
																	screen.blit(background, (0, 0))
																	pygame.display.flip()
																if 'click' in connect.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='connect'
																if 'click' in rechercher.handleEvent(event1) :
																	flagConnect=1
																	flag =1
																	CONNECT='rechercher'
															screen.blit(background, (0, 0))
															pygame.display.flip()
														screen.blit(background, (0, 0))
														pygame.display.flip()
												screen.blit(background, (0, 0))
												pygame.display.flip()
											screen.blit(background, (0, 0))
											pygame.display.flip()

									screen.blit(background, (0, 0))
									pygame.display.flip()
									pygame.time.Clock().tick(30)
								
					#txt="me vois la  passe\n par la et par la\n" #max 20 carractere mettre \n au 20
					#fenetreDialoge(screen,txt)
					fenetreDialoge(screen,'\n \n \n \n')					
					screen.blit(background, (0, 0))
					pygame.display.flip()
					pygame.time.Clock().tick(30)
					
			if 'click' in creerJO.handleEvent(event0) :
				flagClk1=1
				screen.blit(background, (0, 0))
				pygame.display.flip()

				pygame.time.Clock().tick(30)
            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
 		screen.blit(background, (0, 0))
		pygame.display.flip()
        
		#pygame.time.Clock().tick(30)

 ##################################### fin acceuil  ##########################################
    ## set-up screen in these lines above ##
    image = '#016.jpg'#016a.jpg
    tab=[]
    tab1=[]
    tab2=[]
    #button=[]
    #button = pygame.image.load('#016a.jpg').convert_alpha()
    #tab2.append(pygame.image.load('main(100x500).jpg').convert_alpha())
    #tab2.append((XMAIN,YMAIN))#MAIN
    #tab.append(tab2)
    #tab.append(background.blit(pygame.image.load('creature(142x1000).jpg').convert_alpha(),(XCREATURE,YCREATURE)))#CREATURE
    #tab.append(background.blit(pygame.image.load('terrain(142x500).jpg').convert_alpha(),(XTERRAIN,YTERRAIN)))#TERRAIN
    #tab.append(background.blit(pygame.image.load('sort(142x500).jpg').convert_alpha(),(XSORT,YSORT)))#SORT
    

    #allbutton=pygame.Surface(screen.get_size())
    #allbutton=allbutton.convert()
    #allbutton=pygame.image.load('#001.jpg').convert()
    #background.blit(pygame.image.load('#001.jpg').convert(),(XPIOCHEJOUEUR,YPIOCHEJOUEUR))# pioche joueur
    
    button1=pygbutton.PygButton((XPIOCHEJOUEUR+70, YPIOCHEJOUEUR, 60, 30), 'DECK: '+str(len(Arrayjoueur[0].bibliotheque)))
    button1.bgcolor = (255,0,0)
    button=pygbutton.PygButton((XPIOCHEJOUEUR+135	, YPIOCHEJOUEUR, 60, 30), 'CIMET: '+str(len(Arrayjoueur[0].cimetiere)))
    button.bgcolor = (255,0,0)
    button2=pygbutton.PygButton((XPIOCHEJOUEUR+840, YPIOCHEJOUEUR+30, 60, 30), 'FIN')
    button2.bgcolor = (255,0,0)
    button3=pygbutton.PygButton((XPIOCHEJOUEUR+800, YPIOCHEJOUEUR, 150, 30), 'PHASE SUIVANTE')
    button1.draw(background)
    button.draw(background)
    button2.draw(background)
    button3.draw(background)
    
    cpt=0
    i=0
    for i in range(7):
        tab1.append(background.blit(pygame.image.load('#016a.jpg').convert_alpha(),(XSORT+cpt,YSORT)))
        cpt= cpt + 70
    #cpt =0
    #for i in range(7):
        #tab1.append(background.blit(pygame.image.load('#016a.jpg').convert_alpha(),(XSORT+cpt,YSORT+71)))
        #cpt= cpt + 70
    #pygame.display.flip()
    #tab=[a,b,c,d]
    ## does button need to be 'pygame.sprite.Sprite for this? ##
    ## I use 'get_rect() ##
    tab.append(background.blit(pygame.image.load('main(100x500).jpg').convert_alpha(),(XMAIN,YMAIN)))#MAIN
    tab.append(background.blit(pygame.image.load('fond_gris2(80x1000).jpg').convert_alpha(),(XCREATURE,YCREATURE)))#Terrain tab[1]
    tab.append(background.blit(pygame.image.load('creature(145x500).jpg').convert_alpha(),(XTERRAIN,YTERRAIN)))#creature tab[2]
    tab.append(background.blit(pygame.image.load('creature(145x500).jpg').convert_alpha(),(XSORT,YSORT)))#sort tab[3]
    #tab.append(background.blit(pygame.image.load('#001.jpg').convert(),(XPIOCHEJOUEUR,YPIOCHEJOUEUR)))# pioche joueur tab[4]
    #tab.append(background.blit(pygame.image.load('#001.jpg').convert_alpha(),(XPIOCHEADVERSE,YPIOCHEADVERSE)))# pioche adverse tab[5]
    

    #partie adverse
    tab1.append(background.blit(pygame.image.load('fond_gris2(80x1000).jpg').convert_alpha(),(XCREATURE,YCREATURE)))#TERRAIN tab[0]
    tab1.append(background.blit(pygame.image.load('creature(145x500).jpg').convert_alpha(),(XTERRAIN,YTERRAIN)))#CREATURE tab[1]
    tab1.append(background.blit(pygame.image.load('creature(145x500).jpg').convert_alpha(),(XSORT,YSORT)))#SORT tab[2]
    cpt1=0
    ################## avant la boucle placer les 7 ou 6 cartes dans la main de vos joueur########
	##TABJOUEUR[0] est le joueur du pc
	## TABJOUEUR[1] est l adversaire a charger
    cptTour=0
	newCombat = combat()
 ######################################"plateau jeu##################################################
    while 1:
		if cptTour==0:
			posy=YMAIN
			for cptTemp in range(7)
				pioche(TABJOUEUR[0],1,arrayJoMain[cptTemp][0],arrayJoMain[cptTemp][1])
				
            
         ################## nouveau tour####################

################## pose carte ####################
		poseCarte=0
		while poseCarte==0:
			for event in pygame.event.get():
		        if event.type == QUIT:
					   pygame.quit()
					   sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
                
                pos = pygame.mouse.get_pos()
                
                ## check if cursor is on button ##
                for carte in tab:##### parcourt tt les terrain
                  if carte.collidepoint(pos) == tab[0]:#### main
					for cartemain in TABJOUEUR[0].main
						if cartemain.collidepoint(pos)
							if type(cartemain) is terrain: #### si carte est un terrain
								TABJOUEUR[0].cartePose.append(cartemain)
							else:
								if checkManaForPlay(TABJOUEUR[0],cartemain):
									TABJOUEUR[0].cartePose.append(cartemain)
				  if carte.collidepoint(pos) == tab[1]:###### si on a clické sur la partie terrain 
					for cartepose in TABJOUEUR[0].cartePose
						if type(cartepose) is terrain: #### test cest un terrain
							if cartepose.url_img[0]=='a':
								desengagedMana(TABJOUEUR[0], cartepose)
							else 
								engagedMana(TABJOUEUR[0], cartepose)
					#####placé sur le terrain####
                    print(tab.index(carte))
                    print('je passe')
				if 'click' in button3.handleEvent(event) : ##########phase suivante
                	print('ok')
					poseCarte=1
################## fin pose carte ####################

################## debut engagement ####################
		engagementCarte=0
		carteTempsEngage=[]
		carteTempsEngageCreature=[]
		while engagementCarte==0:
			for event in pygame.event.get():
		        if event.type == QUIT:
					   pygame.quit()
					   sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if carte.collidepoint(pos) == tab[1]:###### si on a clické sur la partie terrain 
						for cartepose in TABJOUEUR[0].cartePose
							if type(cartepose) is terrain: #### test cest un terrain
								if checkDesengagedField(TABJOUEUR[0], cartepose):
									desengagedMana(TABJOUEUR[0], cartepose)
								if !checkCardEngaged(TABJOUEUR[0], cartepose):
									engagedMana(TABJOUEUR[0], cartepose)
					if carte.collidepoint(pos) == tab[2]:###### si on a clické sur la creature tab[2]
						for cartepose in TABJOUEUR[0].cartePose
							if type(cartepose) is creature: #### test cest un creature
								if !checkCardEngaged(TABJOUEUR[0], cartepose):
									if checkManaForPlay(TABJOUEUR[0], cartepose):
										engagedAllCarte(TABJOUEUR[0], cartepose) #### engage carte
										carteTempsEngageCreature.append(cartepose) #### ajout dans tableau temp engage carte creature
							if cartepose in carteTempsEngageCreature:
								desengagedAllCarte(TABJOUEUR[0], cartepose) #### desengage carte creature
								del carteTempsEngageCreature[carteTempsEngag.index(cartepose)]

					if carte.collidepoint(pos) == tab[3]:###### si on a clicke sur  sort tab[3]
						for cartepose in TABJOUEUR[0].cartePose
							if type(cartepose) is sort: #### test cest un sort
								if !checkCardEngaged(TABJOUEUR[0], cartepose):
									if checkManaForPlay(TABJOUEUR[0], cartepose):
										engagedAllCarte(TABJOUEUR[0], cartepose) #### engage carte sort
										carteTempsEngage.append(cartepose)### temp sort ajout sort
										flagCible =0
										while flagCible ==0: ########### attend la cible
											for event in pygame.event.get():
												if event.type == QUIT:
													   pygame.quit()
													   sys.exit()
												if event.type == pygame.MOUSEBUTTONDOWN:
													if carte.collidepoint(pos) == tab1[0]:#TERRAIN tab1[0] adverse
														for cartepose1 in TABJOUEUR[1].cartePose
															if testCible(cartepose,type(cartepose1)):
																flagCible =1
													if carte.collidepoint(pos) == tab1[1]:#CREATURE tab[1]
														for cartepose1 in TABJOUEUR[1].cartePose
															if testCible(cartepose,type(cartepose1)):
																flagCible =1
													if carte.collidepoint(pos) == tab1[2]:#CREATURE tab[2]
														for cartepose1 in TABJOUEUR[2].cartePose
															if testCible(cartepose,type(cartepose1)):
																flagCible =1
					if carte.collidepoint(pos) == tab[1]:###### si on a clicke sur la partie terrain 
							if cartepose in carteTempsEngage:
								desengagedAllCarte(TABJOUEUR[0], cartepose) #### desengage carte sort
								del carteTempsEngage[carteTempsEngag.index(cartepose)]
			
	            	if 'click' in button3.handleEvent(event) : ##########phase suivante
			        	engagementCarte=1
			pos = pygame.mouse.get_pos()

################## fin engagement ####################

##################debut attack creature ####################
		selectionCreature =0
		carteTempsEngage=[]
		while selectionCreature ==0:
			for event in pygame.event.get():
		        if event.type == QUIT:
					   pygame.quit()
					   sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					


                if 'click' in button3.handleEvent(event) : ##########phase suivante
			        	selectionCreature =1
                pos = pygame.mouse.get_pos()
			##### juste kil attaque ####
			##### rempli le tableau temporaire####
		newCombat.arrayCreatureAttack=arrayCreature


##################fin attack creature ####################

################## attack sort ####################
		selectionSort=0
		while selectionSort==0:
			for event in pygame.event.get():
		        if event.type == QUIT:
					   pygame.quit()
					   sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
                if 'click' in button3.handleEvent(event) : ##########phase suivante
			        	selectionSort =1
                pos = pygame.mouse.get_pos()
			##### indique la cible######
			##### array (sort,type,cible)   
            #tab1.append(background.blit(pygame.image.load('#016a.jpg').convert_alpha(),(XSORT+cpt,YSORT)))
         newCombat.arrayAction######action##############"
		 newCombat.addArrayInList  
################## fin attack sort ####################
		
		######### utilise des flag pour identifier les phases
		######### charger l adversaire#########################
		######### deangager les carte
        ######### piocher un carte et la placer dans la main du joueur s'il y en a plus de 7 enlever une#####
        ###even mouse IN


		################## fin phase de combat#####################################################
		#######visuel##################
        pos = pygame.mouse.get_pos()
        for carte in tab:
            if carte.collidepoint(pos):
              print(tab.index(carte))
              print('sur carte la carte')
              if tab.index(carte)== 0 and Arrayjoueur[0].main!=[]:
                 for carte1 in Arrayjoueur[0].main:
                   if carte1.rec.collidepoint(pos) :
                      urlGrand= carte1.url_img
                      
                      screen.blit(pygame.image.load(urlGrand).convert_alpha(),(XVISUELJO,YVISUELJO))
                      
                      break
                   else:
                      screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
              elif tab.index(carte)!= 0 and Arrayjoueur[0].cartePose!=[]:
                 for carte1 in Arrayjoueur[0].cartePose:
                   if carte1.rec.collidepoint(pos) :
                      urlGrand= carte1.url_img
                      print(urlGrand)
                      screen.blit(pygame.image.load(urlGrand).convert_alpha(),(XVISUELJO,YVISUELJO))
                      #print('carte')
                      #print(tab1.index(carte1))
                      break
                   else:
                      screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
              else:
                   screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
		
        for field in tab1:
            if field.collidepoint(pos):
              if tab.index(carte)== 0 and Arrayjoueur[1].cartePose!=[]:
                 for carteAD in Arrayjoueur[1].main:
                   if carteAD.rec.collidepoint(pos) :
                      urlGrand= carteAD.url_img
                      screen.blit(pygame.image.load(urlGrand).convert_alpha(),(XVISUELJO,YVISUELJO))
                      break
                   else:
                      screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELAD,YVISUELAD))

		###########fin visuel###################"	

              #fin mouse IN
              #else:
              #screen.blit(pygame.image.load('#001.jpg').convert(),(XVISUELJO,YVISUELJO))
        for event in pygame.event.get():
            if event.type == QUIT:
			       pygame.quit()
			       sys.exit()



            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                print(pos)
                ## check if cursor is on button ##
                for carte in tab:
                  if carte.collidepoint(pos):
                    print(tab.index(carte))
                    print('je passe')
                    ################### ici selection des cartes pour les actions ##########
					### fonction    activeDeactive(background,carte,posx,posy,urlImg)
					####### si on l active ou desactive on change l'urlImg avec 'a' ou 'b' a la fin

            if 'click' in button1.handleEvent(event) and Arrayjoueur[0].bibliotheque != [] :###### deck
               
            if 'click' in button2.handleEvent(event) :######fin
				##### appelle le tableau du joueur adverse#######
				####### redessine le terrain ########
                changePositionAD(background,Arrayjoueur[1])

            if 'click' in button3.handleEvent(event) : ##########phase suivante
                print('ok')
            #if 'click' in button1.handleEvent(event):
                #break

        screen.blit(initAffichage(TABJOUEUR), (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(30)
if __name__ == '__main__': main()
