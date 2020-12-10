class Cultivo(object):
	def __init__(self, idCultivo, nombreCultivo):
		self._idCultivo = idCultivo
		self._nombreCultivo = nombreCultivo

	def set_idCultivo(self, idCultivo):
		self._idCultivo = idCultivo

	def get_idCultivo(self):
		return self._idCultivo


	def set_nombreCultivo(self, nombreCultivo):
		self._nombreCultivo = nombreCultivo

	def get_nombreCultivo(self):
		return self._nombreCultivo