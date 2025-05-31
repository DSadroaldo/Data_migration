from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from dependencies import pegar_sessao
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
  '''
  Essa é a rota de autenticação de pedidos do sistema, criado por Adroaldo!
  '''
  return{"mensagem": "voce acessou a rota padrão de autenticação", "autenticado": False}

# criarmos uma rota de criar um user (criamos um item dentro do nosso db)
# toda informação que nos enviarmos p/nossa rota (post) será recebida pela nossa função async

@auth_router.post("/criar_conta") # postando informações nela e com elas estou editando dentr do sistema  
async def criar_conta(nome: str,email: str, senha: str, session = Depends(pegar_sessao)): # -> na estrutura do FastAPi eh necessario a tipagem de dados
    usuario = session.query(Usuario).filter(Usuario.email==email).first() # isso nos dara uma query no Banco
    if usuario:
       return{"mensagem": "Ja existe um usuário com este email"}
    else:
       novo_usuario = Usuario(nome, email, senha)
       session.add(novo_usuario)
       session.commit()
       return{"mensagem": "Usuário cadastrado com sucesso"}
    



