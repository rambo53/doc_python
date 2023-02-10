import socket

'''
Pour communiquer entre 2 machines on établit une communication réseau qu'on appel 'socket' qui transfert des 
informations en binaire avec le protocole TCP (garantit la fiabilité des données) via des requêtes HTTP ou HTTPS.
Pour fonctionner il faut l'ip et le port de communication (ex : 8080)
'''

s = socket.socket()

# le premier param est l'ip ici je laisse vide pour dire que j'accepte tous types d'ip en entrée
# mais je peux aussi préciser "127.0.0.1" pour mon localhost
s.bind(("", 32000))
s.listen()

print("Connection en cours...")
connection_socket, client_address = s.accept()
print(f"Connection ok sur {client_address}.")

exit = False
# envoie au serveur client un message en binaire
while exit != True:
    message_serveur = input("serveur : ")

    if "exit" in message_serveur:
        exit = True
    else:
        connection_socket.sendall(message_serveur.encode())

    reponse_client = connection_socket.recv(1024)
    print("client : "+reponse_client.decode())

connection_socket.close()
s.close()