import socket
import json

def Instance_client(data : dict):
    adresseIP = "127.0.0.1"
    port=9999
    client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    client.connect((adresseIP , port))
    sendData = json.dumps(data)
    client.sendall(sendData.encode("utf-8"))
    response = client.recv(255)
    print(response.decode("utf-8"))
    client.close()


def InfoEnregistrement()->dict:
    nom=input("entrer votre Nom: ")
    email=input("entrer votre mail: ")
    Mot_de_passe1=input("entrer votre mot de passe: ")
    Mot_de_passe2=input("confirmer votre mot de passe: ")
    while Mot_de_passe1 != Mot_de_passe2: 
        print("mot de passe incorrecte")
        Mot_de_passe1=input("entrer votre mot de passe: ")
        Mot_de_passe2=input("confirmer votre mot de passe: ")
    data = { "Nom" : nom , "email" : email, "Mot_de_passe" : Mot_de_passe1 , "choix" : 'CREER' }
    return data

def InfoLogin()->dict:
    email=input("entrer votre mail: ")
    Mot_de_passe1=input("entrer votre mot de passe: ") 
    data = { "email" : email, "Mot_de_passe" : Mot_de_passe1 , "choix" : 'LOGIN' }
    return(data)
        

def menu():
    print("-----Bienvenue sur notre menu-----")
    print("Taper CREER pour enregistrer un nouveau utilisateur")
    print("Taper LOGIN pour s'authentifier")
    print("Taper FIN pour Quitter")
    choix = input("> ")
    while choix.upper() !="FIN":
        if choix.upper() =="CREER":
            data=InfoEnregistrement()
        elif choix.upper() =="LOGIN":
            data=InfoLogin()  
        else:
            print("choix invalide")
            menu()
        Instance_client(data)
    print("Connexion fermé")
    exit(0)
    


if __name__=='__main__':
    menu()

