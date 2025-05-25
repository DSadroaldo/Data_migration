from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
  '''
  Essa é a rota de ordens de pedidos do sistema, criado por Adroaldo!
  '''
  return {"mensagem": "Voce acessou a rota de pedidos"}
