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

    resultat = {
        'pseudo' : request.form['pseudo'],
        'nom': request.form['nom'].upper(),
        'prenom': request.form['prenom'].upper()
        }


# Connection et création de la base de données:
    exo_db = mariadb.connect(host='localhost', user='root', password='root')
    cursor = exo_db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS data_user")
    cursor.execute("USE data_user")
# Création de la table USER :
    cursor.execute("CREATE TABLE IF NOT EXISTS user (pseudo VARCHAR(255), nom VARCHAR(255), prenom VARCHAR(255))")

# # Vérif des doublons :
    cursor.execute("SELECT pseudo from user WHERE pseudo = '{}'".format(resultat['pseudo']))
    test_pseudo = cursor.fetchone() # fetchone récupère les pseudos s'ils existent, sinon renvoie NONE
    if test_pseudo is not None: # Vérifie que test_pseudo est à None ou pas. Si None c'est qu'il existe pas / donc n'éxécute pas l'erreur
        return render_template("erreur.html")

# Insertion des données :
    post = "INSERT INTO user (pseudo, nom, prenom) VALUES (%s, %s, %s)"
    values = (resultat['pseudo'], resultat['nom'], resultat['prenom'])
    cursor.execute(post, values)
# Validation :
    exo_db.commit()
    cursor.close()
    exo_db.close()


    return render_template("confirmation.html", **resultat) # le **permet de prendre en compte plusieurs variables

if __name__ == '__main__':
    app.run()