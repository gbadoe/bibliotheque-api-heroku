## BIBLIOTHEQUE API
 DEBUT 
## Installation des dépendances
Python 3.10.0
pip 21.3 from C:\Users\ADMIN\AppData\Local\Programs\Python\Python310\lib\site-packages\pip(python3.10)

Suivez les instructions pour installer la dernière version de python pour votre plate-forme dans la documentation python https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

## Environnement virtuel

Nous vous recommandons de travailler dans un environnement virtuel chaque fois que vous utilisez Python pour des projets. Cela permet de garder vos dépendances pour chaque projet séparées et organisées. Les instructions pour configurer un environnement virtuel pour votre plate-forme peuvent être trouvées dans les docs python https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

## Dépendances PIP

Une fois que vous avez configuré et exécuté votre environnement virtuel, installez les dépendances en accédant au répertoire /API et en exécutant:

* pip install -r requirement.txt
ou
* pip3 install -r requirement.txt

Cela installera tous les packages requis que nous avons sélectionnés dans le fichier requirements.txt.

## Dépendances des clés

* Flask est un framework de microservices backend léger. Flask est nécessaire pour gérer les demandes et les réponses.
https://flask.palletsprojects.com/en/2.1.x/

* SQLAlchemy est la boîte à outils Python SQL et l'ORM que nous utiliserons pour gérer la base de données sqlite légère. Vous travaillerez principalement dans app.py et pourrez
https://www.sqlalchemy.org/

## Configuration de la base de données
Avec Postgres en cours d'exécution, restaurez une base de données à l'aide du fichier bibliotheque_database.sql fourni. Depuis le dossier backend dans le terminal, exécutez:

*psql bibliotheque_database < bibliotheque_database.sql*

Exécution du serveur

Dans le répertoire API, assurez-vous d'abord que vous travaillez avec votre environnement virtuel créé.

Pour exécuter le serveur sous Linux ou Mac, exécutez:
*export FLASK_APP=API
export FLASK_ENV=development
flask run*

Pour exécuter le serveur sous Windows, exécutez:
*set FLASK_APP=API
set FLASK_ENV=development
flask run*

La définition de la variable FLASK_ENV sur développement détectera les modifications de fichiers et redémarrera le serveur automatiquement.

La définition de la variable FLASK_APP sur flaskr indique à flask d'utiliser le répertoire flaskr et le fichier __init__.py pour rechercher l'application.

## RÉFÉRENCE API

*Démarrage
URL de base: à l'heure actuelle, cette application ne peut être exécutée que localement et n'est pas hébergée en tant qu'URL de base. L'application principale est hébergée par défaut, http://localhost:5000 ; qui est défini comme proxy dans la configuration frontale.*

## GESTION DES ERREURS

Les erreurs sont renvoyées sous forme d'objets JSON au format suivant : { "success":False "error": 400 "message":"Bad request }

L'API renverra quatre types d'erreurs en cas d'échec des requêtes : . 400 : Mauvaise requête . 500 : erreur interne du serveur . 422 : Impossible à traiter . 404 : Non trouvé

POINTS FINAUX (END POINTS)

## GET/livre

    GÉNÉRAL:
    Ce point de terminaison renvoie une liste d'objets livres, la valeur de réussite, le nombre total de livres.

    "livre": [
        {
            "auteur": "Bernard Dadie",
            "categorie_id": 13,
            "date_publication": "Sun, 02 Jan 2022 00:00:00 GMT",
            "editeur": "Bernard Dadie",
            "id": 2,
            "isbn": 1235,
            "titre": "Pagne noir"
        }
    ],
    "nombre_livre": 1,
    "success": true
    }

## GET/categorie

    GÉNÉRAL:
    Ce point de terminaison renvoie une liste d'objets categories, la valeur de réussite, le nombre total de categories.
    
    {
    "categorie": [
        {
            "id": 12,
            "libelle_categorie": "Roman"
        },
        {
            "id": 14,
            "libelle_categorie": "Article"
        },
        {
            "id": 15,
            "libelle_categorie": "Dictionnaire"
        },
        {
            "id": 16,
            "libelle_categorie": "Document"
        },
        {
            "id": 13,
            "libelle_categorie": "Conte"
        }
    ],
    "nombre_categorie": 5,
    "success": true
    }
    
    
## POST/supprimer (livre_id)

     GÉNÉRAL:
    Supprimer l'usine de l'ID donné si elle existe. Renvoie l'identifiant du livre supprimée, la valeur de réussite, le nombre total de livres

    {
    "livre_id": 1,
    "nombre_livres": 1,
    "success": true
    }


## POST/supprimer_categorie (categorie_id)

     GÉNÉRAL:
    Supprimer l'usine de l'ID donné si elle existe. Renvoie l'identifiant de la categorie supprimée, la valeur de réussite, le nombre total de livres
    
    {
    "categorie_id": 11,
    "nombre_categories": 0,
    "success": true
    }

## PATCH/modifier(livre_id)
    GÉNÉRAL:
    Ce point de terminaison est utilisé pour mettre à jour un livre donnée et
     Nous retournons un livre que nous mettons à jour
     
    {
    "livre_id": 2,
    "message": "livre modifié avec succes",
    "success": true
    }


## PATCH/modifier_categorie(categorie_id)
    GÉNÉRAL:
    Ce point de terminaison est utilisé pour mettre à jour un livre donnée et
     Nous retournons un livre que nous mettons à jour
     
     {
    "categorie_id": 13,
    "message": "libelle categorie modifié avec succes",
    "success": true
    }

## POST/ajout

    GÉNÉRAL:
     Ce point de terminaison permet de créer une nouveau livre 
     Dans le cas de la création d'une nouvelle question :
     On retourne l'ID du nouveau livre crée, le livre qui a été créée,  et le nombre de livres.
     
     {
    "Nombre_livre": 3,
    "livre_id": 9,
    "success": true
}

## POST/ajout_categorie

    GÉNÉRAL:
     Ce point de terminaison permet de créer une nouvelle categorie
     Dans le cas de la création d'une nouvelle question :
     On retourne l'ID de la nouvelle categorie crée, la categorie qui a été créée,  et le nombre de livres.
     
     {
    "categorie_id": 16,
    "nombre categorie": 4,
    "success": true
}


## GET/livre (livre_id)
    
    GÉNÉRAL:
     Ce point de terminaison permet de rechercher le livre par son id
     Dans le cas de la cette recherche :
     On retourne l'ID du livre, la reussite de la requête
     
      "livre": [
        {
            "auteur": "Jean Robert",
            "categorie_id": 15,
            "date_publication": "Sun, 10 May 2020 00:00:00 GMT",
            "editeur": "France Edition",
            "id": 9,
            "isbn": 1012,
            "titre": "Larousse"
        }
    ],
    "success": true
    
## GET/categorie (categorie_id)
    
    GÉNÉRAL:
     Ce point de terminaison permet de rechercher la categorie par son id
     Dans le cas de la cette recherche :
     On retourne l'ID de la categorie, la reussite de la requête    
     
     {
    "categorie": [
        {
            "id": 13,
            "libelle_categorie": "Bande Dessiné"
        }
    ],
        "success": true
    }
    
    
## GET/livre/categorie (categorie_id)    

    GÉNÉRAL:
     Ce point de terminaison permet de lister les livres qui sont dans une catégorie
     On retourne les livres, la reussite de la requête
     
     "livres": [
        {
            "auteur": "Jean Robert",
            "categorie_id": 15,
            "date_publication": "Sun, 10 May 2020 00:00:00 GMT",
            "editeur": "France Edition",
            "id": 3,
            "isbn": 1010,
            "titre": "Petit Robert"
        },
        {
            "auteur": "Jean Robert",
            "categorie_id": 15,
            "date_publication": "Sun, 10 May 2020 00:00:00 GMT",
            "editeur": "France Edition",
            "id": 8,
            "isbn": 1011,
            "titre": "Larousse"
        },
        {
            "auteur": "Jean Robert",
            "categorie_id": 15,
            "date_publication": "Sun, 10 May 2020 00:00:00 GMT",
            "editeur": "France Edition",
            "id": 9,
            "isbn": 1012,
            "titre": "Larousse"
        },
        {
            "auteur": "Larousse Guillaume",
            "categorie_id": 15,
            "date_publication": "Mon, 10 May 2021 00:00:00 GMT",
            "editeur": "France Edition",
            "id": 25,
            "isbn": 1014,
            "titre": "Larousse Junior"
        }
    ],
    "nombre_livres": 4,
    "success": true
}
    





  

   















   
