class Finca(object):
	def __init__(self, idFinca, nombreFinca, topografia, temperaturaProm, altura, luminosidadProm, humedadProm, suelo, acidez, Ubicacion):
		self._idFinca = idFinca
		self._nombreFinca = nombreFinca
		self._topografia = topografia
		self._temperaturaProm = temperaturaProm
		self._altura = altura
		self._luminosidadProm = luminosidadProm
		self._humedadProm = humedadProm
		self._suelo = suelo
		self._acidez = acidez
		self._Ubicacion = Ubicacion


	def set_idFinca(self, idFinca):
		self._idFinca = idFinca

	def get_idFinca(self):
		return self._idFinca


	def set_nombreFinca(self, nombreFinca):
		self._nombreFinca = nombreFinca

	def get_nombreFinca(self):
		return self._nombreFinca


	def set_topografia(self, topografia):
		self._topografia = topografia

	def get_topografia(self):
		return self._topografia


	def set_temperaturaProm(self, temperaturaProm):
		self._temperaturaProm = temperaturaProm

	def get_temperaturaProm(self):
		return self._temperaturaProm


	def set_altura(self, altura):
		self._altura = altura

	def get_altura(self):
		return self._altura


	def set_luminosidadProm(self, luminosidadProm):
		self._luminosidadProm = luminosidadProm

	def get_luminosidadProm(self):
		return self._luminosidadProm


	def set_humedadProm(self, humedadProm):
		self._humedadProm = humedadProm

	def get_humedadProm(self):
		return self._humedadProm


	def set_suelo(self, suelo):
		self._suelo = suelo

	def get_suelo(self):
		return self._suelo


	def set_acidez(self, acidez):
		self._acidez = acidez

	def get_acidez(self):
		return self._acidez


	def set_Ubicacion(self, Ubicacion):
		self._Ubicacion = Ubicacion

	def get_Ubicacion(self):
		return self._Ubicacion