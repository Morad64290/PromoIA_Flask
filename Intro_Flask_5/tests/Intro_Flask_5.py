# les IMPORTS
from flask import Flask, render_template, request, Markup
import mysql.connector as mariadb


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
# Définition de la fonction qui va afficher le résulat du formulaire
def text_box(): 
# On récupère les infos envoyées par l'utilisateur, on a l'objet REQUEST de la libraire flask + FORM requet.form['valeur']    
# gestion du Monsieur / Madame
    genre = str()
    if request.form.get("civilite") == "M.":
        genre += "Mr"

    if request.form.get("civilite") == "MMe.":
        genre += "Mme"

    if request.form.get("civilite") == "Mlle.":
        genre += "Mme"

    resultat = {
        'nom': request.form['nom'].upper(),
        'prenom': request.form['prenom'].upper(),
        'age': request.form['age'].upper(),
        'adr' : request.form['adresse'].upper(),
        'CP' : request.form['CP'].upper(),
        'civilite' : genre
        }


  
    # Création de la base de donnée
    db_connect = mariadb.connect(host="localhost",user="root",password="root", database="Exo_5")
    cursor = db_connect.cursor()
    #Création des tables
    cursor.execute("CREATE TABLE Identite (civilite, nom , prenom , age INT NOT NULL, adr, CP)CHARSET=utf8;")
    # db_connect.close()

    # Connection à la base de données
    db_connect = mariadb.connect(host="localhost", user="root", password="root", database="exo_5")
    cursor = db_connect.cursor()


    # Récupération des données et les mettre dans la table IDENTITE.
    # Ne pas oublier de dire d'où ca provient voir .format()
    baseDeDonnees = mysql.connector.connect(host="localhost",user="root",password="root", database="exo_5")
    curseur = db_connect.cursor()
    curseur.execute("INSERT INTO Identite (civilite, nom , prenom , age, adr, CP) VALUES ('{}', '{}', '{}', '{}')".format(resultat["civilite"], resultat["nom"], resultat["prenom"], resultat["adr"], resultat["CP"]))
    baseDeDonnees.commit()

    # On coupe
    cursor.close()
    db_connect.close()

# page de confirmation d'inscription
    return render_template("confirmation.html", **resultat) # le **permet de prendre en compte plusieurs variables


if __name__ == '__main__':
    app.run()