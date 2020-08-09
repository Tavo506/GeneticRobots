import random as r
from tkinter import *

class Robot:
	muto = False
	numPadre = 0
	numMadre = 0
	cromPadre = "000000"
	cromMadre = "000000"
	generacion = 0
	numRobot = 0
	cromosomas = "000000"
	motor = 1
	bateria = 1
	camara = 1
	nivBateria = 1
	x = 20
	y = 1
	distancia = 0
	pasos = 0
	exito = 0
	exitoNormal = 0
	recorrido = []

	def __init__(self, generacion, cromosomas, numPadre, cromPadre, numMadre, cromMadre, numRobot):
		self.muto = False
		self.generacion = generacion
		self.numRobot = numRobot
		self.cromosomas = cromosomas
		self.numPadre = numPadre
		self.numMadre = numMadre
		self.cromPadre = cromPadre
		self.cromMadre = cromMadre

		self.motor = self.toInt(cromosomas[2:4])
		self.bateria = self.toInt(cromosomas[0:2])
		self.camara = self.toInt(cromosomas[4:6])

		self.nivBateria = self.bateria*750
		self.recorrido = []
		self.pasos = 0
		self.exito = 0
		self.exitoNormal = 0
		self.distancia = 0

	def getNumPadre(self):
		return self.numPadre

	def getNumMadre(self):
		return self.numMadre

	def getCromPadre(self):
		return self.cromPadre

	def getCromMadre(self):
		return self.cromMadre

	def getGen(self):
		return self.generacion

	def getCrom(self):
		return self.cromosomas

	def getNum(self):
		return self.numRobot

	def getMotor(self):
		return self.motor

	def getBateria(self):
		return self.bateria

	def getCamara(self):
		return self.camara

	def getNivBateria(self):
		return self.nivBateria

	def getExitoNormal(self):
		return self.exitoNormal

	def setMuto(self):
		self.muto = True

	def getMuto(self):
		return self.muto	

	def setExitoNormal(self, exitoNormal):
		self.exitoNormal = exitoNormal

	def setCrom(self, cromosomas):
		self.motor = self.toInt(cromosomas[2:4])
		self.bateria = self.toInt(cromosomas[0:2])
		self.camara = self.toInt(cromosomas[4:6])
		self.cromosomas = cromosomas
		self.nivBateria = self.bateria*750


	def setCord(self, i, j):
		self.x += i
		self.y += j


	def getX(self):
		return self.x


	def getY(self):
		return self.y


	def setDist(self, distancia):
		self.distancia = distancia


	def getDist(self):
		return self.distancia


	def getPasos(self):
		return self.pasos


	def getBateriaG(self):
		return self.bateria*750 - self.nivBateria


	def setExito(self, exito):
		self.exito = exito

	def getExito(self):
		return self.exito

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

		 #if(self.motor == 1):
			#print(arriba, derecha, abajo, izquierda, self.getX(), self.getY())

		prom = (arriba + derecha + abajo + izquierda)/4


		if(arriba != 0):
			arriba = (arriba/prom/4)*1000

		if(derecha != 0):
			derecha = (derecha/prom/4)*1000

		if(abajo != 0):
			abajo = (abajo/prom/4)*1000

		if(izquierda != 0):
			izquierda = (izquierda/prom/4)*1000


		#print(arriba, derecha, abajo, izquierda)
		self.calcGastos(matriz)

		if(self.nivBateria < 0):
			return False


		self.mover(arriba, derecha, abajo, izquierda)


		if(self.x == 1 and self.y == 20):	#Si ya llegó a la meta
			return False


		#print(self.nivBateria, self.x, self.y)
	

		return True


	def mover(self, a, b, c, d):
		valor = r.randint(0, 1000)

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

		self.pasos += 1
		self.recorrido.append((self.x, self.y))



	def calcGastos(self, matriz):
		self.nivBateria -= (self.bateria*2) + (int(self.motor*3.4)) + (self.camara*2) + ((matriz[self.x][self.y] - 3)*-3)


	def calcUp(self, matriz):

		valor = 0
		cant = 1
		for i in range(1, self.camara+1):
			aux = matriz[self.x-i][self.y]
			if(aux == 0):
				break

			if(self.motor == 1 and aux in (1,2) ):
				aux /= 5
			elif(self.motor == 2 and aux == 1 ):
				aux /= 5
			else:
				aux += 2

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

			if(self.motor == 1 and aux in (1,2) ):
				aux /= 5
			elif(self.motor == 2 and aux == 1 ):
				aux /= 5
			else:
				aux += 2

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

			if(self.motor == 1 and aux in (1,2) ):
				aux /= 5
			elif(self.motor == 2 and aux == 1 ):
				aux /= 5
			else:
				aux += 2

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

			if(self.motor == 1 and aux in (1,2) ):
				aux /= 5
			elif(self.motor == 2 and aux == 1 ):
				aux /= 5
			else:
				aux += 2

			valor += aux
			cant = i

		valor = valor/cant*0.3

		return valor



	def toBin(self, n):
		return "{0:b}".format(n)

	def toInt(self, n):
		return int(n, 2)


	def verRec(self, casillas):
		for cord in self.recorrido:
			casillas[cord[0]][cord[1]].config(text=" X ")
		casillas[self.x][self.y].config(text=" O ")
		

	def limpiarRec(self, casillas):
		for cord in self.recorrido:
			casillas[cord[0]][cord[1]].config(text="     ")
