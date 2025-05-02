from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return """
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
                    <h2>Sistema de Assistência Pericial</h2>
                    <p>Sistema implantado com sucesso!</p>
                    <p>Em breve: módulos de gestão de laudos e avaliações.</p>
                </div>
                <footer>
                    <p>Desenvolvido por Adiel Rios - contato: adiel.rios@abp.org.br</p>
                </footer>
            </div>
        </body>
        </html>
        """
    
    return app
