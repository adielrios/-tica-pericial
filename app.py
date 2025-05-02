from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Configurar chave secreta
app.config['SECRET_KEY'] = '0697c4d4309a5a2a46459c3614b84051'

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ética Pericial</title>
        <style>
            body { font-family: Arial; background: #f8f9fa; margin: 0; padding: 0; }
            .container { max-width: 800px; margin: 0 auto; padding: 20px; }
            header { background: #003366; color: white; padding: 20px; text-align: center; }
            .content { background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); margin-top: 20px; }
            footer { text-align: center; margin-top: 20px; font-size: 14px; color: #6c757d; }
        </style>
    </head>
    <body>
        <header>
            <h1>Sistema Ética Pericial</h1>
        </header>
        <div class="container">
            <div class="content">
                <h2>Bem-vindo ao Sistema</h2>
                <p>Este é o sistema de gerenciamento de laudos periciais da ABP.</p>
                <p>Status: <strong>Implantação concluída com sucesso!</strong></p>
                
                <h3>Módulos Planejados:</h3>
                <ul>
                    <li>Cadastro de Laudos</li>
                    <li>Gestão de Perícias</li>
                    <li>Relatórios e Estatísticas</li>
                </ul>
            </div>
            <footer>
                <p>Desenvolvido por Adiel Rios | adiel.rios@abp.org.br</p>
            </footer>
        </div>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
