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

    email = request.form.get("email")
    password = request.form.get("password")

    if email and password:
        login = Login(email, password)
        message, its_valid = login.valida_login()
        print(message)

        if its_valid:
            message, type_user = login.tipo_usuario()
            
            if type_user == "student":
                return redirect("/student/home")
            elif type_user == "teacher":
                return redirect("/professor/home")
            else:
                return redirect("/")
    
    # flash('Email ou Senha faltando') ##TESTE
    return redirect("/")

@app_get_routes.route("/user/getregister", methods=['POST'])
def get_register():
    """Rota para receber dados do formulário de criação de usuário"""
    user_email = request.form.get("email")
    user_name = request.form.get("firstname")
    user_password = request.form.get("password")
    user_confirm_password = request.form.get("confirmPassword")
    user_gender = request.form.get("gender")
    user_registration = request.form.get("registration")
    user_birth = request.form.get("birth")
    user_title = request.form.get("title")

    if user_email and user_name and user_password and user_confirm_password and user_gender and user_registration and user_birth and user_title:

        if user_password != user_confirm_password:
            print("PASSWORDS DIFERENTES")
            return redirect("/register")
        
        register = Register(user_name, user_email, user_password, user_gender, user_registration, user_birth, user_title)
        message, its_work = register.registrar()
        print(its_work)
            
        if its_work:
            print("FUNCIONOU KKKKKK")
            return redirect("/")
    
    return redirect("/register")
    