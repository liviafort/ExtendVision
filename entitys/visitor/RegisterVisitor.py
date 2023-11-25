from entitys.visitor.Visitor import Visitor
from flask_mail import Message
from flask import current_app

from entitys.facade.FacadeUsers import FacadeUser
from entitys.facade.FacadeField import FacadeField


class Registerisitor(Visitor):
    def __init__(self):
        self.facadeUser = FacadeUser()
        self.facadeField = FacadeField()

    def responseUser(self, data):
        try:
            data = self.facadeUser.get_user_by_id(data['id_professor'])
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def responseUsers(self):
        try:
            data = self.facadeUser.get_users()
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def responseArea(self, data):
        try:
            data = self.facadeField.get_field_by_id(data['id_field'])
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def create_message(self, instance):
        data = instance.get_data()
        response = self.responseUser(data)
        professor = response['json']['name']

        response = self.responseArea(data)
        area = response['json']['field']

        response = self.responseUsers()
        students = [student['email'] for student in response['json'] if student['title'] == 'student']

        msg = Message(f'ExtendVision: Novo projeto adicionado - {data["theme"]}', recipients=students)
        msg.body = f"""
        O(a) professor(a) {professor} adicionou um novo projeto.
        
        Title: {data['title']}
        Area Temática: {area}
        Data início das incrições: {data['begin_date']}
        Data fim das incrições: {data['end_date']}
        
        att,
        Equipe ExtendVision
        """

        return msg

    def visitarEmail(self, data):
        msg = self.create_message(data)
        try:
            print('carregando')
            current_app.config['mail'].send(msg)
            print('E-mail enviado com sucesso!')
        except Exception as e:
            print('erro email: ', str(e))

