class Robot:

	padre = 0
	madre = 0
	generacion = 0
	cromosomas = "000000"
	motor = 0
	bateria = 0
	camara = 0

	def __init__(self, generacion, cromosomas, padre, madre):
		self.generacion = generacion
		self.cromosomas = cromosomas
		self.padre = padre
		self.madre = madre
		
