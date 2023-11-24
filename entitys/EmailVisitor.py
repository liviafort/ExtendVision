from entitys.Visitor import Visitor
from flask_mail import Message
from flask import current_app
import requests


class EmailVisitor(Visitor):
    def create_message(self, instance):
        data = instance.get_data()
        response = requests.get(f"http://127.0.0.1:5000/user/?user_id={data['id_professor']}")
        professor = response.json()['name']

        response = requests.get(f"http://127.0.0.1:5000/field/?field_id={data['id_field']}")
        area = response.json()['field']

        response = requests.get(f"http://127.0.0.1:5000/user/")
        students = [student['email'] for student in response.json() if student['title'] == 'student']

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

