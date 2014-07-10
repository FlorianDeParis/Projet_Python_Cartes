import sqlite3
from carte import*
from creature import*
from terrain import*
from sort import*

################ creation data base############""
def create_table(fichier):
	#fichierDonnees ="./magic_projet.sql"
	conn =sqlite3.connect('magic_carte.sql')
	#sstr=''
	#f = open ( fichier , 'r' ) 
	#for i in f:

		#for c in i:
			#if c==' ':
	cur = conn.cursor () 
	#cur.execute ( ''' CREATE TABLE COUT_INVOQUE
   #(
#   ID_COUT SMALLINT NOT 0 ,
#   ID_CARTE SMALLINT NOT 0 ,
#   COUT_ROUGE SMALLINT  ,
 #  COUT_BLANC SMALLINT  ,
#   COUT_NOIR SMALLINT  ,
#   COUT_BLEU SMALLINT  ,
#   COUT_VERT SMALLINT  ,
#   COUT_MULTI SMALLINT  
#,
#     PRIMARY KEY (ID_COUT) CONSTRAINT PK_COUT_INVOQUE
#   ) ''' )
#
	
#	cur.execute ( '''CREATE TABLE CARTE
#   (
#   ID_CARTE SMALLINT NOT 0 ,
#   NOM_CARTE CHAR(32)  ,
#   TYPE_CARTE SMALLINT  ,
#   URL_IMAGE VARCHAR(128)  ,
#   COULEUR_CARTE VARCHAR(128)  ,
#   ATTACK SMALLINT  ,
#   DEFENSE SMALLINT  ,
 #  FONCTION_LIEE CHAR(32)  ,
#   CIBLE SMALLINT  ,
#   CREATURE SMALLINT  ,
#   JOUEUR SMALLINT  
#,
#     PRIMARY KEY (ID_CARTE) CONSTRAINT PK_CARTE
#  )
# ''' )
#	cur.execute ( '''CREATE TABLE APPORT_MANA
#   (
#   ID_MANA SMALLINT NOT 0 ,
#   ID_CARTE SMALLINT NOT 0 ,
#   APPORT_ROUGE SMALLINT  ,
#   APPORT_BLANC SMALLINT  ,
#   APPORT_NOIR SMALLINT  ,
#   APPORT_BLEU SMALLINT  ,
#   APPORT_VERT SMALLINT  
#,
#     PRIMARY KEY (ID_MANA) CONSTRAINT PK_APPORT_MANA
#   )  ''' )

#	cur.execute ( '''CREATE TABLE PERSO
#   (
#   ID_PERSO SMALLINT NOT 0 ,
#   PSEUDO VARCHAR(128)  ,
#   XP INTEGER  
#,
#     PRIMARY KEY (ID_PERSO) CONSTRAINT PK_PERSO
#   )  ''' )

#	cur.execute ( '''CREATE TABLE DECK
#   (
#   ID_DECK SMALLINT NOT 0 ,
#   NAME VARCHAR(128)  
#,
#     PRIMARY KEY (ID_DECK) CONSTRAINT PK_DECK
#   ) ''' )

#	cur.execute ( ''' CREATE TABLE LIE
#   (
#   ID_DECK SMALLINT NOT 0 ,
#   ID_CARTE SMALLINT NOT 0 ,
#   QUANTITE_CARTE SMALLINT  
#,
#     PRIMARY KEY (ID_DECK, ID_CARTE) CONSTRAINT PK_LIE
#   ) ''' )

#	cur.execute ( ''' CREATE TABLE APPARTIEN
#   (
#   ID_PERSO SMALLINT NOT 0 ,
#   ID_DECK SMALLINT NOT 0 
#,
#     PRIMARY KEY (ID_PERSO, ID_DECK) CONSTRAINT PK_APPARTIEN
#   ) ''' )	
#	cur.execute ( ''' CREATE  INDEX I_FK_COUT_INVOQUE_CARTE
#     ON COUT_INVOQUE (ID_CARTE ASC)''')
#	cur.execute ( '''CREATE  INDEX I_FK_APPORT_MANA_CARTE
 #    ON APPORT_MANA (ID_CARTE ASC) ''')

#
#	cur.execute ( '''CREATE  INDEX I_FK_LIE_DECK
 #    ON LIE (ID_DECK ASC) ''')
#	cur.execute ( '''CREATE  INDEX I_FK_LIE_CARTE
#     ON LIE (ID_CARTE ASC) ''')
#	cur.execute ( '''CREATE  INDEX I_FK_APPARTIEN_PERSO
#     ON APPARTIEN (ID_PERSO ASC) ''')
#	cur.execute ( '''CREATE  INDEX I_FK_APPARTIEN_DECK
 #    ON APPARTIEN (ID_DECK ASC) ''')
	


	conn.commit()
			#else:
				#sstr+=c
	#str = f.read () 
	

	#conn.commit()
	cur.close() 
	conn.close() 

################################# insert bdd############################""
def insertinbdd():
	conn =sqlite3.connect('magic_carte.sql')
	cur = conn.cursor () 
	cur.execute ("""INSERT INTO  CARTE  (ID_CARTE ,  NOM_CARTE ,  TYPE_CARTE ,  URL_IMAGE ,  COULEUR_CARTE ,  ATTACK ,  DEFENSE ,  FONCTION_LIEE )
VALUES (%s  ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s)""",[
	(1,"Garde moustique",2,"#002.jpg","blanc",1,1,"initiative"),
	(2,"Pecheuse celeste kor",2,"#003.jpg","blanc",2,3,"vol"),
	(3,"Chasseciel leonin",2,"#004.jpg","blanc",2,2,"vol"),
	(4,"Voyage vers le neant",3,"#005.jpg","blanc",0,0,0),
	(5,"Filins prismatiques",5,"#006.jpg","blanc",0,0,0),
	(6,"Legionnaire de porcelaine",2,"#007.jpg","blanc",3,1,"lien de vie"),
	(7,"Sonner alarme",5,"#008.jpg","blanc",0,0,0),
	(8,"Faucon escadron",2,"#009.jpg","blanc",1,1,"vol"),
	(9,"Missionnaire solitaire",2,"#010.jpg","blanc",2,1,"pietinement"),
	(10,"Lynx des steppes",2,"#011.jpg","blanc",0,1,0),
	(11,"Immensite terramorphe",1,"#012.jpg","blanc",0,0,0),
	(12,"Golem de rasoirs",2,"#013.jpg","incolor",3,4,0),
	(13,"Plaine",1,"#014.jpg","blanc",0,0,0),
	(14,"Javelimier Icatian",2,"#015.jpg","blanc",1,1,0),
	(15,"Preceptrice eclairee",5,"#016.jpg","blanc",0,0,0),
	(16,"Mystique forgepierre",2,"#017.jpg","blanc",1,2,"imblocable"),
	(17,"Maitre de etherium",2,"#018.jpg","bleu",6,6,0),
	(18,"Scrige du caveau",2,"#019.jpg","noir",1,1,"vol"),
	(19,"Tezzeret agent de bolas",3,"#020.jpg","noir",0,0,0),
	(20,"Devastateur entravarc",2,"#021.jpg","incolor",1,1,"indestructible"),
	(21,"blindage cranien",3,"#022.jpg","incolor",0,0,0),
	(22,"Nexus des encrimites",1,"#023.jpg","incolor",0,0,0),
	(23,"Champion grave",2,"#024.jpg","bleu",2,2,"distortion"),
	(24,"Citadelle de sombracier",1,"#025.jpg","incolor",0,0,0),
	(25,"Memnite",2,"#026.jpg","bleu",1,1,0),
	(26,"Mox opale",1,"#027.jpg","incolor",0,0,0),
	(27,"Tambour de sautefeuille",3,"#028.jpg","incolor",0,0,0),
	(28,"Ancienne taniere",1,"#029.jpg","blanc",0,0,0),
	(29,"Ornithoptere",2,"#030.jpg","incolor",0,2,"vol"),
	(30,"Siege du synode",1,"#031.jpg","bleu",0,0,0),
	(31,"Adjuration des pensees",4,"#032.jpg","bleu",0,0,0),
	(32,"Caveau des chuchotements",1,"#033.jpg","noir",0,0,0)])
	conn.commit()
	cur.close() 
	conn.close() 

#######################select tte les cartes #########################
def select_all_carte():
	allcarte = []
	fichierDonnees ="./magic_projet.sql"
	conn =sqlite3.connect('magic_carte.sql') 
	cur =conn.cursor()
	i=0
	#def __init__(self, nomCarte, idCarte, url_img, couleurCarte)
	#  ID_CARTE SMALLINT NOT 0 ,    NOM_CARTE CHAR(32)  ,TYPE SMALLINT  ,   URL_IMAGE VARCHAR(128)  ,  
#	COULEUR_CARTE VARCHAR(128)  ,    ATTACK SMALLINT  ,    DEFENSE SMALLINT  ,    FONCTION_LIEE CHAR(32)  
	for row in cur.execute('SELECT NOM_CARTE,ID_CARTE, URL_IMAGE,COULEUR_CARTE,TYPE_CARTE,ATTACK,DEFENSE,FONCTION_LIEE FROM carte '):
		print(row)
		if (row[4]==1) :
			allcarte.append(terrain(row[0],row[1],row[2],row[3],row[6])) #recuperer le mana a la place de row[6]
		elif (row[4]==2) :#carte type monstre et sort (provisoir en attente de la methode d'identification des 
			allcarte.append(creature(row[0],row[1],row[2],row[3],row[5],row[6],row[7])) #recuperer la caracteristique a la place de row[7]
		elif (row[4]==3):
			allcarte.append(sort(row[0],row[1],row[2],row[3],row[6]))#recuperer la caracteristique a la place de row[6]
		i=i+1
	cur.close() 
	conn.close() 
	return allcarte


def select_all_carte_type(couleurDeck):
	allcarte = []
	'''fichierDonnees ="./magic_projet.sql"
	conn =sqlite3.connect('magic_carte.sql') 
	cur =conn.cursor()
	i=0
	#def __init__(self, nomCarte, idCarte, url_img, couleurCarte)
	#  ID_CARTE SMALLINT NOT 0 ,    NOM_CARTE CHAR(32)  ,TYPE SMALLINT  ,   URL_IMAGE VARCHAR(128)  ,  
#	COULEUR_CARTE VARCHAR(128)  ,    ATTACK SMALLINT  ,    DEFENSE SMALLINT  ,    FONCTION_LIEE CHAR(32)  
	for row in cur.execute('SELECT NOM_CARTE,ID_CARTE, URL_IMAGE,COULEUR_CARTE,TYPE_CARTE,ATTACK,DEFENSE,FONCTION_LIEE FROM carte '):
		print(row)
		if (row[4]==1) :
			allcarte.append(terrain(row[0],row[1],row[2],row[3],row[6])) #recuperer le mana a la place de row[6]
		elif (row[4]==2) :#carte type monstre et sort (provisoir en attente de la methode d'identification des 
			allcarte.append(creature(row[0],row[1],row[2],row[3],row[5],row[6],row[7])) #recuperer la caracteristique a la place de row[7]
		elif (row[4]==3):
			allcarte.append(sort(row[0],row[1],row[2],row[3],row[6]))#recuperer la caracteristique a la place de row[6]
		i=i+1
	cur.close() 
	conn.close()'''
	maCarte0 = carte("cauchemard", 10, "#016a.jpg","rouge")
	maCarte1 = carte("cauchemard", 10, "#017a.jpg","rouge")
	maCarte2 = carte("cauchemard", 10, "#018a.jpg","rouge")
	maCarte3 = carte("cauchemard", 10, "#017a.jpg","rouge")
	maCarte4 = carte("cauchemard", 10, "#017a.jpg","rouge")
	maCarte5 = carte("cauchemard", 10, "#017a.jpg","rouge")
	maCarte6 = carte("cauchemard", 10, "#017a.jpg","rouge")
	maCarte7 = carte("cauchemard", 10, "#017a.jpg","rouge")
	allcarte =[maCarte0,maCarte1,maCarte2,maCarte3]
	return allcarte

def insert(insert):
#		purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),('2006-04-06', 'SELL', 'IBM', 500, 53.00),]
#c.executemany('INSERT INTO' table 'VALUES (?,?,?,?,?)', purchases)
	fichierDonnees ="./magic_projet.sql"
	conn =sqlite3.connect('magic_carte.sql') 
	cur =conn.cursor()
	cur.execute(insert)
	conn.commit()
	cur.close() 
	conn.close() 
	
#print(select_all_carte())
def selectUser():
	perso=[]
	fichierDonnees ="./magic_projet.sql"
	conn =sqlite3.connect('magic_carte.sql') 
	cur =conn.cursor()
	row=cur.execute('SELECT ID_PERSO, PSEUDO, XP FROM PERSO')
	
	for ligne in row:
		perso.append(ligne)
		#perso.append('Perso:'+ligne[1]+'\nXP:'+str(ligne[2]))	# a ameliorer car prend tt les persos dans la BDD
	
	
	conn.commit()
	cur.close() 
	conn.close() 
	return(perso)

def saveUser(joueur):
	fichierDonnees ="./magic_projet.sql"
	conn =sqlite3.connect('magic_carte.sql') 
	cur =conn.cursor()
	row=cur.execute('SELECT ID_PERSO FROM PERSO WHERE PSEUDO='(joueur.nom))
	if row[0] == []:
		row=cur.execute('SELECT max(ID_PERSO) FROM PERSO ')
		ids = row[0] +1
	else:
		ids = row[0]
	cur.executemany('INSERT INTO PERSO VALUES '(ids,joueur.nom,joueur.xp))
	conn.commit()
	cur.close() 
	conn.close() 

#insert("INSERT INTO PERSO (ID_PERSO,PSEUDO,XP ) VALUES (3,'floto',1000)")
#print(selectUser())
#print(selectUser()[0])

#create_table('./SQL/magic_carte1.sql')
#insertinbdd()
#print select_all_carte()
