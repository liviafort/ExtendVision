from flask import jsonify, redirect
import requests
import hashlib

class Login:
    def __init__(self, data):
        self.__data = data
        self.__response = requests.get(f"http://127.0.0.1:5000/user/?user_email={self.__data['email']}")

    def test_hashing_password(self):
        hash_object = hashlib.new("SHA256")
        data = self.__data['password'] 
        hash_object.update(data.encode('utf-8'))
        self.__data['password'] = hash_object.hexdigest()

    def valida_login(self):
        """Verifica se o usuário e senha existem no banco de dados"""
        if self.__response.status_code == 200:
            print("Email válido")

            data = self.__response.json()
            self.test_hashing_password()

            if data["password"] == self.__data['password']:
                print("Senha Válida")
                return jsonify({"message": "Acesso permitido"}), True
            
            return jsonify({"error": "Senha invalida"}), False
        
        return jsonify({"error": "Email invalida"}), False
    
    def tipo_usuario(self):
        if self.__response.status_code == 200:
            data = self.__response.json()
            return jsonify({"message":" Email valido"}), data["title"]

        return jsonify({"error": "Email invalida"}), "error"