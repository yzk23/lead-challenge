# Flask API
Uma API em Flask para consulta e cadastro de modelos de IA.

## Tools
- Flask
- SQLAlchemy
- Marshmallow

## Requirements
- Python
- Virtualenv

## Install
Primeiramente deve-se criar um ambiente virtual (venv) para o isolamento das dependências do projeto com os da sua máquina:
```bash
virtualenv env
```
Ativar o ambiente virtual:
```bash
env/Scripts/activate
```
Instalando as dependências:
```bash
pip install -r requirements.txt
```
Configurar a variável de ambiente FLASK_APP:
```bash
cd app/
$env:FLASK_APP=app.py
```
Executar as migrations:
```bash
flask db upgrade
```
Rodar a aplicação:
```bash
flask run
```
Obs.: Todos os comandos foram executados em ambiente Windows via PowerShell

## Routes
- GET http://127.0.0.1/5000/modelo/
- GET http://127.0.0.1/5000/modelo/{id_modelo}
- POST http://127.0.0.1/5000/modelo/
