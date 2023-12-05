from flask import Blueprint, render_template, jsonify, request, redirect
from entitys.bdClasses.BdUsers import BdUser
from entitys.bdClasses.BdProject import BdProject
from entitys.bdClasses.BdProjectStudents import BdProjectStudents
from entitys.bdClasses.BdField import BdField
from entitys.mediator.mediator import Mediator

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
    bdProjectStudents = BdProjectStudents()
    bdProject = BdProject()
    bdField = BdField()
    bdUser = BdUser()

    project = bdProject.get_project_by_id(id)
    area = (bdField.get_field_by_id(project['id_field']))["json"]['field']
    project['field'] = area

    project['user'] = int(request.cookies.get('user'))

    projectStudents = bdProjectStudents.get_ps_by_project(id)
    wait = [(bdUser.get_user_by_id(ps['id_user'])["json"]) for ps in projectStudents if ps['status'] == "Espera"]
    accepted = [(bdUser.get_user_by_id(ps['id_user']))["json"] for ps in projectStudents if ps['status'] == "Deferido"]

    datas = {'project': project, 'users_wait': wait, 'users_accepted': accepted}

    return render_template("projects/project.html", dados=datas)


@app_routes.route('/student/project/<int:id>', methods=['GET'])
def project_student(id):
    bdProject = BdProject()
    bdField = BdField()

    project = bdProject.get_project_by_id(id)
    area = (bdField.get_field_by_id(project['id_field']))["json"]['field']
    project['field'] = area

    return render_template("projects/project_student.html", dados=project)


@app_routes.route('/professor/home')
def home_professor():
    bdProject = BdProject()
    projects = bdProject.get_projects()
    return render_template("home/home_professor.html", dados=projects)


@app_routes.route('/student/home')
def home_student():
    bdProject = BdProject()
    projects = bdProject.get_projects()
    return render_template("home/home_student.html", dados=projects)


@app_routes.route('/student/profile/<int:id>', methods=['GET'])
def profile_student(id):
    bdUser = BdUser()
    user = bdUser.get_user_by_id(id)
    return render_template("account/profile_student.html", dados=user["json"])


@app_routes.route('/professor/profile/<int:id>', methods=['GET'])
def profile_professor(id):
    bdUser = BdUser()
    user = bdUser.get_user_by_id(id)
    return render_template("account/profile_professor.html", dados=user["json"])


@app_routes.route('/projects/update/<int:id>', methods=['GET'])
def update_projects(id):
    bdProject = BdProject()
    project = bdProject.get_project_by_id(id)
    return render_template("projects/update.html", dados=project)


@app_routes.route('/professor/account/myProjects/<int:id>', methods=['GET'])
def my_projects(id):
    bdProject = BdProject()
    bdField = BdField()
    projects = bdProject.get_project_by_id_professor(id)
    projects_field = list()
    for i, project in enumerate(projects):
        project['field'] = (bdField.get_field_by_id(project['id_field']))["json"]['field']
        projects_field.append(project)
    return render_template("account/projects_professor.html", dados=projects_field)


@app_routes.route('/student/account/myProjects/<int:id>', methods=['GET'])
def my_projects_student(id):
    bdProject = BdProject()
    bdField = BdField()
    bdProjectStudents = BdProjectStudents()

    projectStudents = bdProjectStudents.get_ps_by_user(id)

    projects = list()
    for projectstudent in projectStudents:
        if projectstudent['status'] == 'Deferido':
            project = bdProject.get_project_by_id(projectstudent['id_project'])
            project['field'] = (bdField.get_field_by_id(project['id_field']))["json"]['field']
            projects.append(project)
    print(projects)
    
    return render_template("account/my_projects.html", dados=projects)


@app_routes.route('/student/account/myRegistrations/<int:id>', methods=['GET'])
def my_registrations_student(id):
    bdProject = BdProject()
    bdField = BdField()
    bdProjectStudents = BdProjectStudents()

    projectStudents = bdProjectStudents.get_ps_by_user(id)
    projects = list()
    for projectstudent in projectStudents:
        if projectstudent['status'] != 'Deferido':
            project = bdProject.get_project_by_id(projectstudent['id_project'])
            project['field'] = (bdField.get_field_by_id(project['id_field']))["json"]['field']
            project['status'] = projectstudent['status']
            projects.append(project)
    print(projects)

    return render_template("account/my_registrations.html", dados=projects)


@app_routes.route('/confirmEmail/<int:token>', methods=['GET'])
def confirmEmail(token):
    status = Mediator().confirmaToken(token)
    if status:
        return render_template("users/confirmEmail.html")
    return redirect("/")