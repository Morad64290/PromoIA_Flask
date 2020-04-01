## Les imports
from flask import Flask

## Définition de l'application
#app est le nom de l'application
app = Flask(__name__) 

# On définit l'adresse à laquelle on applique la def qui va suivre. Ici / signifie page d'accueil
@app.route("/") 

# Définition de la fonction que retournera la page d'accueil
def hello():
    return "Hello World !!\nC'est pas facile facile quand meme!"

# @app.route("/")
# def exo_1():
#     return "C'est pas facile facile quand meme!"

# Permet à l'application de se lancer qd on lance le script
if __name__ == "__main__":
    app.run()


