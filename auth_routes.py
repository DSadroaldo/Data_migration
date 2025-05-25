from fastapi import APIRouter
 
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
  '''
  Essa é a rota de autenticação de pedidos do sistema, criado por Adroaldo!
  '''
  return{"mensagem": "voce acessou a rota padrão de autenticação", "autenticado": False}


  # sqlalchemy, ORM(obj) - > permite que você interaja com o seu banco de dados usando objetos Python em vez de escrever comandos SQL diretamente. Ele "mapeia" as classes Python para tabelas do banco de dados e os objetos (instâncias dessas classes) para as linhas dessas tabelas.