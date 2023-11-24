from flask import Flask
from routes.routes import app_routes
from routes.bd_routes import app_bd
from routes.get_routes import app_get_routes
from flask_mail import Message, Mail
import os

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'sua_chave_secreta'

app.register_blueprint(app_routes)
app.register_blueprint(app_bd)
app.register_blueprint(app_get_routes)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Porta do servidor de e-mail (pode variar)
app.config['MAIL_USERNAME'] = os.getenv('GMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('GMAIL_PASSWORD')  # Obtém a senha do ambiente
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('GMAIL_USER')
app.config['MAIL_USE_TLS'] = True  # Use TLS para segurança
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
app.config['mail'] = mail


if __name__ == '__main__':
    app.run()
