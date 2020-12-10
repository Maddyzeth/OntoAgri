from Administrador import Administrador

class GestorAdministrador():

    def __init__(self):
        self._administrador = ''

    def set_agricultor(self, administrador):
        self._administrador = administrador

    def get_administrador(self):
        return self._administrador