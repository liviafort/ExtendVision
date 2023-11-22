from flask import jsonify, redirect
import requests
import json

class Register:
    def __init__(self, name, email, password, gender, registration, birth, title):
        print("ENTROU NA CLASSE")
        self.__name = name
        self.__email = email
        self.__password = password
        self.__gender = gender
        self.__registration = registration
        self.__title = title
        self.__birth = birth
        print(self.__title)

    def valida_email(self):
        """Verifica se é um email acadêmico do IFPB"""
        local_part, domain = self.__email.split("@")
        print("VALIDA O EMAIL")
        print(local_part, domain)
        if domain == "academico.ifpb.edu.br":
            return True
        return False

    def registrar(self):
        if not(self.valida_email()):
            return jsonify({"error":"Email acadêmico não detectado"}), False
        print("EMAIL È DO IFPB")
        
        response = requests.get(f"http://127.0.0.1:5000/user/?user_email={self.__email}")
        if response.status_code == 200:
            return jsonify({"error":"Email já cadastrado"}), False
        print("EMAIL NÂO EXISTE NO BD")

        try:
            dados = {
                        "registration":self.__registration,
                        "password":self.__password,
                        "name":self.__name,
                        "title":self.__title,
                        "gender":self.__gender,
                        "birth":self.__birth,
                        "email":self.__email
                    }
            
            dados = json.dumps(dados)
            print("CRIANDO DADOS PARA INSERIR NO BANCO")
            print(dados)
            
            headers = {'Content-Type': 'application/json'}

            response = requests.post("http://127.0.0.1:5000/user/", data=dados, headers=headers)
            print("RESPONSE DO BD")
            print(response)

            if response.status_code == 200:
                 print("LINHA CRIADA")
                 return response.json(), True
            
            return response.json(), False

        except Exception as e:
            print(e)
