from entitys.bdClasses.BdUsers import BdUser


class Subject:
    def __init__(self):
        self.bdUser = BdUser()
        self._observers = [student['email'] for student in self.bdUser.get_users() if student['title'] == 'student']

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()