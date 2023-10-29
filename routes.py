from flask import Blueprint, render_template
from models.users import get_user_by_id

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return render_template("home/home.html")

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        user_data = {
            'id': user.id,
            'registration': user.registration,
            'name': user.name,
        }
        return jsonify(user_data)
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404 
