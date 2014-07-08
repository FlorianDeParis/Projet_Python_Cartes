# -*- coding: utf-8 -*-

# Definition d un serveur reseau gerant un systeme de CHAT simplifie.
# Utilise les threads pour gerer les connexions clientes en parallele.

HOST = '192.168.0.235'
PORT = 40000

import socket, sys, threading
 
class ThreadClient(threading.Thread):
    '''derivation d un objet thread pour gerer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        
    def run(self):
        # Dialogue avec le client :
        nom = self.getName()        # Chaque thread possede un nom
        while 1:
            msgClient = self.connexion.recv(1024)
            if msgClient.upper() == "FIN" or msgClient =="":
                break
            message = "%s> %s" % (nom, msgClient)
            print message
            # Faire suivre le message a tous les autres clients :
            for cle in conn_client:
                if cle != nom:      # ne pas le renvoyer a l emetteur
                    conn_client[cle].send(message)
                    
        # Fermeture de la connexion :
        self.connexion.close()      # couper la connexion cote serveur
        del conn_client[nom]        # supprimer son entree dans le dictionnaire
        print "Client %s deconnecte." % nom
        # Le thread se termine ici    

# Initialisation du serveur Mise en place du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print "La liaison du socket a l adresse choisie a echoue."
    sys.exit()
print "Serveur pret, en attente de requetes ..."
mySocket.listen(5)

# Attente et prise en charge des connexions demandees par les clients :
conn_client = {}                # dictionnaire des connexions clients
while 1:    
    connexion, adresse = mySocket.accept()
    # Creer un nouvel objet thread pour gerer la connexion :
    th = ThreadClient(connexion)
    th.start()
    # Memoriser la connexion dans le dictionnaire : 
    it = th.getName()        # identifiant du thread
    conn_client[it] = connexion
    print "Client %s connecte, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1])
    # Dialogue avec le client :
    connexion.send("Vous etes connecte. Envoyez vos messages.")
