from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!"

@app.route('/tiago')
def tiago():
    return "Hello Tiago :-D"

'''
Ctrl + L - Limpar o terminal
Subir para o github:
1º - git add "nomedoarquivo.py"
2º - git commit -m "descrição do commit aqui"
3º - git push
PRONTO!!
'''