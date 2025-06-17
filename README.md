# Data_migration

Repositório para projetos de migração de dados.

Edições

<!-- TODO create_engine
> gerado nosso motor Banco de Dados, utilizado o create_engine
# onde nos iremos criar nossas classes de banco de dados
# permite que você interaja com o seu banco de dados usando objetos Python em vez de escrever comandos SQL diretamente. Ele "mapeia" as classes Python que são traduzidas no para tabelas do banco de dados e os objetos (instâncias dessas classes) para as linhas dessas tabelas.
# para migração de dados dentro do alchemy utilizamos uma biblioteca para isso a alembic
  # processo de install do alembic, utilizamos o terminal com pip install e executamos, tbm, por ele mesmo (alembic init alembic
-->

<!-- com a mudança do diretório Data_migration(rename) houve a necessidade de alterar a pasta de inicialização do git
comando:
git remote set-url origin https://github.com/DSadroaldo/Data_migration.git // > montando nova URL
(https://github.com/DSadroaldo/Data_migration.git*https://github.com/DSadroaldo/Data_migration.githttps://github.com/DSadroaldo/Data_migration.git)
![Alter_directory_init](alter_directory_init.png)
![ALteracao no codigo](alter_code_directory.png)
-->
<!-- ![doc_autorizacao_usuario](docs_API_auth.png) -->

![rota_pedidos](assets/docs_rota_pedido.png)

<!-- TODO Alembic - comandos processo Migracao:
  alembic revision --autogenerate -m "text mudança  - > cria um versionamento do BD
  alembic upgrade head                              - > aplica o versionamento / implementar as mudanças no db
Entendendo o processo de 'Migration' no SQLAlchemy, hávera situações em nosso banco de dados já existente onde precisaremos fazer uma alteração, onde poderá alterar a estrutura do BD e, tbm, alterar os registros já existentes no BD.
Para isso, existe uma biblioteca no SQLAlchemy que atua de forma segura nesses processos de Migration, chamada Alembic... Basicamente esta ela apoia no processo de migração de uma versão de seu BD para outra versão de forma segura.
-->

<!-- TODO Autogenerate: processo de migração dentro do almebic gera o q chamamos de versões de migração
o autogenerate é o cara que irá gerar o arquivo de migração, dizendo como irá funcionar o processo de migração.
diversos comandos em  python de como ele irá gerar estas mudanças no banco -->

<!-- criacao da conta do usuario
  como estruturar o processo de crição de itens no seu banco de dados
  garantir sessoes no banco de dados maneira robusta e escalavel
  atender a fechar sessoes, sem deixa-las abertas
  A base do processo de criação rotas, endpoints, links
  # importante (sqlalchemy__utils)Ela oferece uma coleção de funções úteis e tipos de dados personalizados que estendem as funcionalidades do SQLAlchemy(utilizaremos a ChoiceType)
  # uma lista, tupla de tuplas
    -->

<!--
  # sqlalchemy, ORM(obj) - > permite que você interaja com o seu banco de dados usando objetos Python em vez de escrever comandos SQL diretamente. Ele "mapeia" as classes Python para tabelas do banco de dados e os objetos (instâncias dessas classes) para as linhas dessas tabelas. -->

<!-- Sessions Restrições
 e importante gerenciar as sessoes de conexões no banco de dados
  isto é, torna-se impreenscídivel a finalização das conexões abertas no banco de   dados
  CRIAR | FAZER o q TEM FAZER | FECHAR -->

  <!-- Criamos primeiro escopo de rota de criação e autenticação de usuário
  sem nos atermos a regras mais seguras. Aqui nos atemos a gerar a teste de rota e create de um item 
  a nível de teste  -->

<!-- TODO dependencies(pegar_sessao), criado uma função cria esta sessao, dar a sessao a rota para funcionar
e quando esta rota acabar(independente de dar certo ou não) ela fechará
Dentro do FastAPI, "Depends" é um sistema poderoso e intuitivo de Injeção de Dependência
-->
<!-- TODO Session Close, a fim de, tratar uma possível session presa na memória (return), tratamos com yield
 retorna um valor mas não encerra a execução da nossa função
 adotamos uma estrutura de try
 try-finally no gerenciamento de sessao
   -->

   <!-- TODO sys.path.append(os.abspath(os.path.join(os.path.dirname(__file__), "..")))
   
    entendendo a linha
    Atuando com path diferentes dentro do projeto, primeiro temos q importar algumas bibliotecas: sys, os 
     assim devemos entender q ao executar ele ve os arquivos q estão dentro da pasta do arquivo assim como os arquivos q estão dentro da pasta python
     devemos então mostrar, além desses, o caminho q precisamos que ele verifique
     sys.path.append() //-> estou atribuindo(append) ao sistema de arquivos/caminhos(path)
     sys.path.append(os.path.abspath) //-> caminho absoluto
     os.path.join(os.path.dirname(__file__), "..") //-> pegando o caminho do meu arquivo (alembic/env) e join com ..
     por fim fica assim
     sys.path.append(os.abspath(os.path.join(os.path.dirname(__file__), ".."))) -->
