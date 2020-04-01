# les IMPORTS 
from pymongo import MongoClient
from pprint import pprint

# connection à MongoDB
client = MongoClient('127.0.0.1',27017)
db = client['ma_base']
# db = client['admin']

#Etat du server
# serverStatusResult = db.command("serverStatus")
# pprint(serverStatusResult)

# Se placer dans test dans admin de la base:
db = client['ma_base']
#Création de la collection:
collec = db.create_collection("data_client")

#descritif de la collection :
#data_user = {'_id': nick_name, 'prenom': prenom, 'nom': nom, 'sexe': sexe}

# morad a posté :
nick_name = 'phoenix'
prenom = 'morad'
nom = 'ziad'
sexe = 'masculin'

data = {'_id':nick_name, 'prenom':prenom, 'nom':nom, 'sexe':sexe}

#poster :
client_1 = db.insert_many([data])




