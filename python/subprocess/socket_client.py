import socket
import time

s = socket.socket()

print("Connection au serveur...")

# ici je dois préciser que je tourne sur mon serveur localhost pour se connecter à mon serveur
# si je ne précise pas d'adresse serveur alors cela ne fonctionne pas

def connectionServer():
    try:
        s.connect(("127.0.0.1", 32000))
        print("Connecté au serveur.")
        return True
    except ConnectionRefusedError as e:
        print(str(e))
        time.sleep(5)
        return False

########################## MAIN ########################## 

connectionOk = False

while connectionOk == False:
    connectionOk = connectionServer()

exit = False
while exit != True:
    # reçoit le binaire d'une longuer max de 1ko
    reponse_serveur = s.recv(1024)
    # affiche le message reçu au format str
    if reponse_serveur:
        print("serveur : "+reponse_serveur.decode())

    message_client = input("client : ")
    if "exit" in message_client:
        exit = True
    else:
        s.sendall(message_client.encode())


s.close()