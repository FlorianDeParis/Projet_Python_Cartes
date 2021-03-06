


CREATE TABLE `APPARTIEN` (
  `ID_PERSO` smallint(2) NOT NULL,
  `ID_DECK` smallint(2) NOT NULL,
  PRIMARY KEY (`ID_PERSO`,`ID_DECK`),
  KEY `I_FK_APPARTIEN_PERSO` (`ID_PERSO`),
  KEY `I_FK_APPARTIEN_DECK` (`ID_DECK`),
  CONSTRAINT `appartien_ibfk_2` FOREIGN KEY (`ID_DECK`) REFERENCES `DECK` (`ID_DECK`),
  CONSTRAINT `appartien_ibfk_1` FOREIGN KEY (`ID_PERSO`) REFERENCES `PERSO` (`ID_PERSO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




CREATE TABLE `APPORT_MANA` (
  `ID_MANA` smallint(2) NOT NULL AUTO_INCREMENT,
  `ID_CARTE` smallint(2) NOT NULL,
  `APPORT_ROUGE` smallint(1) DEFAULT NULL,
  `APPORT_BLANC` smallint(1) DEFAULT NULL,
  `APPORT_NOIR` smallint(1) DEFAULT NULL,
  `APPORT_BLEU` smallint(1) DEFAULT NULL,
  `APPORT_VERT` smallint(1) DEFAULT NULL,
  PRIMARY KEY (`ID_MANA`),
  KEY `I_FK_APPORT_MANA_CARTE` (`ID_CARTE`),
  CONSTRAINT `apport_mana_ibfk_1` FOREIGN KEY (`ID_CARTE`) REFERENCES `CARTE` (`ID_CARTE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `APPORT_MANA` WRITE;


INSERT INTO `APPORT_MANA` (`ID_MANA`, `ID_CARTE`, `APPORT_ROUGE`, `APPORT_BLANC`, `APPORT_NOIR`, `APPORT_BLEU`, `APPORT_VERT`)
VALUES
	(1,11,1,1,1,1,1),
	(2,13,NULL,1,NULL,NULL,NULL);


UNLOCK TABLES;






CREATE TABLE `CARTE` (
  `ID_CARTE` smallint(2) NOT NULL AUTO_INCREMENT,
  `NOM_CARTE` char(32) DEFAULT NULL,
  `TYPE_CARTE` smallint(1) DEFAULT NULL COMMENT '1:terrain,2:creature,3:enchantement,4:rituel,5:ephemere',
  `URL_IMAGE` varchar(128) DEFAULT NULL,
  `COULEUR_CARTE` varchar(128) DEFAULT NULL,
  `ATTACK` smallint(2) DEFAULT NULL,
  `DEFENSE` smallint(2) DEFAULT NULL,
  `FONCTION_LIEE` char(32) DEFAULT NULL,
  PRIMARY KEY (`ID_CARTE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



INSERT INTO `CARTE` (`ID_CARTE`, `NOM_CARTE`, `TYPE_CARTE`, `URL_IMAGE`, `COULEUR_CARTE`, `ATTACK`, `DEFENSE`, `FONCTION_LIEE`)
VALUES
	(1,'Garde moustique',2,'#002.jpg','blanc',1,1,'initiative'),
	(2,'Pecheuse celeste kor',2,'#003.jpg','blanc',2,3,'vol'),
	(3,'Chasseciel leonin',2,'#004.jpg','blanc',2,2,'vol'),
	(4,'Voyage vers le neant',3,'#005.jpg','blanc',NULL,NULL,NULL),
	(5,'Filins prismatiques',5,'#006.jpg','blanc',NULL,NULL,NULL),
	(6,'Legionnaire de porcelaine',2,'#007.jpg','blanc',3,1,'lien de vie'),
	(7,'Sonner alarme',5,'#008.jpg','blanc',NULL,NULL,NULL),
	(8,'Faucon escadron',2,'#009.jpg','blanc',1,1,'vol'),
	(9,'Missionnaire solitaire',2,'#010.jpg','blanc',2,1,'pietinement'),
	(10,'Lynx des steppes',2,'#011.jpg','blanc',0,1,NULL),
	(11,'Immensite terramorphe',1,'#012.jpg','blanc',NULL,NULL,NULL),
	(12,'Golem de rasoirs',2,'#013.jpg','incolor',3,4,NULL),
	(13,'Plaine',1,'#014.jpg','blanc',NULL,NULL,NULL),
	(14,'Javelimier Icatian',2,'#015.jpg','blanc',1,1,NULL),
	(15,'Preceptrice eclairee',5,'#016.jpg','blanc',NULL,NULL,NULL),
	(16,'Mystique forgepierre',2,'#017.jpg','blanc',1,2,'imblocable'),
	(17,'Maitre de etherium',2,'#018.jpg','bleu',6,6,NULL),
	(18,'Scrige du caveau',2,'#019.jpg','noir',1,1,'vol'),
	(19,'Tezzeret agent de bolas',3,'#020.jpg','noir',NULL,NULL,NULL),
	(20,'Devastateur entravarc',2,'#021.jpg','incolor',1,1,'indestructible'),
	(21,'blindage cranien',3,'#022.jpg','incolor',NULL,NULL,NULL),
	(22,'Nexus des encrimites',1,'#023.jpg','incolor',NULL,NULL,NULL),
	(23,'Champion grave',2,'#024.jpg','bleu',2,2,'distortion'),
	(24,'Citadelle de sombracier',1,'#025.jpg','incolor',NULL,NULL,NULL),
	(25,'Memnite',2,'#026.jpg','bleu',1,1,NULL),
	(26,'Mox opale',1,'#027.jpg','incolor',NULL,NULL,NULL),
	(27,'Tambour de sautefeuille',3,'#028.jpg','incolor',NULL,NULL,NULL),
	(28,'Ancienne taniere',1,'#029.jpg','blanc',NULL,NULL,NULL),
	(29,'Ornithoptere',2,'#030.jpg','incolor',NULL,2,'vol'),
	(30,'Siege du synode',1,'#031.jpg','bleu',NULL,NULL,NULL),
	(31,'Adjuration des pensees',4,'#032.jpg','bleu',NULL,NULL,NULL),
	(32,'Caveau des chuchotements',1,'#033.jpg','noir',NULL,NULL,NULL);


UNLOCK TABLES;




CREATE TABLE `COUT_INVOQUE` (
  `ID_COUT` smallint(2) NOT NULL AUTO_INCREMENT,
  `ID_CARTE` smallint(2) NOT NULL,
  `COUT_ROUGE` smallint(1) DEFAULT NULL,
  `COUT_BLANC` smallint(1) DEFAULT NULL,
  `COUT_NOIR` smallint(1) DEFAULT NULL,
  `COUT_BLEU` smallint(1) DEFAULT NULL,
  `COUT_VERT` smallint(1) DEFAULT NULL,
  `COUT_MULTI` smallint(1) DEFAULT NULL,
  PRIMARY KEY (`ID_COUT`),
  KEY `I_FK_COUT_INVOQUE_CARTE` (`ID_CARTE`),
  CONSTRAINT `cout_invoque_ibfk_1` FOREIGN KEY (`ID_CARTE`) REFERENCES `CARTE` (`ID_CARTE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `COUT_INVOQUE` WRITE;


INSERT INTO `COUT_INVOQUE` (`ID_COUT`, `ID_CARTE`, `COUT_ROUGE`, `COUT_BLANC`, `COUT_NOIR`, `COUT_BLEU`, `COUT_VERT`, `COUT_MULTI`)
VALUES
	(2,1,NULL,1,NULL,NULL,NULL,NULL),
	(3,2,NULL,1,NULL,NULL,NULL,1),
	(4,3,NULL,2,NULL,NULL,NULL,NULL),
	(5,4,NULL,1,NULL,NULL,NULL,1),
	(6,5,NULL,1,NULL,NULL,NULL,2),
	(7,6,NULL,NULL,NULL,NULL,1,2),
	(8,7,NULL,1,NULL,NULL,NULL,1),
	(9,8,NULL,1,NULL,NULL,NULL,1),
	(10,9,NULL,1,NULL,NULL,NULL,1),
	(11,10,NULL,1,NULL,NULL,NULL,NULL),
	(12,12,NULL,NULL,NULL,NULL,NULL,6),
	(13,14,NULL,1,NULL,NULL,NULL,NULL),
	(14,15,NULL,1,NULL,NULL,NULL,NULL),
	(15,16,NULL,1,NULL,NULL,NULL,1),
	(16,17,NULL,NULL,NULL,1,NULL,2),
	(17,18,NULL,NULL,1,NULL,NULL,1),
	(18,19,NULL,NULL,1,1,NULL,2),
	(19,20,NULL,NULL,NULL,NULL,NULL,2),
	(20,21,NULL,NULL,NULL,NULL,NULL,2),
	(21,23,NULL,NULL,NULL,NULL,NULL,3),
	(22,25,NULL,NULL,NULL,NULL,NULL,NULL),
	(23,27,NULL,NULL,NULL,NULL,NULL,1),
	(24,29,NULL,NULL,NULL,NULL,NULL,NULL),
	(25,31,NULL,NULL,NULL,1,NULL,4);


UNLOCK TABLES;





CREATE TABLE `DECK` (
  `ID_DECK` smallint(2) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`ID_DECK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `DECK` WRITE;


INSERT INTO `DECK` (`ID_DECK`, `NAME`)
VALUES
	(1,'Pauper Weenie_white'),
	(2,'Affinite_robot blanc_noir_bleu');


UNLOCK TABLES;






CREATE TABLE `LIE` (
  `ID_DECK` smallint(2) NOT NULL,
  `ID_CARTE` smallint(2) NOT NULL,
  `QUANTITE_CARTE` smallint(2) DEFAULT NULL,
  PRIMARY KEY (`ID_DECK`,`ID_CARTE`),
  KEY `I_FK_LIE_DECK` (`ID_DECK`),
  KEY `I_FK_LIE_CARTE` (`ID_CARTE`),
  CONSTRAINT `lie_ibfk_2` FOREIGN KEY (`ID_CARTE`) REFERENCES `CARTE` (`ID_CARTE`),
  CONSTRAINT `lie_ibfk_1` FOREIGN KEY (`ID_DECK`) REFERENCES `DECK` (`ID_DECK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `LIE` WRITE;


INSERT INTO `LIE` (`ID_DECK`, `ID_CARTE`, `QUANTITE_CARTE`)
VALUES
	(1,1,3),
	(1,2,4),
	(1,3,3),
	(1,4,4),
	(1,5,2),
	(1,6,3),
	(1,7,4),
	(1,8,4),
	(1,9,3),
	(1,10,4),
	(1,11,4),
	(1,12,2),
	(1,13,16),
	(1,14,4),
	(2,15,1),
	(2,16,1),
	(2,17,4),
	(2,18,4),
	(2,19,3),
	(2,20,2),
	(2,21,4),
	(2,22,1),
	(2,23,4),
	(2,24,4),
	(2,25,4),
	(2,26,4),
	(2,27,4),
	(2,28,4),
	(2,29,4),
	(2,30,4),
	(2,31,4),
	(2,32,4);


UNLOCK TABLES;




CREATE TABLE `PERSO` (
  `ID_PERSO` smallint(2) NOT NULL AUTO_INCREMENT,
  `PSEUDO` varchar(128) DEFAULT NULL,
  `XP` bigint(4) DEFAULT NULL,
  PRIMARY KEY (`ID_PERSO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;





