# onde nos iremos criar nossas classes de banco de dados
# permite que você interaja com o seu banco de dados usando objetos Python em vez de escrever comandos SQL diretamente. Ele "mapeia" as classes Python que são traduzidas no para tabelas do banco de dados e os objetos (instâncias dessas classes) para as linhas dessas tabelas.
# para migração de dados dentro do alchemy utilizamos uma biblioteca para isso a alembic
  # processo de install do alembic, utilizamos o terminal com pip install e executamos, tbm, por ele mesmo (alembic init alembic
from sqlalchemy import create_engine  , Column, Integer, Float, Boolean, ForeignKey, String  #permite criarmos o banco de dados
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType # (lista suspensa de escolhas)
#===================================================== #

# cria a conexão de seu banco
db = create_engine("sqlite:///banco.db") # aqui, quando no deploy colocamos o link do nosso banco

# criar nossa base de dados(importando sqlalchemy.orm)
Base = declarative_base()

# criar as classes/tabelas do banco
# usuario
class Usuario(Base):
  __tablename__ = "usuarios"
# importante que no sqlalchemy há forte tipagem de dados(por isso devemos declarar ela no import)
  id = Column("id", Integer, primary_key=True, autoincrement=True)
  nome = Column("nome", String)
  email = Column("email", String, nullable=False)
  senha = Column("senha", String)
  ativo = Column("ativo", Boolean, default=True)
  # admin = Column("admin", Boolean, default=False)

# parametro __init__, sempre q for criar um usuario o q necessariamente nosso sistema exige
def __init__(self, nome, email, senha, ativo=True, admin=False):
  self.nome = nome
  self.email = email
  self.senha = senha
  self.ativo = ativo
  # self.admin = admin

# pedido
class Pedido(Base):
  __tablename__ = "pedidos"
  
  # importante (sqlalchemy__utils)Ela oferece uma coleção de funções úteis e tipos de dados personalizados que estendem as funcionalidades do SQLAlchemy(utilizaremos a ChoiceType)  
  # uma lista, tupla de tuplas
  
  #choiceType#
  # uma tupla com ("chave"(que vai pro banco), valor(que visualizamos))
  # STATUS_PEDIDOS = (
  #   ("PENDENTE", "PENDENTE"),
  #   ("CANCELADO","CANCELADO"),
  #   ("FINALIZADO","FINALIZADO")
  # )

  id = Column("id", Integer, primary_key=True, autoincrement=True)
  status = Column("status", String) #garantia de INTEGRIDADE no db
  usuario = Column("usuario", ForeignKey("usuarios.id"))
  preco = Column("preco", Float)
  # itens = 


# sempre que criarmos um usuário o q devemos ter como 
  def __init__(self, usuario, status="PENDENTE", preco=0):
    self.usuario = usuario
    self.preco = preco
    self.stauts = status # aqui temos uma condição pré-definida


# itensPedido
class ItemPedido(Base):
  __tablename__ = "itens_pedido"

  id = Column("id", Integer, primary_key=True, autoincrement=True)   
  quantidade = Column("quantidade", Integer)
  sabor =  Column("sabor", String)
  tamanho = Column("tamanho", String) 
  preco_unitario = Column("preco_unitario", Float)
  pedido = Column("pedido", ForeignKey("pedidos.id")) # preciso de um pedido associado a ele

def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
    self.quantidade = quantidade
    self.sabor = sabor
    self.tamanho = tamanho
    self.preco_unitario  = preco_unitario
    self.pedido = pedido


# criação dos metadados do seu banco dados (cria efetivamente o banco de dados)
#----vamos rodar nosso construtor de banco de dados----#
#  terminal roda | "alembic revision --autogenerate -m "Migration initial""
#  executamos nosso banco(gerar) | "alembic upgrade head"



    # utilizamos a biblioteca alembic
    # o alembic precisa ser inicializado, pois assim, ele gera o diretorio onde teremos estara nosso banco 