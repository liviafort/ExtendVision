from flask import jsonify, redirect
import requests

class Login:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self.__situation = False

        self.__response = requests.get(f"http://127.0.0.1:5000/user/?user_email={self.__email}")


    def get_situation(self):
        return self.__situation

    def valida_login(self):
        """Verifica se o usuário e senha existem no banco de dados"""
        if self.__response.status_code == 200:
            print("Email válido")
            data = self.__response.json()

            if data["password"] == self.__password:
                print("Senha Válida")
                self.__situation = True
                return jsonify({"message":"Acesso permitido"}), True
            
            return jsonify({"error":"Senha invalida"}), False
        
        return jsonify({"error":"Email invalida"}), False
    
    def tipo_usuario(self):
        if self.__response.status_code == 200:
            data = self.__response.json()
            return jsonify({"message":"Email valido"}), data["title"] 

        return jsonify({"error":"Email invalida"}), "error"