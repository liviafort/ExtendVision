from models.User import User


class Project:
    def __init__(self, title, area, theme, resume, teacher,  workload, vaga, remuneration, init, end, init_registration, end_registration):
        self.title = title
        self.area = area
        self.theme = theme
        self.resume = resume
        self.teacher = teacher
        self.workload = workload
        self.vaga = vaga
        self.remuneration = remuneration
        self.init = init
        self.end = end
        self.init_registration = init_registration
        self.end_registration = end_registration
        self.students = list()


