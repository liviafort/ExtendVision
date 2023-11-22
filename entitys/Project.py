from entitys.User import User

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


    def get_title(self):
        return self.title

    def get_area(self):
        return self.area

    def get_theme(self):
        return self.theme

    def get_resume(self):
        return self.resume

    def get_teacher(self):
        return self.teacher

    def get_workload(self):
        return self.workload

    def get_vaga(self):
        return self.vaga

    def get_remuneration(self):
        return self.remuneration

    def get_init(self):
        return self.init

    def get_end(self):
        return self.end

    def get_init_registration(self):
        return self.init_registration

    def get_end_registration(self):
        return self.end_registration

    def set_title(self, title):
        self.title = title

    def set_area(self, area):
        self.area = area

    def set_theme(self, theme):
        self.theme = theme

    def set_resume(self, resume):
        self.resume = resume

    def set_teacher(self, teacher):
        self.teacher = teacher

    def set_workload(self, workload):
        self.workload = workload

    def set_vaga(self, vaga):
        self.vaga = vaga

    def set_remuneration(self, remuneration):
        self.remuneration = remuneration

    def set_init(self, init):
        self.init = init

    def set_end(self, end):
        self.end = end

    def set_init_registration(self, init_registration):
        self.init_registration = init_registration

    def set_end_registration(self, end_registration):
        self.end_registration = end_registration

