import socket
import os

# Création de socket pour permettre la communaication et l'écoute
ordinateur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ordinateur.bind(('Computer_ip_address', 1000))
ordinateur.listen()

while True:
    # Accepter la connexion du terminal mobile
    android, android_address = ordinateur.accept()
    print(f"Le terminal d'adresse {android_address} est connecté !")

    # Recevoir les données ou commandes du terminal mobile
    data = android.recv(1024)
    print(f"Commande reçue: {data.decode()}")

    # Exécuter la commande reçue
    commande = data.decode()
    if commande == "Eteindre":
        os.system("shutdown -s -t 1")  # L'ordinateur s'éteind aussitôt avec un delai de 0 seconde
    elif commande == "Musique":
        os.startfile("C:/Users/Username/Song/Directory/Path/title.mp3")  # La musique est jouée (Chemin d'acces de la chanson à jouer)
    android.close()
