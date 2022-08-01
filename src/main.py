import json

"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, User, Planetas, Personajes
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
# setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    users= User.query.all
    UserList = lit(map(lambda obj:obj.serialize(),users))
    print(usersList)

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200



@app.route('/users/<int:id_usuario>/favoritos', methods=['GET'])
def los_favoritos(id_usuario):

    response_personajes = User.query.filter_by(id=id_usuario).first().persFavoritos
    response_planetas = User.query.filter_by(id=id_usuario).first().planFavoritos
    Personajes = list(map(lambda obj: obj.serialize(), response_personajes))
    Planetas = list(map(lambda obj: obj.serialize(), response_planetas))

    return jsonify({
        "persFavoritos": Personajes,
        "planFavoritos": Planetas
    }), 200


@app.route('/favoritos/personajes/<int:personajes_id>', methods=['POST'])
def create_pers_favorito(personajes_id):
    id_usuario = 1
    user = User.query.get(id_usuario)
    personaje = Personajes.query.get(personajes_id)
    listaFavoritos = User.query.filter_by(id=id_usuario).first().persFavoritos
    listaFavoritos.append(personaje)
    db.session.commit()

    return jsonify({
        "success": "favorite added",
        "persFavoritos": list(map(lambda obj: obj.serialize(), listaFavoritos))
    }), 200


@app.route('/favoritos/personajes/<int:personajes_id>', methods=['DELETE'])
def delete_pers_favorito(personajes_id):
    id_usuario = 1
    user = User.query.get(id_usuario)
    personaje = Personajes.query.get(personajes_id)
    listaFavoritos = User.query.filter_by(id=id_usuario).first().persFavoritos
    listaFavoritos.remove(personaje)
    db.session.commit()

    return jsonify({
        "success": "favorite deleted",
        "planFavoritos": list(map(lambda obj: obj.serialize(), listaFavoritos))
    }), 200


@app.route('/favoritos/planetas/<int:planetas_id>', methods=['POST'])
def create_plan_favorito(planetas_id):
    id_usuario = 1
    user = User.query.get(id_usuario)
    planeta = Planetas.query.get(planetas_id)
    listaFavoritos = User.query.filter_by(id=id_usuario).first().planFavoritos
    listaFavoritos.append(planeta)
    db.session.commit()

    return jsonify({
        "success": "favorite added",
        "planFavoritos": list(map(lambda obj: obj.serialize(), listaFavoritos))
    }), 200


@app.route('/favoritos/planetas/<int:planetas_id>', methods=['DELETE'])
def eliminar_planeta_favorito(planetas_id):
    id_usuario = 1
    user = User.query.get(id_usuario)
    planeta = Planetas.query.get(planetas_id)
    listaFavoritos = User.query.filter_by(id=id_usuario).first().planFavoritos
    listaFavoritos.remove(planeta)
    db.session.commit()
    return jsonify({
        "success": "favorite deleted",
        "planFavoritos": list(map(lambda obj: obj.serialize(), listaFavoritos))
    }), 200


@app.route('/personajes', methods=['GET'])
def obtener_personajes():
    personajes_query = Personajes.query.all()
    all_personajes = list(map(lambda obj: obj.serialize(), personajes_query))
    return jsonify({
        "result": all_personajes
    }), 200


@app.route('/personajes/<int:personaje_id>', methods=['GET'])
def obtener_detalles_personaje(personaje_id):
    personaje_query = Personajes.query.get(personaje_id)
    data_personaje = personaje_query.serialize()
    return jsonify({
        "result": data_personaje
    }), 200


@app.route('/planetas', methods=['GET'])
def obtener_planetas():
    planetas_query = Planetas.query.all()
    all_planetas = list(map(lambda obj: obj.serialize(), planetas_query))
    response_body = {
        "result": all_planetas
    }
    return jsonify(response_body), 200


@app.route('/planetas/<int:planeta_id>', methods=['GET'])
def obtener_detalles_planeta(planeta_id):
    planeta_query = Planetas.query.get(planeta_id)
    data_planeta = planeta_query.serialize()
    response_body = {
        "result": data_planeta
    }
    return jsonify(response_body), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)