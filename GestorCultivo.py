from Cultivo import Cultivo

class GestorCultivo():
    def __init__(self):
        self._cultivo = ''

    def set_cultivo(self, cultivo):
        self._cultivo = cultivo

    def get_cultivo(self):
        return self._cultivo

