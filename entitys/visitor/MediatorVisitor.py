from entitys.visitor.Visitor import Visitor
from flask_mail import Message
from flask import current_app

class MediatorVisitor(Visitor):
    def __init__(self):
        pass

    def create_message(self, instance):
        data = instance.get_data()
        student = [data["email"] for e in range(len(data['email']))]
        name = data['name']
        token = data['token'] 

        msg = Message('ExtendVision: Validação de Email', recipients=student)
        msg.body = f"""
        Olá {name}, 
        confirme seu email clicando no link abaixo:
        http://127.0.0.1:5000/confirmEmail/{token}
        
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
            return True
        except Exception as e:
            print('erro email: ', str(e))
            return False
