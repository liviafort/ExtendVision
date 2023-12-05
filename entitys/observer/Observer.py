

class Observer:
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print("Os dados do banco de dados foram atualizados!")
