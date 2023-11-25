from flask import Blueprint, render_template, jsonify, request, redirect
from entitys.facade.FacadeProject import FacadeProject

app_routes = Blueprint('app_routes', __name__)

#Rotas para as páginas principais da aplicação

@app_routes.route('/')
def login():
    return render_template("users/signin.html")


@app_routes.route('/register')
def register():
    return render_template("users/signup.html")


@app_routes.route('/projects/register')
def register_project():
    return render_template("projects/register.html")


@app_routes.route('/projects/project/<int:id>', methods=['GET'])
def project(id):
    facadeProject = FacadeProject()
    project = facadeProject.get_project_by_id(id)
    return render_template("projects/project.html", dados=project)


@app_routes.route('/professor/home')
def home_professor():
    facadeProject = FacadeProject()
    projects = facadeProject.get_projects()
    return render_template("home/home_professor.html", dados=projects)


@app_routes.route('/student/home')
def home_student():
    return render_template("home/home_student.html")

@app_routes.route('/student/account/profile')
def profile():
    return render_template("account/profile.html")
