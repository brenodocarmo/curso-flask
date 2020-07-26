from flask import Flask

app = Flask("__name__")

@app.route("/")
def index():
    return "Hello Breno Carmo"


@app.route("/sobre")
def sobre():
    return "Meu site de delivery"
