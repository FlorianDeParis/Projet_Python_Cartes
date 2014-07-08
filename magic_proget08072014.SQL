DROP DATABASE IF EXISTS magic_carte;

CREATE DATABASE IF NOT EXISTS magic_carte;
USE magic_carte;
# -----------------------------------------------------------------------------
#       TABLE : COUT_INVOQUE
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS COUT_INVOQUE
 (
   ID_COUT SMALLINT(2) NOT NULL  ,
   ID_CARTE SMALLINT(2) NOT NULL  ,
   COUT_ROUGE SMALLINT(1) NULL  ,
   COUT_BLANC SMALLINT(1) NULL  ,
   COUT_NOIR SMALLINT(1) NULL  ,
   COUT_BLEU SMALLINT(1) NULL  ,
   COUT_VERT SMALLINT(1) NULL  ,
   COUT_MULTI SMALLINT(1) NULL  
   , PRIMARY KEY (ID_COUT) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       INDEX DE LA TABLE COUT_INVOQUE
# -----------------------------------------------------------------------------


CREATE  INDEX I_FK_COUT_INVOQUE_CARTE
     ON COUT_INVOQUE (ID_CARTE ASC);

# -----------------------------------------------------------------------------
#       TABLE : CARTE
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS CARTE
 (
   ID_CARTE SMALLINT(2) NOT NULL  ,
   NOM_CARTE CHAR(32) NULL  ,
   TYPE_CARTE SMALLINT(1) NULL  ,
   URL_IMAGE VARCHAR(128) NULL  ,
   COULEUR_CARTE VARCHAR(128) NULL  ,
   ATTACK SMALLINT(2) NULL  ,
   DEFENSE SMALLINT(2) NULL  ,
   FONCTION_LIEE CHAR(32) NULL  
   , PRIMARY KEY (ID_CARTE) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       TABLE : APPORT_MANA
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS APPORT_MANA
 (
   ID_MANA SMALLINT(2) NOT NULL  ,
   ID_CARTE SMALLINT(2) NOT NULL  ,
   APPORT_ROUGE SMALLINT(1) NULL  ,
   APPORT_BLANC SMALLINT(1) NULL  ,
   APPORT_NOIR SMALLINT(1) NULL  ,
   APPORT_BLEU SMALLINT(1) NULL  ,
   APPORT_VERT SMALLINT(1) NULL  
   , PRIMARY KEY (ID_MANA) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       INDEX DE LA TABLE APPORT_MANA
# -----------------------------------------------------------------------------


CREATE  INDEX I_FK_APPORT_MANA_CARTE
     ON APPORT_MANA (ID_CARTE ASC);

# -----------------------------------------------------------------------------
#       TABLE : PERSO
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS PERSO
 (
   ID_PERSO SMALLINT(2) NOT NULL  ,
   PSEUDO VARCHAR(128) NULL  ,
   XP BIGINT(4) NULL  
   , PRIMARY KEY (ID_PERSO) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       TABLE : DECK
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS DECK
 (
   ID_DECK SMALLINT(2) NOT NULL  ,
   NAME VARCHAR(128) NULL  
   , PRIMARY KEY (ID_DECK) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       TABLE : LIÉ
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS LIÉ
 (
   ID_DECK SMALLINT(2) NOT NULL  ,
   ID_CARTE SMALLINT(2) NOT NULL  ,
   QUANTITE_CARTE SMALLINT(2) NULL  
   , PRIMARY KEY (ID_DECK,ID_CARTE) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       INDEX DE LA TABLE LIÉ
# -----------------------------------------------------------------------------


CREATE  INDEX I_FK_LIÉ_DECK
     ON LIÉ (ID_DECK ASC);

CREATE  INDEX I_FK_LIÉ_CARTE
     ON LIÉ (ID_CARTE ASC);

# -----------------------------------------------------------------------------
#       TABLE : APPARTIEN
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS APPARTIEN
 (
   ID_PERSO SMALLINT(2) NOT NULL  ,
   ID_DECK SMALLINT(2) NOT NULL  
   , PRIMARY KEY (ID_PERSO,ID_DECK) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       INDEX DE LA TABLE APPARTIEN
# -----------------------------------------------------------------------------


CREATE  INDEX I_FK_APPARTIEN_PERSO
     ON APPARTIEN (ID_PERSO ASC);

CREATE  INDEX I_FK_APPARTIEN_DECK
     ON APPARTIEN (ID_DECK ASC);


# -----------------------------------------------------------------------------
#       CREATION DES REFERENCES DE TABLE
# -----------------------------------------------------------------------------


ALTER TABLE COUT_INVOQUE 
  ADD FOREIGN KEY FK_COUT_INVOQUE_CARTE (ID_CARTE)
      REFERENCES CARTE (ID_CARTE) ;


ALTER TABLE APPORT_MANA 
  ADD FOREIGN KEY FK_APPORT_MANA_CARTE (ID_CARTE)
      REFERENCES CARTE (ID_CARTE) ;


ALTER TABLE LIÉ 
  ADD FOREIGN KEY FK_LIÉ_DECK (ID_DECK)
      REFERENCES DECK (ID_DECK) ;


ALTER TABLE LIÉ 
  ADD FOREIGN KEY FK_LIÉ_CARTE (ID_CARTE)
      REFERENCES CARTE (ID_CARTE) ;


ALTER TABLE APPARTIEN 
  ADD FOREIGN KEY FK_APPARTIEN_PERSO (ID_PERSO)
      REFERENCES PERSO (ID_PERSO) ;


ALTER TABLE APPARTIEN 
  ADD FOREIGN KEY FK_APPARTIEN_DECK (ID_DECK)
      REFERENCES DECK (ID_DECK) ;

