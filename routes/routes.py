from flask import Blueprint, render_template, jsonify, request, redirect

app_routes = Blueprint('app_routes', __name__)

#Rotas para as páginas principais da aplicação

@app_routes.route('/')
def login():
    return render_template("users/signin.html")

@app_routes.route('/register')
def register():
    return render_template("users/signup.html")

@app_routes.route('/projects/register')
def registerProject():
    return render_template("projects/register.html")

@app_routes.route('/projects/project')
def project():
    return render_template("projects/project.html")

@app_routes.route('/professor/home')
def home_professor():
    return render_template("home/home_professor.html")

@app_routes.route('/student/home')
def home_student():
    return render_template("home/home_student.html")

