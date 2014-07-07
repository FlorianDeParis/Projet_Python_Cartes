
# Definition d un client reseau rudimentaire
# Ce client dialogue avec un serveur ad hoc

import socket, sys

HOST = '10.66.126.86'
PORT = 50000

# 1) creation du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) envoi d'une requete de connexion au serveur :
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print "La connexion a echoue."
    sys.exit()    
print "Connexion etablie avec le serveur."    

# 3) Dialogue avec le serveur :
msgServeur = mySocket.recv(1024)

while 1:
    if msgServeur.upper() == "FIN" or msgServeur =="":
        break
    print "S>", msgServeur
    msgClient = raw_input("C> ")
    mySocket.send(msgClient)
    msgServeur = mySocket.recv(1024)

# 4) Fermeture de la connexion :
print "Connexion interrompue."
mySocket.close()
