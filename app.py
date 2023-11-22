from flask import Flask
from routes.routes import app_routes
from routes.bd_routes import app_bd
from routes.get_routes import app_get_routes

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'sua_chave_secreta'

app.register_blueprint(app_routes)
app.register_blueprint(app_bd)
app.register_blueprint(app_get_routes)

if __name__ == '__main__':
    app.run()
