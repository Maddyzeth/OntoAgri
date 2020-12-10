from RecomendacionCultivos import Persona

class Administrador(Persona):
	def __init__(self, idPersona, nombrePersona, tipoIdentificacion, identificacion, numTelefono, email, idAdmin):
		Persona.__init__(self, idPersona, nombrePersona, tipoIdentificacion, identificacion, numTelefono, idAdmin)

	def set_idAdmin(self, idAdmin):
		self._idAdmin = idAdmin

	def get_idAdmin(self):
		return self._idAdmin