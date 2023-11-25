from flask import Blueprint, render_template, jsonify, request, redirect, flash
from entitys.Login import Login
from entitys.Register import Register
import requests

app_get_routes = Blueprint('app_get_routes', __name__)
#Rotas para obter respostas dos formulários


@app_get_routes.route('/user/getlogin', methods=['POST'])
def get_login():
    """Rota que recebe os dados do formulário de login"""

    data = request.json

    if data['email'] and data['password']:
        login = Login(data)
        message, its_valid = login.valida_login()
        print(message)

        if its_valid:
            message, type_user = login.tipo_usuario()
            if type_user == "student":
                return jsonify({"user_type": "student"})
            elif type_user == "teacher":
                return jsonify({"user_type": "teacher"})
            else:
                return jsonify({"error": "Erro ao entrar no sistema"}), 500
            
    return jsonify({"error": "Erro ao entrar no sistema"}), 500
    # flash('Email ou Senha faltando') ##TESTE


@app_get_routes.route("/user/getregister", methods=['POST'])
def get_register():
    """Rota para receber dados do formulário de criação de usuário"""
    data = request.json
    paramters = ['email', 'name', 'password', 'gender', 'registration', 'birth']

    if all([bool(data[key]) for key in paramters]):
        register = Register(data)
        message, its_work = register.registrar()
            
        if its_work:
            return jsonify({"works": "Conta criada com sucesso!"})
    
    return jsonify({"error": "Erro ao efetuar cadastro"}), 500


@app_get_routes.route("/user/getproject", methods=['POST'])
def get_register_project():
    """Rota para receber dados do formulário de criação de projeto"""
    data = request.json
    paramters = ['email', 'area', 'theme', 'title', 'description', 'begin_date', 'end_date', 'register_begin', 'register_end', 'workload', 'available_spots', 'scholarship']

    if all([bool(data[key]) for key in paramters]):
        register = Register(data)
        message, its_work = register.registrar_projeto()

        if its_work:
            return jsonify({"works": "Projeto criada com sucesso!"})

    return jsonify({"error": "Erro ao efetuar cadastro"}), 500


@app_get_routes.route("/user/getInscription", methods=['POST'])
def get_project_student():
    """Rota para receber dados do formulário de criação de projeto"""
    data = request.json
    paramters = ['id_project', 'id_user']

    if all([bool(data[key]) for key in paramters]):
        register = Register(data)
        message, its_work = register.registrar_projeto_estudante()

        if its_work:
            return jsonify({"works": "Solicitação realizada com sucesso!"})

    return jsonify({"error": "Erro ao efetuar solicitação"}), 500


@app_get_routes.route("/user/getInscriptionAprove", methods=['POST'])
def get_inscription_aprove():
    """Rota para receber dados do formulário de criação de projeto"""
    data = request.json
    paramters = ['id_project', 'id_user']

    if all([bool(data[key]) for key in paramters]):
        register = Register(data)
        message, its_work = register.aceitar_solitacao()

        if its_work:
            return jsonify({"works": "Solicitação realizada com sucesso!"})

    return jsonify({"error": "Erro ao efetuar solicitação"}), 500

@app_get_routes.route("/user/getInscriptionRefused", methods=['POST'])
def get_inscription_refused():
    """Rota para receber dados do formulário de criação de projeto"""
    data = request.json
    paramters = ['id_project', 'id_user']

    if all([bool(data[key]) for key in paramters]):
        register = Register(data)
        message, its_work = register.recusar_solitacao()

        if its_work:
            return jsonify({"works": "Solicitação realizada com sucesso!"})

    return jsonify({"error": "Erro ao efetuar solicitação"}), 500