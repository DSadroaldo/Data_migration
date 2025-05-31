from sqlalchemy.orm import sessionmaker
from models import db

def pegar_sessao():
  Session = sessionmaker(bind=db) # -> aqui estou criando uma conexão com meu BD
  session = Session() # -> instanciando esta sessão
  yield session
  session.close()