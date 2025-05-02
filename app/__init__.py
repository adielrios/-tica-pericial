from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Chave já configurada diretamente (sem variáveis de ambiente)
    app.config['SECRET_KEY'] = '0697c4d4309a5a2a46459c3614b84051'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('postgres://'):
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgres://', 'postgresql://', 1)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    @app.route('/')
    def home():
        return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Ética Pericial</title>
            <style>
                body { font-family: Arial; margin: 0; padding: 0; background: #f5f5f5; }
                .container { max-width: 800px; margin: 0 auto; padding: 20px; }
                header { background: #00406c; color: white; padding: 20px; text-align: center; }
                .content { background: white; border-radius: 5px; padding: 20px; margin-top: 20px; }
                footer { text-align: center; margin-top: 20px; font-size: 12px; color: #666; }
            </style>
        </head>
        <body>
            <header>
                <h1>Ética Pericial</h1>
            </header>
            <div class="container">
                <div class="content">
                    <h2>Sistema de Gerenciamento de Laudos</h2>
                    <p>Implantação realizada com sucesso!</p>
                    <p>Domínio configurado e sistema operacional.</p>
                </div>
                <footer>
                    <p>Desenvolvido por Adiel Rios - contato: adiel.rios@abp.org.br</p>
                </footer>
            </div>
        </body>
        </html>
        """)
    
    return app
