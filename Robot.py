import random as r

class Robot:

	padre = 0
	madre = 0
	generacion = 0
	cromosomas = "000000"
	motor = 1
	bateria = 1
	camara = 1
	nivBateria = 1
	x = 20
	y = 1


	def __init__(self, generacion, cromosomas, padre, madre):
		self.generacion = generacion
		self.cromosomas = cromosomas
		self.padre = padre
		self.madre = madre

		self.motor = self.toInt(cromosomas[0:2])
		self.bateria = self.toInt(cromosomas[2:4])
		self.camara = self.toInt(cromosomas[4:6])

		self.nivBateria = self.bateria*1000


	def setCord(self, i, j):
		self.x += i
		self.y += j

	#Marcov
	def seleccion(self, matriz):

		if(matriz[self.x][self.y] == 1 and self.motor < 3):
			return False

		if(matriz[self.x][self.y] == 2 and self.motor == 1):
			return False

		arriba = self.calcUp(matriz)
		derecha = self.calcRight(matriz)
		abajo = self.calcDown(matriz)
		izquierda = self.calcLeft(matriz)

		#print(arriba, derecha, abajo, izquierda)

		prom = (arriba + derecha + abajo + izquierda)/4


		if(arriba != 0):
			arriba = (arriba/prom/4)*100

		if(derecha != 0):
			derecha = (derecha/prom/4)*100

		if(abajo != 0):
			abajo = (abajo/prom/4)*100

		if(izquierda != 0):
			izquierda = (izquierda/prom/4)*100


		#print(arriba, derecha, abajo, izquierda)
		self.calcGastos(matriz)


		self.mover(arriba, derecha, abajo, izquierda)
		

		print(self.nivBateria, self.x, self.y)

		

		return True


	def mover(self, a, b, c, d):
		valor = r.uniform(0, 100)

		if(valor < a):						#Arriba
			direccion = 0
			self.setCord(-1, 0)

		elif(valor >= a and valor < a+b):	#Derecha
			direccion = 1
			self.setCord(0, 1)
		
		elif(valor >= a+b and valor < a+b+c):#Abajo
			direccion = 2
			self.setCord(1, 0)

		else:								#Izquierda
			direccion = 3
			self.setCord(0, -1)



	def calcGastos(self, matriz):
		self.nivBateria -= (self.bateria*2) + (int(self.motor*3.4)) + (self.camara*2) + ((matriz[self.x][self.y] - 3)*-3)


	def calcUp(self, matriz):
		valor = 0
		cant = 1
		for i in range(1, self.camara+1):
			aux = matriz[self.x-i][self.y]
			if(aux == 0):
				break

			if(self.motor > aux):
				aux += 1

			elif(self.motor < aux):
				aux -= 1

			valor += aux
			cant = i

		valor /= cant

		return valor



	def calcRight(self, matriz):
		valor = 0
		cant = 1
		for i in range(1, self.camara+1):
			
			aux = matriz[self.x][self.y+1]
			if(aux == 0):
				break

			if(self.motor > aux):
				aux += 1

			elif(self.motor < aux):
				aux -= 1

			valor += aux
			cant = i

		valor /= cant

		return valor



	def calcDown(self, matriz):
		valor = 0
		cant = 1
		for i in range(1, self.camara+1):
			aux = matriz[self.x+i][self.y]
			if(aux == 0):
				break

			if(self.motor > aux):
				aux += 1

			elif(self.motor < aux):
				aux -= 1

			valor += aux
			cant = i

		valor = valor/cant*0.3

		return valor



	def calcLeft(self, matriz):
		valor = 0
		cant = 1
		for i in range(1, self.camara+1):
			aux = matriz[self.x][self.y-1]
			if(aux == 0):
				break

			if(self.motor > aux):
				aux += 1

			elif(self.motor < aux):
				aux -= 1

			valor += aux
			cant = i

		valor = valor/cant*0.3

		return valor



	def toBin(self, n):
		return "{0:b}".format(n)

	def toInt(self, n):
		return int(n, 2)
