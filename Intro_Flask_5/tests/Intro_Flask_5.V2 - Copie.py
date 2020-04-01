from flask import Flask, render_template, request, Markup

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
    
    

    return render_template("confirmation.html", **resultat) # le **permet de prendre en compte plusieurs variables

if __name__ == '__main__':
    app.run()