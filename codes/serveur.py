import mysql.connector
from mysql.connector import errorcode

def Authentification(data : dict):
    # Connection à la base de données
    config = {
        'user': 'root',
        'password': 'pass',
        'host': '127.0.0.1',
        'database': 'roman',
        'raise_on_warnings': True
    }

    try:
        cnx = mysql.connector.connect(**config)
        cursorSel = cnx.cursor()
        selectAction = ("select * from user where mail = '"+data.get("mail")+"' and mdp = '"+data.get("mot_de_passe")+"'")
        cursorSel.execute(selectAction)
        resultSelect = cursorSel.fetchall()
        cursorSel.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("L'utilisateur ou le mot de passe n'est pas correct")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de données n'existe pas!")
        else:
            print(err)

    exit()

def Authentification(data : dict):
    # Connection à la base de données
    config = {
        'user': 'root',
        'password': 'pass',
        'host': '127.0.0.1',
        'database': 'roman',
        'raise_on_warnings': True
    }

    try:
        cnx = mysql.connector.connect(**config)
        cursorSel = cnx.cursor()
        requet="insert into user(nom,mail,mdp) values('"+liste[0]+"','"+liste[1]+"','"+liste[3]+"')"
        selectAction = ("select * from user where mail = '"+data.get("mail")+"' and mdp = '"+data.get("mot_de_passe")+"'")
        cursorSel.execute(selectAction)
        resultSelect = cursorSel.fetchall()
        cursorSel.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("L'utilisateur ou le mot de passe n'est pas correct")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de données n'existe pas!")
        else:
            print(err)

    exit()

    