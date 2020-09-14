from flask import Flask, jsonify, abort, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

models = [
  {
    'nome': 'AlexNet',
    'descricao': 'Modelo de CNN para classificação de imagens. Possui uma estrutura complexa com milhões de parâmetros, o que requer um volume imenso de dados para treinamento.'
  },
  {
    'nome': 'AlexNet2',
    'descricao': 'Modelo de CNN para classificação de imagens. Possui uma estrutura complexa com milhões de parâmetros, o que requer um volume imenso de dados para treinamento.'
  },
]


@app.route('/modelo/', methods=['GET'])
def get_models():
  return jsonify({ 'models': models })


@app.route('/modelo/<string:nome>', methods=['GET'])
def get_model(nome):
  model = [model for model in models if model['nome'] == nome]
  
  return jsonify(model)


@app.route('/modelo/', methods=['POST'])
def create_model():
  if not request.json or not 'nome' in request.json:
    abort(400)

  model = {
    'nome': request.json['nome'],
    'descricao': request.json['descricao']
  }

  models.append(model)

  return jsonify(model), 201


if __name__ == "__main__":
    app.run(debug=True)