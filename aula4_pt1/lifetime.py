# # Contextos

# from flask import Flask
    
# app = Flask(__name__)

# ## 1 Contexto de configuraçao

# ### Add configuração
# app.config["FOO"] = "bar"
# app.config["DEBUG"] = "True"
# app.config["SQLALCHEMY_DB_URI"] = "mysql://.."

# ### Resgistrar Rotas
# @app.route("/")
# def funcao():
#     ...
# app.add_url_rule("/path", funcao)

# ### Inicializar extensões

# from flask_admin import Admin
# Admin.init_app(app)

# ### Registra Blueprints
# app.register_blueprint(...)

# ### add hooks

# @app.before_first_request(...)
# @app.erro_handler(...)

# ### Chamar outras factories

# views.init_app(app)

# ## 2 App Context

# ### App está pronta! 'app'

# ### Testar
# app.test_client
# debug
# objetos globaais do Flask
# (request, session, g)
# - Hooks

# from flask import current_app, g

# ## 3 Request Context

# ##user globasi do flask
# from flask import request, session, g


# request.args
# request.form