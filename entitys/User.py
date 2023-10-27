
class User:
    def __init__(self, name, registration, password, titration, gender, birth):
        self.name = name
        self.registration = registration
        self.password = password
        self.titration = titration
        self.gender = gender
        self.birth = birth

    def get_name(self):
        return self.name

    def get_registration(self):
        return self.registration

    def get_password(self):
        return self.password

    def get_titration(self):
        return self.titration

    def get_gender(self):
        return self.gender

    def get_birth(self):
        return self.birth

    def set_name(self, name):
        self.name = name

    def set_registration(self, registration):
        self.registration = registration

    def set_password(self, password):
        self.password = password

    def set_titration(self, titration):
        self.titration = titration

    def set_gender(self, gender):
        self.gender = gender

    def set_birth(self, birth):
        self.birth = birth
