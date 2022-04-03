import socket
import json


adresseIP = "127.0.0.1"
port=50000
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((adresseIP , port))

def InfoEnregistrement():
    nom=input("entrer votre Nom: ")
    email=input("entrer votre mail: ")
    Mot_de_passe1=input("entrer votre mot de passe: ")
    Mot_de_passe2=input("confirmer votre mot de passe: ")
    while Mot_de_passe1 != Mot_de_passe2:
        
        print("mot de passe incorrecte")
        Mot_de_passe1=input("entrer votre mot de passe: ")
        Mot_de_passe2=input("confirmer votre mot de passe: ")
    
    data = { "Nom" : nom , "email" : email, "Mot_de_passe" : Mot_de_passe1 , "choix" : 'AJOUTER' }
    sendData = json.dumps(data)
    client.sendall(sendData.encode("utf-8"))

    response = client.recv(255)
    print("le resultat est :" , response.decode("utf-8"))
        
    exit(0)

def InfoLogin():
    email=input("entrer votre mail: ")
    Mot_de_passe1=input("entrer votre mot de passe: ") 
    data = { "email" : email, "Mot_de_passe" : Mot_de_passe1 , "choix" : 'LOGIN' }
    sendData = json.dumps(data)
    client.sendall(sendData.encode("utf-8"))
    response = client.recv(255)
    print("le resultat est :" , response.decode("utf-8"))
        
    exit(0)    

def menu():
    print("-----Bienvenue sur notre menu-----")
    print("Taper AJOUTER pour enregistrer un nouveau utilisateur")
    print("Taper LOGIN pour s'authentifier")
    print("Taper FIN pour Quitter")
    choix=""

    while choix != "FIN":
        try:
            choix = input("> ")
            if choix =="AJOUTER":
                InfoEnregistrement()
            elif choix =="LOGIN":
                InfoLogin()
            else:
                print("choix invalide")
                menu()
        except ValueError:
            print("choix invalide")
    print("Connexion fermé")
    client.close()




