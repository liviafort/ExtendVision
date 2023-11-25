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
    facadeProject = FacadeProject()
    projects = facadeProject.get_projects()
    return render_template("home/home_student.html", dados=projects)

@app_routes.route('/student/profile')
def profile_student():
    return render_template("account/profile_student.html")

@app_routes.route('/professor/profile')
def profile_professor():
    return render_template("account/profile_professor.html")

@app_routes.route('/projects/update/<int:id>', methods=['GET'])
def update_projects(id):
    facadeProject = FacadeProject()
    project = facadeProject.get_project_by_id(id)
    return render_template("projects/update.html", dados=project)

@app_routes.route('/professor/account/myProjects')
def my_projects():
    return render_template("projects/my_projects.html")

@app_routes.route('/student/account/myProjects')
def my_projects_student():
    return render_template("account/my_projects.html")