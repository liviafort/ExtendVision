from flask import Blueprint, render_template, jsonify, request, redirect
from entitys.BdClass.BdUsers import BdUser
from entitys.BdClass.BdProject import BdProject
from entitys.BdClass.BdProjectStudents import BdProjectStudents
from entitys.BdClass.BdField import BdField


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
    ProjectStudents = BdProjectStudents()
    Project = BdProject()
    Field = BdField()
    User = BdUser()

    project = Project.get_project_by_id(id)
    area = Field.get_field_by_id(project['id_field'])['field']
    project['field'] = area

    project['user'] = int(request.cookies.get('user'))

    projectStudents = ProjectStudents.get_ps_by_project(id)
    wait = [User.get_user_by_id(ps['id_user']) for ps in projectStudents if ps['status'] == "Espera"]
    accepted = [User.get_user_by_id(ps['id_user']) for ps in projectStudents if ps['status'] == "Deferido"]

    datas = {'project': project, 'users_wait': wait, 'users_accepted': accepted}

    return render_template("projects/project.html", dados=datas)


@app_routes.route('/student/project/<int:id>', methods=['GET'])
def project_student(id):
    Project = BdProject()
    Field = BdField()
    User = BdUser()

    project = Project.get_project_by_id(id)
    area = Field.get_field_by_id(project['id_field'])['field']
    project['field'] = area

    return render_template("projects/project_student.html", dados=project)


@app_routes.route('/professor/home')
def home_professor():
    Project = BdProject()
    projects = Project.get_projects()
    return render_template("home/home_professor.html", dados=projects)


@app_routes.route('/student/home')
def home_student():
    Project = BdProject()
    projects = Project.get_projects()
    return render_template("home/home_student.html", dados=projects)


@app_routes.route('/student/profile/<int:id>', methods=['GET'])
def profile_student(id):
    User = BdUser()
    user = User.get_user_by_id(id)
    return render_template("account/profile_student.html", dados=user)


@app_routes.route('/professor/profile/<int:id>', methods=['GET'])
def profile_professor(id):
    User = BdUser()
    user = User.get_user_by_id(id)
    return render_template("account/profile_professor.html", dados=user)


@app_routes.route('/projects/update/<int:id>', methods=['GET'])
def update_projects(id):
    Project = BdProject()
    project = Project.get_project_by_id(id)
    return render_template("projects/update.html", dados=project)


@app_routes.route('/professor/account/myProjects/<int:id>', methods=['GET'])
def my_projects(id):
    Project = BdProject()
    projects = Project.get_project_by_id_professor(id)
    return render_template("account/projects_professor.html", dados=projects)


@app_routes.route('/student/account/myProjects/<int:id>', methods=['GET'])
def my_projects_student(id):
    Project = BdProject()
    Field = BdField()
    ProjectStudents = BdProjectStudents()

    projectStudents = ProjectStudents.get_ps_by_user(id)

    projects = list()
    for projectstudent in projectStudents:
        if projectstudent['status'] == 'Deferido':
            project = Project.get_project_by_id(projectstudent['id_project'])
            project['field'] = Field.get_field_by_id(project['id_field'])['field']
            projects.append(project)
    print(projects)
    
    return render_template("account/my_projects.html", dados=projects)


@app_routes.route('/student/account/myRegistrations/<int:id>', methods=['GET'])
def my_registrations_student(id):
    Project = BdProject()
    Field = BdField()
    ProjectStudents = BdProjectStudents()

    projectStudents = ProjectStudents.get_ps_by_user(id)
    projects = list()
    for projectstudent in projectStudents:
        if projectstudent['status'] != 'Deferido':
            project = Project.get_project_by_id(projectstudent['id_project'])
            project['field'] = Field.get_field_by_id(project['id_field'])['field']
            project['status'] = projectstudent['status']
            projects.append(project)
    print(projects)

    return render_template("account/my_registrations.html", dados=projects)