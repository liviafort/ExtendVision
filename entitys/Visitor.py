import abc


class Visitor:
    def __init__(self):
        pass

    @abc.abstractmethod
    def visitarEmail(self, data):
        pass