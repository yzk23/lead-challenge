from flask import Flask, jsonify, abort, request, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/app.sqlite3'

DB = SQLAlchemy(app)
MIGRATE = Migrate(app, DB)
ma = Marshmallow(app)

from models import Modelo
auth = HTTPBasicAuth()

class ModeloSchema(Schema):
  class Meta:
    model = Modelo

  descricao = fields.Str()
  nome = fields.Str()


@auth.get_password
def get_password(username):
  if username == 'isaac':
    return 'python'
  return None


@auth.error_handler
def unauthorized():
  return make_response(jsonify({ 'error': 'Unauthorized access' }), 403)


@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({ 'error': 'Not found' }), 404)


@app.route('/modelo/', methods=['GET'])
@auth.login_required
def get_models():
  modelos = Modelo.query.all()
  modelo_schema = ModeloSchema()

  modelos = [modelo_schema.dump(modelo) for modelo in modelos]

  return jsonify({ 'modelos': modelos }), 200


@app.route('/modelo/<string:nome>', methods=['GET'])
@auth.login_required
def get_model(nome):
  modelo = Modelo.query.filter_by(nome=nome).first()
  modelo_schema = ModeloSchema()

  modelo = modelo_schema.dump(modelo)
  if(modelo == {}):
    abort(404)
  
  return jsonify(modelo), 200


@app.route('/modelo/', methods=['POST'])
@auth.login_required
def create_model():
  if not request.json or not 'nome' in request.json or not 'descricao' in request.json:
    abort(400)

  modelo = Modelo(request.json['nome'], request.json['descricao'])
  DB.session.add(modelo)
  DB.session.commit()

  modelo_schema = ModeloSchema()
  modelo = modelo_schema.dump(modelo)

  return jsonify(modelo), 201


if __name__ == "__main__":
    app.run(debug=True)