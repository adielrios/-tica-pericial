from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ética Pericial</title>
        <style>
            body { font-family: Arial; background: #f0f0f0; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            h1 { color: #003366; text-align: center; }
            footer { margin-top: 20px; text-align: center; font-size: 12px; color: #666; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sistema Ética Pericial</h1>
            <p>Bem-vindo ao sistema de gerenciamento de laudos periciais.</p>
            <p>Plataforma desenvolvida para a Associação
# Acesse a pasta do projeto
cd ~/etica-pericial

# Remova a estrutura complexa anterior
rm -rf app
rm -f wsgi.py

# Criar um arquivo app.py na raiz (isto é crítico!)
cat > app.py << 'EOF'
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ética Pericial</title>
        <style>
            body { font-family: Arial; background: #f0f0f0; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            h1 { color: #003366; text-align: center; }
            footer { margin-top: 20px; text-align: center; font-size: 12px; color: #666; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sistema Ética Pericial</h1>
            <p>Bem-vindo ao sistema de gerenciamento de laudos periciais.</p>
            <p>Plataforma desenvolvida para a Associação Brasileira de Perícias.</p>
            <hr>
            <p>Status: <strong>Operacional</strong></p>
            <footer>
                <p>Desenvolvido por Adiel Rios - adiel.rios@abp.org.br</p>
            </footer>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0")
