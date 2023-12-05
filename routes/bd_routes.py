from flask import Blueprint, render_template, jsonify, request, redirect
from entitys.bdClasses.BdField import BdField
from entitys.bdClasses.BdUsers import BdUser
from entitys.bdClasses.BdProject import BdProject
from entitys.bdClasses.BdProjectStudents import BdProjectStudents


bdUser = BdUser()
bdField = BdField()
bdProject = BdProject()
bdProjectStudents = BdProjectStudents()


#Rotas para banco de dados
app_bd = Blueprint('app_bd', __name__)

#CRUD USER
@app_bd.route('/user/', methods=['GET'])
def get_user():
    user_id = request.args.get("user_id")
    user_email = request.args.get("user_email")

    if user_id:
        try:
            return bdUser.get_user_by_id(user_id)
        except:
            return jsonify({'error':'ID nao encontrado'}), 404

    elif user_email:
        try:
            return bdUser.get_user_by_email(user_email)
        except:
            return jsonify({'error':'Email nao encontrado'}), 404
        
    return bdUser.get_users()


@app_bd.route('/user/', methods=['POST'])
def create_user_route():
    data = request.json
    required_fields = ['registration', 'password', 'name', 'title', 'gender', 'birth', 'email']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_user_id = bdUser.create_user(data)

    return jsonify({'message': 'Novo usuário criado com sucesso', 'user_id': new_user_id})


@app_bd.route('/user/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.json
    required_fields = ['registration', 'password', 'name', 'title', 'gender', 'birth', 'email']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_user_id = bdUser.update_user(user_id, data)

    return jsonify({'message': 'Usuário atualizado com sucesso', 'user_id': new_user_id})


@app_bd.route('/user/<int:user_id>', methods=['DELETE'])
def delete_users(user_id):
    user_del = bdUser.delete_user(user_id)
    return jsonify({'message': 'Usuário Deletado', 'user': user_del})


#CRUD PROJET
@app_bd.route('/project/', methods=['GET'])
def get_project():
    return bdProject.get_projects()


@app_bd.route('/project/<int:project_id>', methods=['GET'])
def get_proje_by_id(project_id):
    return bdProject.get_project_by_id(project_id)


@app_bd.route('/project/', methods=['POST'])
def create_project_route():
    data = request.json
    required_fields = ['id_professor','id_field','title','theme','description','begin_date','end_date','register_begin','register_end','workload','available_spots','scholarship']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_project_id = (bdProject.create_project(data))["json"]

    return jsonify({'message': 'Novo Projeto criado com sucesso', 'Project_id': new_project_id})


@app_bd.route('/project/<int:project_id>', methods=['PUT'])
def update_project_route(project_id):
    data = request.json
    required_fields = ['id_professor','id_field','title','theme','description','begin_date','end_date','register_begin','register_end','workload','available_spots','scholarship']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_project_id = bdProject.update_project(project_id, data)

    return jsonify({'message': 'Projeto atualizado com sucesso', 'project_id': new_project_id})


@app_bd.route('/project/<int:project_id>', methods=['DELETE'])
def delete_project_route(project_id):
    project_del = bdProject.delete_project(project_id)
    return jsonify({'message': 'Projeto Deletado', 'Project': project_del})


#CRUD FIELDS
@app_bd.route('/field/', methods=['GET'])
def get_field_by_id_route():
    field_id = request.args.get('field_id')
    field_name = request.args.get('field_name')

    if field_id:
        return (bdField.get_field_by_id(field_id))["json"]
    
    elif field_name:
        return (bdField.get_field_by_name(field_name))["json"]
    
    return bdField.get_fields()


@app_bd.route('/field/', methods=['POST'])
def create_field_route():
    data = request.json
    required_fields = ['field']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_field_id = bdField.create_field(data)

    return jsonify({'message': 'Novo Campo adicionado com sucesso', 'Field_id': new_field_id})


@app_bd.route('/field/<int:field_id>', methods=['PUT'])
def update_field_route(field_id):
    data = request.json
    required_fields = ['field']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_field_id = bdField.update_field(field_id, data)

    return jsonify({'message': 'Campo atualizado com sucesso', 'Field_id': new_field_id})


@app_bd.route('/field/<int:field_id>', methods=['DELETE'])
def delete_field_route(field_id):
    field_del = bdField.delete_field(field_id)
    return jsonify({'message': 'Campo Deletado', 'Campo': field_del})


#CRUD PROJECT STUDENTS
@app_bd.route('/project_students/', methods=['GET'])
def get_project_students_route():

    user_id = request.args.get('user_id')
    project_id = request.args.get('project_id')
    user_accepted = request.args.get('user_accepted')

    if user_id: 
        #exemplode url: http://127.0.0.1:5000/project_students?user_id=25
        return (bdProjectStudents.get_ps_by_user(user_id))["json"]
    
    elif project_id:
        if user_accepted == "True":
            projectStudents = bdProjectStudents.get_ps_by_project(project_id)
            studets = [(bdUser.get_user_by_id(ps['id_user']))["json"] for ps in projectStudents if ps['status'] == "Deferido"]
            return studets
        
        elif user_accepted == "False":
            projectStudents = bdProjectStudents.get_ps_by_project(project_id)
            studets = [(bdUser.get_user_by_id(ps['id_user']))["json"] for ps in projectStudents if ps['status'] == "Espera"]
            return studets
    
        else:
            projectStudents = bdProjectStudents.get_ps_by_project(project_id)
            studets = [(bdUser.get_user_by_id(ps['id_user']))["json"] for ps in projectStudents]
            return studets
            
    else:
        return bdProjectStudents.get_project_students()


@app_bd.route('/project_students/', methods=['POST'])
def create_project_students_route():
    data = request.json
    required_fields = ['id_project', 'id_user']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_project_students_id = (bdProjectStudents.create_project_student(data))["json"]

    return jsonify({'message': 'Novo relação Projeto-Estudante criada', 'Project_id': new_project_students_id[0], 'User_id': new_project_students_id[1]})


@app_bd.route('/project_students/', methods=['PUT'])
def update_project_students_route():
    user_id = request.args.get('user_id')
    project_id = request.args.get('project_id')
    data = request.json

    if user_id and project_id:
        required_fields = ['id_project', 'id_user']

        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
        
        new_project_students_id = (bdProjectStudents.update_project_students(project_id, user_id, data))["json"]

        return jsonify({'message': 'Relação Projeto-Estudante Atualizada', 'Project_id': new_project_students_id[0], 'User_id': new_project_students_id[1]})
    
    return jsonify({'error': 'IDs não especificados'}), 400


@app_bd.route('/project_students/', methods=['DELETE'])
def delete_project_student_route():
    user_id = request.args.get('user_id')
    project_id = request.args.get('project_id')

    if user_id and project_id:
        ps_del = bdProjectStudents.delete_project_students(project_id, user_id)
        return jsonify({'message': 'Relação Projeto Estudante Deletada', 'ProjectStudent:': ps_del})
    
    return jsonify({'error': 'IDs não especificados'}), 400