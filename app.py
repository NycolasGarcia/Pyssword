from flask import Flask, render_template

import webview
from threading import Thread

app = Flask(__name__, static_folder='./static', template_folder='./templates')

# Register the blueprints

@app.route("/")
def index():
    return render_template('index.html', active_page='index')

# Variável global para controlar a janela
window = None

if __name__ == '__main__':
    # Inicializa o banco de dados
    #init_db()
    
    # Cria a janela
    window = webview.create_window('Pyssword', app, frameless=False, height=720, width=1280)
    
    # Inicia a aplicação
    webview.start()