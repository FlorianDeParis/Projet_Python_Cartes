
# Definition d'un client reseau gerant en parallele l emission
# et la reception des messages (utilisation de 2 THREADS).

host = '192.168.0.235'
port = 40000

import socket, sys, threading

class ThreadReception(threading.Thread):
    """objet thread gerant la reception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # ref. du socket de connexion
        
    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print "*" + message_recu + "*"
            if message_recu =='' or message_recu.upper() == "FIN":
                break
        # Le thread <reception> se termine ici.
        # On force la fermeture du thread <emission> :
        th_E._Thread__stop()
        print "Client arrete. Connexion interrompue."
        self.connexion.close()
    
class ThreadEmission(threading.Thread):
    """objet thread gerant l'emission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # ref. du socket de connexion
        
    def run(self):
        while 1:
            message_emis = raw_input()
            self.connexion.send(message_emis)

# Programme principal - Etablissement de la connexion :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print "La connexion a echoue."
    sys.exit()    
print "Connexion etablie avec le serveur."
            
# Dialogue avec le serveur : on lance deux threads pour gerer
# independamment l emission et la reception des messages :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()        
