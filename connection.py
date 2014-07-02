import sqlite3
from carte import*
from creature import*
from terrain import*
from sort import*

def create_table():
	#fichierDonnees ="./magic_projet.sql"
	#conn =sqlite3.connect('magic_projet1.sql') 
	#cur =conn.cursor()
	#~ cur.execute(''' CREATE TABLE COUT_INVOQUE
	   #~ (
	   #~ ID_CARTE SMALLINT NOT NULL ,
	   #~ COUT_ROUGE SMALLINT  ,
	   #~ COUT_BLANC SMALLINT  ,
	   #~ COUT_NOIR SMALLINT  ,
	   #~ COUT_BLEU SMALLINT  ,
	   #~ COUT_VERT SMALLINT  ,
	   #~ COUT_MULTI SMALLINT  ,
	   #~ ID_COUT SMALLINT NOT NULL 
	#~ ,
	     #~ PRIMARY KEY (ID_COUT) CONSTRAINT PK_COUT_INVOQUE)
	   #~ ''')
	#~ cur.execute(''' CREATE TABLE APPORT_MANA
	   #~ (
	   #~ ID_CARTE SMALLINT NOT NULL ,
	   #~ APPORT_ROUGE SMALLINT  ,
	   #~ APPORT_BLANC SMALLINT  ,
	   #~ APPORT_NOIR SMALLINT  ,
	   #~ APPORT_BLEU SMALLINT  ,
	   #~ APPORT_VERT SMALLINT  ,
	   #~ ID_MANA SMALLINT NOT NULL 
	   #~ ,
	     #~ PRIMARY KEY (ID_MANA) CONSTRAINT PK_APPORT_MANA
	   #~ ) ''')
	#~ cur.execute('''CREATE TABLE PERSO
	   #~ (
	   #~ ID_PERSO SMALLINT NOT NULL ,
	   #~ PSEUDO VARCHAR(128)  ,
	   #~ XP INTEGER  
	   #~ ,
	     #~ PRIMARY KEY (ID_PERSO) CONSTRAINT PK_PERSO
	   #~ )   ''')
	#~ cur.execute('''  CREATE TABLE DECK
	   #~ (
	   #~ ID_DECK SMALLINT NOT NULL ,
	   #~ NAME VARCHAR(128)  
	   #~ ,
	     #~ PRIMARY KEY (ID_DECK) CONSTRAINT PK_DECK
	   #~ ) ''')
	#~ cur.execute('''CREATE TABLE carte
	   #~ (ID_CARTE SMALLINT NOT NULL ,
	   #~ NOM_CARTE CHAR(32)  ,
	   #~ TYPE SMALLINT  ,
	   #~ URL_IMAGE VARCHAR(128)  ,
	   #~ COULEUR_CARTE VARCHAR(128)  ,
	   #~ ATTACK SMALLINT  ,
	   #~ DEFENSE SMALLINT  ,
	   #~ FONCTION_LIEE CHAR(32)  
	#~ ,
	     #~ PRIMARY KEY (ID_CARTE) CONSTRAINT PK_CARTE)''')
	     
	 #cur.execute('''CREATE TABLE LIER(  ID_DECK SMALLINT NOT NULL ,ID_CARTE SMALLINT NOT NULL ,PRIMARY KEY (ID_DECK, ID_CARTE) CONSTRAINT PK_LIER)''')
	#cur.execute(''' CREATE TABLE APPARTIEN(ID_PERSO SMALLINT NOT NULL ,ID_DECK SMALLINT NOT NULL, PRIMARY KEY (ID_PERSO, ID_DECK) CONSTRAINT PK_APPARTIEN
	#   )''')    
	#cur.execute(''' CREATE  INDEX I_FK_LIER_DECK      ON LIER (ID_DECK ASC)''')

	#cur.execute('''CREATE  INDEX I_FK_LIER_CARTE      ON LIER (ID_CARTE ASC)''')    
	#cur.execute('''CREATE  INDEX I_FK_APPARTIEN_PERSO      ON APPARTIEN (ID_PERSO ASC) ''')
	#cur.execute('''CREATE  INDEX I_FK_APPARTIEN_DECK    ON APPARTIEN (ID_DECK ASC) ''')
	#conn.commit()
	#cur.close() 
	conn.close() 
def select_all_carte():
	allcarte = []
	fichierDonnees ="./magic_projet.sql"
	conn =sqlite3.connect('magic_projet1.sql') 
	cur =conn.cursor()
	i=0
	#def __init__(self, nomCarte, idCarte, url_img, couleurCarte)
	#  ID_CARTE SMALLINT NOT NULL ,    NOM_CARTE CHAR(32)  ,TYPE SMALLINT  ,   URL_IMAGE VARCHAR(128)  ,  
#	COULEUR_CARTE VARCHAR(128)  ,    ATTACK SMALLINT  ,    DEFENSE SMALLINT  ,    FONCTION_LIEE CHAR(32)  
	for row in cur.execute('SELECT NOM_CARTE,ID_CARTE, URL_IMAGE,COULEUR_CARTE,TYPE,ATTACK,DEFENSE,FONCTION_LIEE FROM carte '):
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

def insert(insert):
#		purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),('2006-04-06', 'SELL', 'IBM', 500, 53.00),]
#c.executemany('INSERT INTO' table 'VALUES (?,?,?,?,?)', purchases)
	fichierDonnees ="./magic_projet.sql"
	conn =sqlite3.connect('magic_projet1.sql') 
	cur =conn.cursor()
	cur.executemany(insert)
	conn.commit()
	cur.close() 
	conn.close() 
	
print(select_all_carte())
