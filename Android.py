import socket
import os

#Création du socket pour communiquer
android = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
android.connect(('Computer_ip_address', 1000))

#Phrases d'appel
print("Vous êtes connecté à l'ordinateur et pouvez exécuter quelques actions.")
print("________________________________")
print("Tapez: ")
print("Eteindre pour arrêter l'ordinateur.")
print("Musique pour jouer de la musique.")
print("________________________________")

#Commande
command = input("Que voulez-vous faire ?:  ")
android.send(command.encode())

android.close()
