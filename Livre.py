from os import abort
from token import AT
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# importation de flask


##################################################################################################################################
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:JunioR2000@localhost:5432/esagapi'
# chaine de connexion à la base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

####################################################################################################################################




####################################################################################################################################

class Categorie(db.Model):
    __tablename__ = 'categorie'
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String, nullable=False)
    livres = db.relationship('Livre', backref='categorie', lazy=True)

    def __init__(self,libelle_categorie):
        self.libelle_categorie = libelle_categorie
        
    def format(self):
        return {
            "id" : self.id,
            "libelle_categorie" : self.libelle_categorie
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()    
       



# table Livre
class Livre(db.Model):
    __tablename__ = 'livre'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer, unique=True, nullable=False)
    titre = db.Column(db.String(), nullable=False)
    date_publication = db.Column(db.Date(), nullable=False)
    auteur = db.Column(db.String(), nullable=False)
    editeur = db.Column(db.String(), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))

    def __init__(self, isbn, titre, date_publication, auteur, editeur, categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categorie_id = categorie_id

    def format(self):
        return {
            "id" : self.id,
            "isbn" : self.isbn,
            "titre" : self.titre,
            "auteur" : self.auteur,
            "date_publication" : self.date_publication,
            "editeur" : self.editeur,
            "categorie_id" : self.categorie_id
       }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()   


db.create_all()



####################################################################################################################################

####################################################################################################################################
                                                    
                                                    #AJOUT DE LIVRE#

@app.route('/ajout', methods=['POST'])
def ajout_livre():
    
        livres = Livre.query.all()
        body = request.get_json()
        new_isbn = body.get('isbn')
        new_titre = body.get('titre')
        new_datepublication = body.get('date_publication')
        new_auteur = body.get('auteur')
        new_editeur = body.get('editeur')
        new_categorie = body.get('categorie_id')
    

        livre = Livre(isbn=new_isbn, titre=new_titre,date_publication=new_datepublication, auteur=new_auteur, editeur=new_editeur, categorie_id=new_categorie)
        livre.insert()

        return jsonify({
        'success': True,
        'livre_id': livre.id,
        'Nombre_livre': len(livres)
     })

    
####################################################################################################################################


####################################################################################################################################
                                                #LISTER LES LIVRES#
@app.route('/livre', methods=['GET'])
def liste_livres():
    livres = Livre.query.all()
    livres_formatted = [livre.format() for livre in livres]
   
    return jsonify({

     'success': True,     
     'livre': livres_formatted,
     'nombre_livre':  len(livres)
    })
     
####################################################################################################################################



####################################################################################################################################
                                        # RECHERCHER UN LIVRE PAR SON ID
@app.route('/livre/<int:id>', methods=['GET'])
def selectionner_etudiant(id):
    livre = Livre.query.get(id)
    if livre:

        return jsonify({

            'success': True,
            'livre': [livre.format()]
        })
    else:
        return {'message': 'Ce livre n\'existe pas'}
####################################################################################################################################


####################################################################################################################################
                                                # MODIFIER UN LIVRE
@app.route('/modifier/<int:id>', methods=['PATCH'])
def modifier_livre(id):
    try:
        livres = Livre.query.get(id)
        body = request.get_json()
        livres.isbn = body.get('isbn', None)
        livres.titre = body.get('titre', None)
        livres.date_publication = body.get('date_publication', None)
        livres.auteur = body.get('auteur', None)
        livres.editeur = body.get('auteur', None)
        livres.categorie_id = body.get('categorie_id', None)

        livres.update()

    except AttributeError:
        return jsonify({
            'success': False,
            'message': 'le livre que vous voulez modifier n\'existe pas'
        })    

    except TypeError:
        return jsonify({
            'success': False,
            'message': 'Aucune reponse après votre requête'
        })
    else:
        return jsonify({
            'success': True,
            'livre_id': id,
            'message': 'livre modifié avec succes'
        })
####################################################################################################################################

                                    # SUPPRIMER UN LIVRE


@app.route('/supprimer/<int:id>', methods=['POST'])
def delete_livre(id):
    try:
        livre = Livre.query.get(id)
        livre.delete()
        livres = Livre.query.all()

    except AttributeError:
        return jsonify({
            'success': False,
            'message': 'Ce livre que vous voulez supprimer n\'existe pas'
        })
    except TypeError:
        return jsonify({
            'success': False,
            'message': 'Aucune reponse après votre requête'
        })

    else:
        return jsonify({
            'success': True,
            'nombre_livres': [livre.format() for livre in livres],
            'livre_id': id,
            'nombre_livres': len(livres)
        })
####################################################################################################################################



####################################################################################################################################
                                            ##ERROHANDLER

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'Mauvaise requête'
    }), 400


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'erreur interne du serveur'
    }), 500


@app.errorhandler(405)
def method_not_error(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'Method not allowed'
    }), 405


@app.errorhandler(422)
def unprocessable_error(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'Méthode Non Autorisée'
    }), 422

@app.errorhandler(404)
def Not_Found_error(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'Non trouvé'
    }), 404


####################################################################################################################################


####################################################################################################################################
                                            #AJOUT D'UNE CATEGORIE#
@app.route('/ajout_categorie', methods=['POST'])
def ajout_categorie():
    categories=Categorie.query.all()
    body = request.get_json()
    new_libelle_categorie = body.get('libelle_categorie',None)
    
     
    categorie = Categorie(libelle_categorie=new_libelle_categorie)
    categorie.insert()
    return jsonify({
        'success': True,
        'categorie_id': categorie.id,
        'nombre categorie': len(categories)
    })

####################################################################################################################################


####################################################################################################################################
                                                #LISTER LES CATEGORIES#
@app.route('/categorie', methods=['GET'])
def liste_categories():
    categories = Categorie.query.all()
    categories_formatted = [categories.format() for categories in categories]
    
   
    return jsonify({

     'success': True,   
     'categorie': categories_formatted,
     'nombre_categorie': len(categories)
    })
    
####################################################################################################################################


####################################################################################################################################
                                            # RECHERCHER UNE CATEGORIE PAR SON ID

@app.route('/categorie/<int:id>', methods=['GET'])
def selectionner_categorie(id):

    
        categorie = Categorie.query.get(id)
        if categorie : 
            return jsonify ({
                'success' : True,
                'categorie': [categorie.format()]
            })
        else:
            return jsonify({
                'message':'Cette categorie n\'existe pas'
            })    
    
        
        
        
####################################################################################################################################


####################################################################################################################################
                                        # MODIFIER LE LIBELLE D'UNE CATEGORIE
@app.route('/modifier_categorie/<int:id>', methods=['PATCH'])
def modifier_categorie(id):
    try:
        categories = Categorie.query.get(id)
        body = request.get_json()
        categories.libelle_categorie = body.get('libelle_categorie', None)

        categories.update()

    except AttributeError:
        return jsonify({
            'success': False,
            'message': 'Cette categorie que vous voulez modifier n\'existe pas'
        })
    except TypeError:
        return jsonify({
            'success': False,
            'message': 'Aucune reponse après votre requête'
        })
    else:    

        return jsonify({
        'success': True,
        'categorie_id': id,
        'message': 'libelle categorie modifié avec succes'
        })
####################################################################################################################################


####################################################################################################################################
                                                
                                                # SUPPRIMER UNE CATEGORIE

@app.route('/supprimer_categorie/<int:id>', methods=['POST'])
def delete_categorie(id):
    try:
        categorie = Categorie.query.get(id)
        categorie.delete()
        categories = Categorie.query.all()
    except AttributeError:
        return jsonify({
            'success': False,
            'message': 'Cette categorie que vous voulez supprimer n\'existe pas'
        })
    except TypeError:
        return jsonify({
            'success': False,
            'message': 'Aucune reponse après votre requête'
        })
    else:    
        return jsonify({
        'success': True,
        'nombre_categories': [categorie.format() for categorie in categories],
        'categorie_id': id,
        'nombre_categories': len(categories)
        })
#################################################################################################################################### 