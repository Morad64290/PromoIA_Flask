# Test serveur SQL

import mysql.connector as mariadb


## d'abord on se connecte à la DB. On stock dans une variable ici test_db
## Le .connect nécessite 3 parametres : host user et password
test_db = mariadb.connect(host='localhost', user='root', password='root')
#print(test_db)
## On devrait à avoir une réponse type : <mariadb.connector.connection_cext.CMySQLConnection object at 0x0000020C26A84C50>

## Création  d'une instance de la classe "cursor" qui est utilisée pour exécuter les instructions "SQL" dans Python.
cursor = test_db.cursor()


                    # ''' Création de la base de données appelée "data_user" '''
                    
## La méthode "execute()" est utilisée pour compiler une instruction "SQL".
## Si la base existe déjà on aura un message d'erreur / IF NOT EXISTS permet de créer la DB si elle n'existe pas
cursor.execute("CREATE DATABASE IF NOT EXISTS data_user")

##  On peut voir l'état de TOUTES les bases 
cursor.execute("SHOW DATABASES")
bases_G = cursor.fetchall()
print(bases_G)

##  On utilise la base en cours 
cursor.execute("USE data_user")
## On peut également pour etre sur se reconnecter à la base

# test_db = mariadb.connect(host='localhost', user='root', password='root', database = 'data_user')
# print(test_db)

## Création de tables
# Ici on va créer une table USER et colonnes nom/prénom
# On doit également définir les types pour les colonnes VARCHAR(255), INT, FLOAT ....

cursor.execute("CREATE TABLE IF NOT EXISTS user (pseudo VARCHAR(255), nom VARCHAR(255), prenom VARCHAR(255), PRIMARY KEY (pseudo))")
##  On peut voir l'état des tables de la base DATA_USER
cursor.execute("SHOW TABLES")
tables_G = cursor.fetchall()
print("la table crée est:", tables_G) # Doit afficher USER

# Pour afficher les tables une par une :
for table in tables_G:
    print(table) # Doit afficher USER

# Pour afficher ce qu'il y'a dans la table USER:
# cursor.execute("DESC user")
# print(cursor.fetchall() ) va renvoyer un tuple avec les infos varchar, int, etc etc
# exemple [('nom', 'varchar(255)'), ('prenom', 'varchar(255))]

   
#### A NOTER QU'IL N'Y A PAS ENCORE DE CLE PRIMAIRE ####
# Clé primaire : C'est une valeur unique dans le tableau. Elle permet de trouver chaque ligne de manière unique dans le tableau.
# Pour créer une clé primaire, il faut l'instruction PRIMARY KEY lors de la création de la table.

### On va rajouter un clé primaire type : PSEUDO
# Méthode : ALTER TABLE table_name ADD COLUMN column_name PRIMARY KEY 
# cursor.execute("ALTER TABLE user ADD COLUMN pseudo PRIMARY KEY")

# On peut vérifier :

# verif = cursor.execute("DESC user")
# print(verif)

# ou print(cursor.fetchall() ) --> On devrait avoir 3 colonnes

#### ON VA INSERER UN USER (nom prenom pseudo)
# Insertion de données dans un tableau pour les stocker. 
# Méthode : INSERT INTO table_name (noms_colonnes) VALUES (données soit %s, %s, %s, soit '{nom}','{prenom}','{pseudo}' ) pour l'insérer dans la table

# Définition de l'insertion:
post = "INSERT INTO user (pseudo, nom, prenom) VALUES (%s, %s, %s)"

# Définition des valeurs
values = ("phx1", "ziad", "morad")

# Exécution de l'insertion :
print(post, values)
cursor.execute(post, values)

# Résultat final, nous devons exécuter la méthode 'COMMIT()' de l'objet de la base de données
test_db.commit()
#Petite vérif du bon insert :
print(cursor.rowcount, 'insertion ok')

check = "SELECT pseudo from user GROUP BY pseudo HAVING COUNT (pseudo) >1"
if check > 0:
    return render_template("erreur.html")