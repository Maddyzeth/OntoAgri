from RecomendacionCultivos import Persona

class Agricultor(Persona):
	def __init__(self, idPersona, nombrePersona, tipoIdentificacion, identificacion, numTelefono, email, Finca):
		Persona.__init__(self, idPersona, nombrePersona, tipoIdentificacion, identificacion, numTelefono, email)
		self.Finca = Finca

	def set_Finca(self, Finca):
		self._Finca = Finca

	def get_Finca(self):
		return self._Finca
