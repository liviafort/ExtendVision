from flask import Blueprint, render_template, jsonify, request, redirect, flash
from entitys.Login import Login
from entitys.Register import Register
import requests

app_get_routes = Blueprint('app_get_routes', __name__)
#Rotas para obter respostas dos formulários


@app_get_routes.route('/users/getlogin', methods=['POST'])
def get_login():
    """Rota que recebe os dados do formulário de login"""
    register_button = request.form.get("register")
    print(register_button)

    if register_button:
        return redirect('/register')

    data = request.json

    if data['email'] and data['password']:
        login = Login(data)
        message, its_valid = login.valida_login()
        print(message)

        if its_valid:
            message, type_user = login.tipo_usuario()
            
            if type_user == "student":
                return redirect("/student/home")
            elif type_user == "teacher":
                return redirect("/professor/home")
            else:
                return jsonify("Erro ao logar no sistema"), 500
    
    # flash('Email ou Senha faltando') ##TESTE
    return redirect("/")


@app_get_routes.route("/user/getregister", methods=['POST'])
def get_register():
    """Rota para receber dados do formulário de criação de usuário"""
    data = request.json
    paramters = ['email', 'firstname', 'password', 'gender', 'registration', 'birth']

    if all([bool(data[key]) for key in paramters]):
        register = Register(data)
        message, its_work = register.registrar()
        print(its_work)
            
        if its_work:
            print("FUNCIONOU KKKKKK")
            return redirect("/")
    
    return redirect("/register")
    