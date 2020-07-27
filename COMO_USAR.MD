# MAS COMO CONFIGURAR?!

## Aqui está a árvore do projeto:

```sh
Blog/

└── app
    ├── __init__.py
    ├── app.py
    ├── config
    │   ├── __init__.py
    │   └── config.py                                               
    ├── model                                                       
    |   ├── __init__.py
    │   └── model.py                                                
    ├── static
    │   ├── css
    │   └── js
    ├── templates
    └── views
        ├── __init__.py
        └── views.py
```

App/\__init__.py 
    é um arquivo vazio

App/app.py
   É onde esta o 'core' do app, onde a class Flask foi instanciada

App/config/\__init__.py
   É onde esta sendo atribuido todas as outras classes

App/config/config.py
   É onde esta sendo atribuido os valores de configuração
   Exemplo: app.config['SECRET_KEY'] = 'SECRET'

App/model/\__init__.py
   É onde esta sendo configurado o banco de dados:
     O SQLAlchemy, Marshmallow e o Migrante esta sendo instânciados aqui

App/model/model.py
   É onde você pode criar suas classes onde o ORM do 
      SQLAlchemy vai gerar os metadados e configurações para o banco do çe dados

App/static
    É onde ficara os arquivos estáticos:
      Css, js, jquery, imagens, etc..

App/templates
    É onde ficara os templates (arquivos html)
