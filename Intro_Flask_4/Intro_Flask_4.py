from flask import Flask, render_template, request, Markup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
# Définition de la fonction qui va afficher le résulat du formulaire
def text_box(): 
# On récupère les infos envoyées par l'utilisateur, on a l'objet REQUEST de la libraire flask + FORM requet.form['valeur']    
    # nom = request.form['nom'].upper()
    # prenom = request.form['prenom'].upper()
    # age = request.form['age'].upper()
    # adr = request.form['adresse'].upper()
    # CP = request.form['CP'].upper()

    # code_html =  f"""<div id="cr">
    #     <p id="identif">Votre nom et prénom sont: {nom} {prenom}</p>
    #     <p id="year_old">Vous avez {age} ans</p>
    #   </div>
    #   <br>
      
    #   <div id="lieu">
    #     <p id="adresse">Vous habitez à l'adresse suivante : <br>
    #     {adr} {CP}</p>
    #   </div>"""

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
            
    return render_template("bienvenue.html", **resultat) # le **permet de prendre en compte plusieurs variables

if __name__ == '__main__':
    app.run()