# importando do módulo a classe
from flask import Flask, url_for, render_template

# iniciar a classe na variável
app = Flask(__name__)   # sempre no topo do código

# rotas


@app.route('/')
def ola():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    texto = f'''
    <b>CursoemVideo</b>: assista os vídeos no
    <a href="https://youtube.com/cursoemvideo" target="_blank">Canal no YouTube</a>
    <br> <a href='{url_for("ola")}'>página inicial</a>
    '''
    return texto

# função que executa nosso servidor web no modo desenvolvedor
app.run(debug=True)  # sempre no final do código
