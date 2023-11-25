from flask import jsonify, redirect
from entitys.facade.FacadeUsers import FacadeUser
import hashlib


class Login:
    def __init__(self, data):
        self.data = data
        self.facadeUser = FacadeUser()
        self.response = self.responseEmail()

    def responseEmail(self):
        try:
            data = self.facadeUser.get_user_by_email(self.data['email'])
            return {'json': data, 'status': 200}
        except:
            return {'json': {}, 'status': 404}

    def test_hashing_password(self):
        hash_object = hashlib.new("SHA256")
        data = self.data['password']
        hash_object.update(data.encode('utf-8'))
        self.data['password'] = hash_object.hexdigest()

    def valida_login(self):
        """Verifica se o usuário e senha existem no banco de dados"""
        if self.response['status'] == 200:
            print("Email válido")

            data = self.response['json']
            self.test_hashing_password()

            if data["password"] == self.data['password']:
                print("Senha Válida")
                return jsonify({"message": "Acesso permitido"}), True
            
            return jsonify({"error": "Senha invalida"}), False
        
        return jsonify({"error": "Email invalida"}), False
    
    def tipo_usuario(self):
        if self.response['status'] == 200:
            data = self.response['json']
            return jsonify({"message": "Email valido"}), data["title"]

        return jsonify({"error": "Email invalida"}), "error"