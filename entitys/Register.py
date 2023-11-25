from flask import jsonify
from entitys.EmailVisitor import EmailVisitor
from datetime import datetime
import requests
import json
import hashlib
import threading


class Register:
    def __init__(self, data):
        self.__data = data
        print("ENTROU NA CLASSE")


    def get_data(self):
        return self.__data


    def student_or_professor(self):
        local_part, domain = self.__data['email'].split("@")
        self.__data['title'] = 'student' if domain == 'academico.ifpb.edu.br' else 'teacher'


    def hashing_password(self):
        try:
            hash_object = hashlib.new("SHA256")
            data = self.__data['password'] 
            hash_object.update(data.encode('utf-8'))
            self.__data['password'] = hash_object.hexdigest()
        except Exception as e:
            print(e)


    def valida_email(self):
        """Verifica se é um email acadêmico do IFPB"""
        local_part, domain = self.__data['email'].split("@")
        print("VALIDA O EMAIL")
        print(local_part, domain)
        if domain == 'academico.ifpb.edu.br' or domain == 'ifpb.edu.br':
            return True
        return False
    

    def validate_birth(self):
        date_birth = datetime.strptime(self.__data['birth'], "%Y-%m-%d").date()
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
        
        response = requests.get(f"http://127.0.0.1:5000/user/?user_email={self.__data['email']}")
        if response.status_code == 200:
            return jsonify({"error":"Email já cadastrado"}), False
        print("EMAIL NÃO EXISTE NO BD")

        self.student_or_professor()
        self.hashing_password()

        if not(self.validate_birth()):
            return jsonify({"error":"Data de nascimento inválida"}), False
        print("DATA DE NASCIMENTO VÁLIDA")

        try:
            dados = json.dumps(self.__data)
            print("CRIANDO DADOS PARA INSERIR NO BANCO")
            
            headers = {'Content-Type': 'application/json'}

            response = requests.post("http://127.0.0.1:5000/user/", data=dados, headers=headers)
            print("RESPONSE DO BD")
            # print(response)

            if response.status_code == 200:
                 print("USUÁRIO CRIADO")
                 return response.json(), True
            
            return response.json(), False 

        except Exception as e:
            print(e)


    def registrar_projeto(self):
        """Realiza o cadastro de um projeto no banco de dados"""

        response = requests.get(f"http://127.0.0.1:5000/user/?user_email={self.__data['email']}")
        data = response.json()
        self.__data['id_professor'] = data['id']

        response = requests.get(f"http://127.0.0.1:5000/field/?field_name={self.__data['area']}")
        data = response.json()
        self.__data['id_field'] = data['id']
        
        del self.__data['email']
        del self.__data['area']
        
        try:
            dados = json.dumps(self.__data)
            print("CRIANDO DADOS PARA INSERIR NO BANCO")
            print(dados)

            headers = {'Content-Type': 'application/json'}

            response = requests.post("http://127.0.0.1:5000/project/", data=dados, headers=headers)
            print("RESPONSE DO BD")
            print(response)

            if response.status_code == 200:
                print("LINHA CRIADA")
                visitor = EmailVisitor()

                thread = threading.Thread(target=self.accept, args=(visitor,))
                thread.start()

                return response.json(), True
            return response.json(), False

        except Exception as e:
            print(e)


    def accept(self, visitor):
        visitor.visitarEmail(self)