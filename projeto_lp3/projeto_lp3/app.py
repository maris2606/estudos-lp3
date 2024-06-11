# importa a classe flask do modulo flask
from flask import Flask

# java
# Aluno aluno = new Aluno();

# python
# a1 = Aluno()

# instancia o objeto flask que representa a aplicação
app = Flask("minha aplicação")


# rota + função
# rota: definição de um padrao de url
# função: função python com um retorno

# página home - /
# "'app', toda vez que a rota for '/', execute home"
@app.route("/") # @ decorator -> uma notação pra função home
def home():
    return '<h1>homepage</h1> <a href="/contatos">contatos</a>'

# página contatos - /contatos
@app.route("/contatos")
def contatos():
    return '<h1>contatos</h1>'

# página de produtos - /produtos
@app.route("/produtos")
def produtos(): # dá os mesmos nomes pra facilitar
    return '<h1>produtos</h1>'
