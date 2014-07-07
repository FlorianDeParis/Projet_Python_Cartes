import socket
import select

hote = '25.60.75.61'
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur ecoute a present sur le port {}".format(port))

serveur_lance = True
clients_connectes = []
while serveur_lance:
    # On va verifier que de nouveaux clients ne demandent pas e se connecter
    # Pour cela, on ecoute la connexion_principale en lecture
    # On attend maximum 50ms
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
        [], [], 0.05)
    
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # On ajoute le socket connecte à la liste des clients
        clients_connectes.append(connexion_avec_client)
    
    # Maintenant, on ecoute la liste des clients connectes
    # Les clients renvoyes par select sont ceux devant etre lus (recv)
    # On attend la encore 50ms maximum
    # On enferme l appel à select.select dans un bloc try
    # En effet, si la liste de clients connectes est vide, une exception
    # Peut etre levee
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients a lire
        for client in clients_a_lire:
            # Client est de type socket
            msg_recu = client.recv(1024)
            # Peut planter si le message contient des caracteres speciaux
            msg_recu = msg_recu.decode()
            print("Reçu {}".format(msg_recu))
            client.send(b"5 / 5")
            if msg_recu == "fin":
                serveur_lance = False

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()
