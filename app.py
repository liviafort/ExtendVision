from flask import Flask
from routes import app_routes

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'sua_chave_secreta'

app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run()
