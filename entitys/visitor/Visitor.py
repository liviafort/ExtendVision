import abc


class Visitor:
    @abc.abstractmethod
    def visitarEmail(self, data):
        pass