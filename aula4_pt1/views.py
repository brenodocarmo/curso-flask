"""Extesão do Flask"""


from flask import Flask, request


def init_app(app):
    """Inicialização de extensões"""

    @app.route("/")  # VIEWS
    def index():
        print(request.args)
        return "Hello Breno do Carmo"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"
        
