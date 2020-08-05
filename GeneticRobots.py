from tkinter import *
from Robot import *
from threading import Thread
import random as r


main = Tk()
main.configure(bg="#4A4A4F")
main.title("Genetic Robots")
main.geometry("800x600+500+200")
main.resizable(False, False)

v = StringVar()


"""
Funciones|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
"""

def readFile():
	lista = []
	file = open("maze.txt", "r")
	contenido = file.read()

	for i in range(22):
		lista.append([])
		for j in range(22):
			lista[i].append(int(contenido[j+i*23]))

	return lista


def getColor(value):
	if(value == 0):
		return "#2E1700"
	elif(value == 1):
		return "#5E3000"
	elif(value == 2):
		return "#914A00"
	elif(value == 3):
		return "#C78239"
	elif(value == 4):
		return "#00FF00"
	elif(value == 5):
		return "#FF0000"


def toBin(n):
	return "{0:b}".format(n)

def toInt(n):
	return int(n, 2)

"""
0 = camino bloqueado
1 = camino dificil
2 = camino moderado
3 = camino normal
4 = inicio
5 = fin
"""
def Carga_Maze(main):
    lista = []
    for i in range(22):
        lista.append([])
        for j in range(22):
            aux = Label(main, bg=getColor(matriz[i][j]), text="     ", relief=RAISED)
            aux.grid(row=i, column=j)
            lista[i].append(aux)
    return lista




def incGen():
	try:
		gen = int(entryGen.get())
		if(gen < generaciones):
			entryGen.delete(0, END)
			entryGen.insert(0, gen+1)
		else:
			entryGen.delete(0, END)
			entryGen.insert(0, generaciones)
	except:
		entryGen.insert(0, "0")

def decGen():
	try:
		gen = int(entryGen.get())
		if(gen > 1):
			entryGen.delete(0, END)
			entryGen.insert(0, gen-1)
		if(gen > generaciones):
			entryGen.delete(0, END)
			entryGen.insert(0, generaciones)
	except:
		entryGen.insert(0, "0")


def verDatosRob(rob):
	global listaLabels
	global lastRob

	datosHijo.set("Generación : " + str(rob.getGen()) + "   Número : " + rob.getNum())


	datosPadre.set("Padre : " + rob.getNumPadre())
	cromoPadre.set("Cromosomas : " + rob.getCromPadre())
	
	datosMadre.set("Madre : " + rob.getNumMadre())
	cromoMadre.set("Cromosomas : " + rob.getCromMadre())

	cromoHijo.set("Cromosomas : " + rob.getCrom())
	bateriaHijo.set("Batería : " + str(rob.getBateria()))
	motorHijo.set("Motor : " + str(rob.getMotor()))
	camaraHijo.set("Cámara : " + str(rob.getCamara()))
	exitoHijo.set("Éxito : " + str(rob.getExito()))

	if(lastRob != None):
		lastRob.limpiarRec(listaLabels)

	rob.verRec(listaLabels)
	lastRob = rob

	print(rob.getX(), rob.getY(), rob.getNivBateria(), rob.getPasos(), rob.getMuto())


def bRob1():
	botonRobot1.config(bg = "#C6FFB9")
	botonRobot2.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot5.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][0]

	verDatosRob(rob)
	



def bRob2():
	botonRobot2.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot5.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][1]
	
	verDatosRob(rob)


def bRob3():
	botonRobot3.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot2.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot5.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][2]
	
	verDatosRob(rob)


def bRob4():
	botonRobot4.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot2.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot5.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][3]
	
	verDatosRob(rob)


def bRob5():
	botonRobot5.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot2.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][4]
	
	verDatosRob(rob)


def bRob6():
	botonRobot6.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot2.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot5.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][5]
	
	verDatosRob(rob)


def createCrom():
	cromosomas = ""

	motor = "0" + toBin(r.randint(1,2))
	motor = motor[len(motor)-2 : len(motor)]

	bateria = "0" + toBin(r.randint(1,2))
	bateria = bateria[len(bateria)-2 : len(bateria)]

	camara = "0" + toBin(r.randint(1,2))
	camara = camara[len(camara)-2 : len(camara)]

	cromosomas = motor+bateria+camara

	return cromosomas


def convergen():
	global generaciones
	if(generaciones > 10):
		return True
	return False


def calcNormal(listaBots):

	norm1 = listaBots[0].getExito()
	norm2 = listaBots[1].getExito()
	norm3 = listaBots[2].getExito()
	norm4 = listaBots[3].getExito()
	norm5 = listaBots[4].getExito()
	norm6 = listaBots[5].getExito()

	prom = (norm1 + norm2 + norm3 + norm4 + norm5 + norm6) / 6

	norm1 = (norm1/prom/6)*100
	norm2 = (norm2/prom/6)*100
	norm3 = (norm3/prom/6)*100
	norm4 = (norm4/prom/6)*100
	norm5 = (norm5/prom/6)*100
	norm6 = (norm6/prom/6)*100

	listaBots[0].setExitoNormal(norm1)
	listaBots[1].setExitoNormal(norm2)
	listaBots[2].setExitoNormal(norm3)
	listaBots[3].setExitoNormal(norm4)
	listaBots[4].setExitoNormal(norm5)
	listaBots[5].setExitoNormal(norm6)

	print(norm1, norm2, norm3, norm4, norm5, norm6)



#Pitagoras
def distancia(x, y):
	cat1 = (x - 1)**2
	cat2 = (20 - y)**2
	dist = (cat1 + cat2)**(0.5)
	return dist


def caminar(rob):
	global matriz
	puedeAndar = True

	while(puedeAndar):
		puedeAndar = rob.seleccion(matriz)

	dist = distancia(rob.getX(), rob.getY())
	pasos = rob.getPasos()
	bateriaG = rob.getBateriaG()

	exito = (dist*4 + pasos + abs(bateriaG))/3
	
	rob.setExito(exito)


def seleccion(lista):
	
	norm1 = lista[0].getExitoNormal()
	norm2 = lista[1].getExitoNormal()
	norm3 = lista[2].getExitoNormal()
	norm4 = lista[3].getExitoNormal()
	norm5 = lista[4].getExitoNormal()
	norm6 = lista[5].getExitoNormal()

	listaPadres = []

	for i in range(6):
		valor = r.uniform(0, 100)

		if(valor < norm1):						
			listaPadres.append(lista[0])

		elif(valor >= norm1 and valor < norm1+norm2):	
			listaPadres.append(lista[1])
			
		elif(valor >= norm1+norm2 and valor < norm1+norm2+norm3):
			listaPadres.append(lista[2])

		elif(valor >= norm1+norm2+norm3 and valor < norm1+norm2+norm3+norm4):
			listaPadres.append(lista[3])

		elif(valor >= norm1+norm2+norm3+norm4 and valor < norm1+norm2+norm3+norm4+norm5):
			listaPadres.append(lista[4])

		else:								
			listaPadres.append(lista[5])

	return listaPadres


def swap(padre, madre, val1, val2):
	aux = padre[val1:val2]
	padre = padre[0:val1] + madre[val1:val2] + padre[val2:6]
	madre = madre[0:val1] + aux + madre[val2:6]

	if(padre[0:2]=="00"):
			padre = "01"+padre[2:6]
	if(padre[2:4]=="00"):
			padre = padre[0:2]+"01"+padre[4:6]
	if(padre[4:6]=="00"):
			padre = padre[0:4]+"01"

	if(madre[0:2]=="00"):
			madre = "01"+madre[2:6]
	if(madre[2:4]=="00"):
			madre = madre[0:2]+"01"+madre[4:6]
	if(madre[4:6]=="00"):
			madre = madre[0:4]+"01"

	return (padre, madre)


def change(val1, val2, bot):

	cromosomas = bot.getCrom()
	aux = cromosomas[val1:val2]
	aux = aux.replace("0","2")
	aux = aux.replace("1","0")
	aux = aux.replace("2", "1")

	cromosomas = cromosomas[0:val1] + aux + cromosomas[val2:6]
	
	#Revisa que la mutacion no haya generado un cromosoma cero, tampoco queremos que salgan con down
	if(cromosomas[0:2]=="00"):
			cromosomas = "01"+cromosomas[2:6]
	if(cromosomas[2:4]=="00"):
			cromosomas = cromosomas[0:2]+"01"+cromosomas[4:6]
	if(cromosomas[4:6]=="00"):
			cromosomas = cromosomas[0:4]+"01"


	return cromosomas


def mutar(bot):
	global listaRobots

	val1 = r.randint(0, 6)
	val2 = r.randint(0, 6)

	if(val1 > val2):
		aux = val1
		val1 = val2
		val2 = aux

	bot.setCrom(change(val1, val2, bot))




def cruce(listaPadres):
	global listaRobots
	global generaciones
	global indiceMutacion

	for i in range(0, 5, 2):
		val1 = r.randint(0, 6)
		val2 = r.randint(0, 6)

		if(val1 > val2):
			aux = val1
			val1 = val2
			val2 = aux

		padre = listaPadres[i]
		madre = listaPadres[i+1]

		Ncromosomas = swap(padre.getCrom(), madre.getCrom(), val1, val2)

		rob1 = Robot(generaciones, Ncromosomas[0], padre.getNum(), padre.getCrom(), madre.getNum(), madre.getCrom(), str(i+1))
		rob2 = Robot(generaciones, Ncromosomas[1], padre.getNum(), padre.getCrom(), madre.getNum(), madre.getCrom(), str(i+2))

		if(r.randint(0,100) <= indiceMutacion):
			rob1.setMuto()
			mutar(rob1)
		if(r.randint(0,100) <= indiceMutacion):
			rob2.setMuto()
			mutar(rob2)

		listaRobots[generaciones-1].append(rob1)
		listaRobots[generaciones-1].append(rob2)




def hilos(generaciones, listaRobots):
	t1 = Thread(target=caminar, args=(listaRobots[generaciones-1][0],))
	t2 = Thread(target=caminar, args=(listaRobots[generaciones-1][1],))
	t3 = Thread(target=caminar, args=(listaRobots[generaciones-1][2],))
	t4 = Thread(target=caminar, args=(listaRobots[generaciones-1][3],))
	t5 = Thread(target=caminar, args=(listaRobots[generaciones-1][4],))
	t6 = Thread(target=caminar, args=(listaRobots[generaciones-1][5],))


	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()
	t6.join()



"""
Fin funciones|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||












############################################################################################################################################################
init components
"""
cantGen = Label(main, bg = "#4A4A4F", fg = "white", textvariable = v).grid(row=22, columnspan=7)

botonIzq = Button(main, bg = "white", text="◀", command=decGen).grid(row=23, column=8)

botonDer = Button(main, bg = "white", text="▶", command=incGen).grid(row=23, column=13)



entryGen = Entry(main, bg = "white", font = (13), width = 5, justify = CENTER)
entryGen.grid(row=23, column=9, columnspan = 4, sticky = W + E, padx = 5)
entryGen.insert(0, "1")

"""
Verificación de input________________________________________________________________
"""																					#|
def ValidGen(inp):																	#|
    if (inp.isdigit() and (len(inp) <= len(str(generaciones))) or (len(inp) == 0)):	#|
        return True																	#|
    else:																			#|
        return False																#|
        																			#|
validarGen = main.register(ValidGen)												#|
entryGen.config(validate="key", validatecommand=(validarGen, '%P'))					#|
"""																					#|
____________________________________________________________________________________#|
"""

Label(main, bg = "#4A4A4F").grid(row=25)

bot1 = PhotoImage(file = "bot001.PNG")
bot2 = PhotoImage(file = "bot010.PNG")
bot3 = PhotoImage(file = "bot011.PNG")
bot4 = PhotoImage(file = "bot100.PNG")
bot5 = PhotoImage(file = "bot101.PNG")
bot6 = PhotoImage(file = "bot110.PNG")


botonRobot1 = Button(main, image=bot1, command = bRob1)
botonRobot1.grid(row = 26, column = 1, columnspan = 4, sticky = E)
botonRobot2 = Button(main, image=bot2, command = bRob2)
botonRobot2.grid(row = 26, column = 4, columnspan = 4, sticky = E)
botonRobot3 = Button(main, image=bot3, command = bRob3)
botonRobot3.grid(row = 26, column = 7, columnspan = 4, sticky = E)
botonRobot4 = Button(main, image=bot4, command = bRob4)
botonRobot4.grid(row = 26, column = 10, columnspan = 4, sticky = E)
botonRobot5 = Button(main, image=bot5, command = bRob5)
botonRobot5.grid(row = 26, column = 13, columnspan = 4, sticky = E)
botonRobot6 = Button(main, image=bot6, command = bRob6)
botonRobot6.grid(row = 26, column = 16, columnspan = 4, sticky = E)

Label(main, bg = "#4A4A4F", width=3).grid(column = 23)


#Labels y strings de datos --------------------------------------------------------------------------------------------------------------------------

datosHijo = StringVar()

datosHijo.set("Generación : ####   Número : #")

datosPadre = StringVar()
cromoPadre = StringVar()
datosMadre = StringVar()
cromoMadre = StringVar()

datosPadre.set("Padre : ")
cromoPadre.set("Cromosomas : ")
datosMadre.set("Madre : ")
cromoMadre.set("Cromosomas : ")

cromoHijo = StringVar()
bateriaHijo = StringVar()
motorHijo = StringVar()
camaraHijo = StringVar()
exitoHijo = StringVar()

cromoHijo.set("Cromosomas : ")
bateriaHijo.set("Batería : ")
motorHijo.set("Motor : ")
camaraHijo.set("Cámara : ")
exitoHijo.set("Éxito : ")



labelDatosHijo = Label(main, textvariable = datosHijo, font = ("Arial", 14, "bold"), bg = "#4A4A4F", fg="white")
labelDatosHijo.grid(row = 1, column = 24, columnspan = 20, rowspan = 2)

labelDatosPadre = Label(main, textvariable = datosPadre, font = (16), width = 14, anchor = W)
labelDatosPadre.grid(row = 3, column = 24, rowspan = 2, columnspan=5, sticky = W)

labelCromoPadre = Label(main, textvariable = cromoPadre, font = (16), width = 28, anchor = W)
labelCromoPadre.grid(row = 5, column = 24, rowspan = 2, columnspan=5, sticky = W)

labelDatosMadre = Label(main, textvariable = datosMadre, font = (16), width = 14, anchor = W)
labelDatosMadre.grid(row = 7, column = 24, rowspan = 2, columnspan=5, sticky = W)

labelCromoMadre = Label(main, textvariable = cromoMadre, font = (16), width = 28, anchor = W)
labelCromoMadre.grid(row = 9, column = 24, rowspan = 2, columnspan=5, sticky = W)

Label(main, text = "Datos Robot", font = ("Arial", 18, "bold"), bg = "#4A4A4F", fg="white").grid(row = 12, column = 24, rowspan = 2, columnspan=5)

labelCromoHijo = Label(main, textvariable = cromoHijo, font = (16), width = 28, anchor = W)
labelCromoHijo.grid(row = 14, column = 24, rowspan = 2, columnspan=5, sticky = W)

labelBateria = Label(main, textvariable = bateriaHijo, font = (16), width = 14, anchor = W)
labelBateria.grid(row = 16, column = 24, rowspan = 2, columnspan=5, sticky = W)

labelMotor = Label(main, textvariable = motorHijo, font = (16), width = 14, anchor = W)
labelMotor.grid(row = 18, column = 24, rowspan = 2, columnspan=5, sticky = W)

labelCamara = Label(main, textvariable = camaraHijo, font = (16), width = 14, anchor = W)
labelCamara.grid(row = 20, column = 24, rowspan = 2, columnspan=5, sticky = W)

labelCamara = Label(main, textvariable = exitoHijo, font = ("Arial", 23), width = 14, anchor = W)
labelCamara.grid(row = 24, column = 24, rowspan = 2, columnspan=5, sticky = W)

# Fin labels y datos --------------------------------------------------------------------------------------------------------------------------------


"""
############################################################################################################################################################
"""






"""
main $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

matriz = readFile()
matriz[20][1] = 4
matriz[1][20] = 5
listaLabels = Carga_Maze(main)

lastRob = None

indiceMutacion = 16

listaRobots = []
listaRobots.append([])

generaciones = 1

rob1 = Robot(generaciones, createCrom(), "Tavo B", "XY", "Tavo A", "XY", "1")
rob2 = Robot(generaciones, createCrom(), "Tavo B", "XY", "Tavo A", "XY", "2")
rob3 = Robot(generaciones, createCrom(), "Tavo B", "XY", "Tavo A", "XY", "3")
rob4 = Robot(generaciones, createCrom(), "Tavo B", "XY", "Tavo A", "XY", "4")
rob5 = Robot(generaciones, createCrom(), "Tavo B", "XY", "Tavo A", "XY", "5")
rob6 = Robot(generaciones, createCrom(), "Tavo B", "XY", "Tavo A", "XY", "6")

listaRobots[generaciones-1].append(rob1)
listaRobots[generaciones-1].append(rob2)
listaRobots[generaciones-1].append(rob3)
listaRobots[generaciones-1].append(rob4)
listaRobots[generaciones-1].append(rob5)
listaRobots[generaciones-1].append(rob6)






while(not convergen()):
	hilos(generaciones, listaRobots)
	generaciones += 1
	listaRobots.append([])
	
	calcNormal(listaRobots[generaciones-2])

	cruce(seleccion(listaRobots[generaciones-2]))
	




v.set("Generaciones: " + str(generaciones-1))

main.mainloop()
