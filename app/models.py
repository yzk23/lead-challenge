from app import DB

class Modelo(DB.Model):
  __tablename__ = 'models'

  id = DB.Column(DB.Integer, primary_key=True)
  nome = DB.Column(DB.String(50))
  descricao = DB.Column(DB.String(100))

  def __init__(self, nome, descricao):
    self.nome = nome
    self.descricao = descricao