# instalando as bibliotecas necessarias
# fastAPI
# uvicorn (asgi server) gerenciador do nosso servidor
# sqlalchemy(criação do nosso banco de dados)
# passlib[bcrypt] - criptografar de forma segura as senhas ali salvas (forma correta de salvar em um proj backend)
# python-jose[criptography] - token informalções embed jwt (json web token)
# python-dotenv(gerenciar nossas variaveis de ambiente)
# python-multipart
# para rodar o nosso codigo, executar no terminal: uvicorn main:app --reload
# uvicorn main:app --reload  --> nos vamos criar dentro do nosso servidor uvicorn atraves do nosso arq main a instancia app do fastAPI
# em resuno sempre q quesermos criar um site, vc precisa 


from fastapi import FastAPI
app = FastAPI()

# somente após a criação da nossa classe app, que podemos importar nossos outros arquivos (order/auth)
from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

# criação de rotas, as rotas de seu sistema são definições do q ira ocorrer quando o usuáiro fizer um requisiçaõ
# requisições em api / acessamos p/requisições através de endpoints (formato Json)
# Rest APIs 
# Get         - > Leitura/pegar
# Post        - > enviar
# Put/Patch   - > edição 
# Delete      - > deletar 
# O caminho de uma rota será o caminho de uma rota
# O arquivo main sera o unico o qual devemos nos preocupar com a ordens das coisas (referencia singular)
# diferenças entre framework e uma biblioteca será o fato q programa dentro do framework, vc cria seu programa dentro das regras do framework