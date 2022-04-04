import json
import socket
import webbrowser
import mysql.connector
from mysql.connector import errorcode

def Authentification(data : dict):
    # Connection à la base de données
    config = {
        'user': 'root',
        'password': 'essai',
        'host': '127.0.0.1',
        'database': 'user',
        'raise_on_warnings': True
    }

    try:
        cnx = mysql.connector.connect(**config)
        cursorSel = cnx.cursor()
        selectAction = ("select * from user where mail = '"+data.get("mail")+"' and mdp = '"+data.get("mot_de_passe")+"'")
        cursorSel.execute(selectAction)
        resultSelect = cursorSel.fetchall()
        return resultSelect
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("L'utilisateur ou le mot de passe n'est pas correct")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de données n'existe pas!")
        else:
            print(err)
    finally:
        cursorSel.close()

    exit()

def Enregistrement(data : dict):
    # Connection à la base de données
    config = {
        'user': 'root',
        'password': 'essai',
        'host': '127.0.0.1',
        'database': 'users',
        'raise_on_warnings': True
    }

    try:
        cnx = mysql.connector.connect(**config)
        cursorInsert = cnx.cursor()
        requet="insert into user(nom,mail,mdp) values('"+data.get("nom")+"','"+data.get("mail")+"','"+data.get("mot_de_passe")+"')"
        selectAction = (requet)
        cursorInsert.execute(selectAction)
        #resultSelect = cursorInsert.fetchall()
        print("Donnée Inserer")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("L'utilisateur ou le mot de passe n'est pas correct")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de données n'existe pas!")
        else:
            print(err)
    finally:
        cursorInsert.close()


    exit()

# Creation de socket 
host= ''
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             
# Demarrage du server
server.bind((host, port))
print("Serveur Demarré ..........")
while True:
    server.listen(5) 
    conn, addr = server.accept()
    message = conn.recv(1024)  
    message = message.decode("utf8")
    data = json.loads(message)
    if data.get("choix")== "LOGIN":
        resultat = Authentification(data)
        if resultat:
        #Envoi de message de connxion reussi
            messagesend = f"Connexion reussi"
            messagesend= messagesend.encode("utf8")
            conn.sendall(messagesend)
        #ouvrir le serveur mail
            webbrowser.open("http://192.168.10.1/SOGo/") 
        else:
            #Envoi de message de connxion echoue
            messagesend = "Identifiant Incorrect"
            messagesend = messagesend.encode("utf8")
            conn.sendall(messagesend)
            pass
    elif data.get("choix")== "CREER":
        Enregistrement(data)
       

conn.close()
server.close()