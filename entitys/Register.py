from flask import jsonify, redirect
import requests
import json

class Register:
    def __init__(self, data):
        self.__data = data
        print("ENTROU NA CLASSE")

    def student_or_professor(self):
        _, domain = self.__data['email'].split("@")
        self.__data['title'] = 'student' if domain == 'academico.ifpb.edu.br' else 'teacher'

    def valida_email(self):
        """Verifica se é um email acadêmico do IFPB"""
        local_part, domain = self.__data['email'].split("@")
        print("VALIDA O EMAIL")
        print(local_part, domain)
        if domain == 'academico.ifpb.edu.br' or domain == 'ifpb.edu.br':
            return True
        return False

    def registrar(self):
        if not(self.valida_email()):
            return jsonify({"error": "Email acadêmico não detectado"}), False
        print("EMAIL È DO IFPB")
        
        response = requests.get(f"http://127.0.0.1:5000/user/?user_email={self.__data['email']}")
        if response.status_code == 200:
            return jsonify({"error":"Email já cadastrado"}), False
        print("EMAIL NÂO EXISTE NO BD")
        self.student_or_professor()

        try:
            dados = json.dumps(self.__data)
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

    def registrar_projeto(self):
        response = requests.get(f"http://127.0.0.1:5000/user/?user_email={self.__data['email']}")
        data = response.json()
        self.__data['id_professor'] = data['id']

        response = requests.get(f"http://127.0.0.1:5000/field/?field_name={self.__data['area']}")
        data = response.json()
        self.__data['id_field'] = data['id']

        try:
            dados = json.dumps(self.__data)
            print("CRIANDO DADOS PARA INSERIR NO BANCO")
            print(dados)

            headers = {'Content-Type': 'application/json'}

            response = requests.post("http://127.0.0.1:5000/field/", data=dados, headers=headers)
            print("RESPONSE DO BD")
            print(response)

            if response.status_code == 200:
                print("LINHA CRIADA")
                return response.json(), True

            return response.json(), False

        except Exception as e:
            print(e)

