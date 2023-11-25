from flask import jsonify
from entitys.visitor.RegisterVisitor import Registerisitor
from entitys.facade.FacadeUsers import FacadeUser
from entitys.facade.FacadeField import FacadeField
from entitys.facade.FacadeProject import FacadeProject
from entitys.facade.FacadeProjectStudents import FacadeProjectStudents
from datetime import datetime
import json
import hashlib


class Register:
    def __init__(self, data):
        self.data = data
        self.facadeUser = FacadeUser()
        self.facadeField = FacadeField()
        self.facadeProject = FacadeProject()
        self.facadeProjectStudent = FacadeProjectStudents()
        print("ENTROU NA CLASSE")

    def responseEmail(self):
        try:
            data = self.facadeUser.get_user_by_email(self.data['email'])
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def responsePostUser(self):
        try:
            data = self.facadeUser.create_user(self.data)
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def responseArea(self):
        try:
            data = self.facadeField.get_field_by_name(self.data['area'])
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def responsePostProject(self):
        try:
            data = self.facadeProject.create_project(self.data)
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def responseProjectStudent(self):
        try:
            data = self.facadeProjectStudent.create_project_student(self.data)
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def responseUpdateProjectStudent(self):
        try:
            id_project = self.data['id_project']
            id_user = self.data['id_user']
            data = self.facadeProjectStudent.update_project_students(id_project, id_user, self.data)
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def get_data(self):
        return self.data

    def student_or_professor(self):
        local_part, domain = self.data['email'].split("@")
        self.data['title'] = 'student' if domain == 'academico.ifpb.edu.br' else 'teacher'

    def hashing_password(self):
        try:
            hash_object = hashlib.new("SHA256")
            data = self.data['password']
            hash_object.update(data.encode('utf-8'))
            self.data['password'] = hash_object.hexdigest()
        except Exception as e:
            print(e)

    def valida_email(self):
        """Verifica se é um email acadêmico do IFPB"""
        local_part, domain = self.data['email'].split("@")
        print("VALIDA O EMAIL")
        print(local_part, domain)
        if domain == 'academico.ifpb.edu.br' or domain == 'ifpb.edu.br':
            return True
        return False

    def validate_birth(self):
        date_birth = datetime.strptime(self.data['birth'], "%Y-%m-%d").date()
        current_date = datetime.now().date()

        if date_birth < current_date:
            age = current_date.year - date_birth.year
            print(age)
            if int(age) >= 13:
                return True
            
            return False
        return False

    def registrar(self):
        """Realiza o cadastro do usuário no banco de dados"""

        if not(self.valida_email()):
            return jsonify({"error": "Email acadêmico não detectado"}), False
        print("EMAIL È DO IFPB")
        
        response = self.responseEmail()
        if response['status'] == 200:
            return jsonify({"error":"Email já cadastrado"}), False
        print("EMAIL NÃO EXISTE NO BD")

        self.student_or_professor()
        self.hashing_password()

        if not(self.validate_birth()):
            return jsonify({"error":"Data de nascimento inválida"}), False
        print("DATA DE NASCIMENTO VÁLIDA")

        try:
            print("CRIANDO DADOS PARA INSERIR NO BANCO")
            response = self.responsePostUser()
            print("RESPONSE DO BD")
            # print(response)

            if response['status'] == 200:
                 print("USUÁRIO CRIADO")
                 return response['json'], True
            
            return response['json'], False

        except Exception as e:
            print(e)

    def registrar_projeto(self):
        """Realiza o cadastro de um projeto no banco de dados"""

        response = self.responseEmail()
        data = response['json']
        self.data['id_professor'] = data['id']

        response = self.responseArea()
        data = response['json']
        self.data['id_field'] = data['id']
        
        del self.data['email']
        del self.data['area']
        
        try:
            response = self.responsePostProject()
            print("RESPONSE DO BD")
            print(response)

            if response['status'] == 200:
                print("LINHA CRIADA")
                visitor = Registerisitor()

                # thread = threading.Thread(target=self.accept, args=(visitor,))
                # thread.start()
                self.accept(visitor)

                return response['json'], True
            return response['json'], False

        except Exception as e:
            print(e)

    def registrar_projeto_estudante(self):
        self.data['status'] = 'Espera'
        response = self.responseProjectStudent()
        if response['status'] == 200:
            print("LINHA CRIADA")
            return response['json'], True
        return response['json'], False

    def aceitar_solitacao(self):
        self.data['status'] = 'Deferido'
        response = self.responseUpdateProjectStudent()
        if response['status'] == 200:
            print("LINHA CRIADA")
            return response['json'], True
        return response['json'], False

    def recusar_solitacao(self):
        self.data['status'] = 'Indeferido'
        response = self.responseUpdateProjectStudent()
        if response['status'] == 200:
            print("LINHA CRIADA")
            return response['json'], True
        return response['json'], False

    def accept(self, visitor):
        visitor.visitarEmail(self)