
# Definition d un client reseau rudimentaire
# Ce client dialogue avec un serveur ad hoc

import socket, sys, pickle

HOST = '192.168.0.14'
PORT = 48000


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
    try:
        newObj = pickle.loads(msgServeur)
        print "A>", newObj.pointMana
    except:       
        print "S>", msgServeur

    msgClient = raw_input("C> ")
    mySocket.send(msgClient)
    msgServeur = mySocket.recv(1024)
    newObj = pickle.loads(msgServeur)
    print "Z>", newObj.pointMana
    
# 4) Fermeture de la connexion :
print "Connexion interrompue."
mySocket.close()
