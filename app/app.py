from flask import Flask, jsonify, abort, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/app.sqlite3'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
#     # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
#     os.environ['DBUSER'], os.environ['DBPASS'], os.environ['DBHOST'], os.environ['DBNAME']
# )

DB = SQLAlchemy(app)
MIGRATE = Migrate(app, DB)
ma = Marshmallow(app)

from models import Modelo

class ModeloSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Modelo

@app.route('/modelo/', methods=['GET'])
def get_models():
  modelos = Modelo.query.all()
  modelo_schema = ModeloSchema()

  output = [modelo_schema.dump(modelo) for modelo in modelos]

  return jsonify({ 'models': output }), 200


@app.route('/modelo/<string:nome>', methods=['GET'])
def get_model(nome):
  modelos = Modelo.query.all()
  modelo_schema = ModeloSchema()

  modelo = list(filter(lambda modelo: modelo['nome'] == nome, modelos))
  print(modelo[0])
  modelo = modelo_schema.dump(modelo)
  print(modelo)
  
  return jsonify(modelo), 200


@app.route('/modelo/', methods=['POST'])
def create_model():
  if not request.json or not 'nome' in request.json:
    abort(400)

  modelo = Modelo(request.json['nome'], request.json['descricao'])
  DB.session.add(modelo)
  DB.session.commit()

  modelo_schema = ModeloSchema()
  modelo = modelo_schema.dump(modelo)

  return jsonify(modelo), 201


if __name__ == "__main__":
    app.run(debug=True)