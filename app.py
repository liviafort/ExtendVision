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


@app.route('/enviar_email')
def enviar_email():
    destinatarios = ['geovana.bezerra@academico.ifpb.edu.br']  # Lista de destinatários

    msg = Message('Assunto do e-mail', recipients=destinatarios)
    print(os.getenv('GMAIL_USER'), destinatarios, os.getenv('GMAIL_PASSWORD') )
    msg.body = 'Este é o corpo do e-mail enviado com Flask-Mail para múltiplos destinatários'

    try:
        mail.send(msg)
        return 'E-mail enviado com sucesso!'
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
