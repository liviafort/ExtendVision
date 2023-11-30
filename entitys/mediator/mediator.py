import random
from entitys.bdClasses.BdRegister import BdRegister
from entitys.bdClasses.BdUsers import BdUser
from entitys.visitor.MediatorVisitor import MediatorVisitor


class Mediator:
    def __init__(self):
        print("Entrando no Mediador")
        self.data = None
        self.bdRegister = BdRegister()
        self.bdUser = BdUser()

    def get_data(self):
        return self.data

    def criarToken(self):
        caracteres = [str(random.randint(0, 9)) for i in range(10)]
        token = ''
        for c in caracteres:
            token = token + c
        return token


    def confirmaEmail(self, data):
        response = self.bdRegister.get_user_by_email(data['email'])

        if len(response) != 0:
            return False

        data['token'] = self.criarToken()
        self.data = data

        print("registro feito. Enviando email")
        visitor = MediatorVisitor()
        status = self.accept(visitor)

        if status:
            print("registrando dados")
            response = self.bdRegister.create_register(data)

            if response != None:
                return True
            return False
        return False


    def confirmaToken(self, token):
        print("Validando token")
        data = self.bdRegister.get_user_by_token(token)

        if len(data) != 0:
            print(data)
            del data['token']
            del data['id']

            try:
                response = self.bdUser.create_user(data)
                print(response)
                response = self.bdRegister.delete_register(token)
                return True
            except Exception as e:
                print(e)
                return False
            
        return False
    

    def accept(self, visitor):
        return visitor.visitarEmail(self)