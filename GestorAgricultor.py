from Agricultor import Agricultor

class GestorAgricultor():

    def __init__(self):
        self._agricultor = ''

    def set_agricultor(self, agricultor):
        self._agricultor = agricultor

    def get_agricultor(self):
        return self._agricultor