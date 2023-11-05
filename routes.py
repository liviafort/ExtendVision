from flask import Blueprint, render_template, jsonify, request
from models.users import get_user_by_id, create_user, update_user, delete_user

from database import bd2

app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/')
def index():
    return render_template("home/home.html")


@app_routes.route('/user/<int:user_id>', methods=['GET'])
def get_users(user_id):
    return get_user_by_id(user_id)


@app_routes.route('/user/', methods=['POST'])
def create_user_route():
    data = request.json
    required_fields = ['registration', 'password', 'name', 'title', 'gender', 'birth_date', 'type']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_user_id = create_user(**data)

    return jsonify({'message': 'Novo usuário criado com sucesso', 'user_id': new_user_id})

@app_routes.route('/user/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.json
    required_fields = ['registration', 'password', 'name', 'title', 'gender', 'birth_date', 'type']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_user_id = update_user(user_id, **data)

    return jsonify({'message': 'Usuário atualizado com sucesso', 'user_id': new_user_id})

@app_routes.route('/user/<int:user_id>', methods=['DELETE'])
def delete_users(user_id):
    return delete_user(user_id)