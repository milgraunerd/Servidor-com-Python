  
from flask import Flask, render_template

#render_template - função de python que tem no flask que renderiza templates

app = Flask(__name__)

@app.route('/') #Cria uma nova rota
def index():
    return render_template('index.html', lista = ['Tiago', 'Rogério', 'Mateus', 'Yan', 'Daniel'])

@app.route('/<nome>')
def ola_com_nome(nome):
    return render_template('index.html', nome_pessoa=nome)