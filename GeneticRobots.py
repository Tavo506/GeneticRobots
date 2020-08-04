from tkinter import *
from Robot import *
from threading import Thread
import random as r


main = Tk()
main.configure(bg="#4A4A4F")
main.title("Genetic Robots")
main.geometry("800x600")
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


def bRob1():
	botonRobot1.config(bg = "#C6FFB9")
	botonRobot2.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot5.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][0]
	datosHijo.set("Generación : " + str(gen + 1) + "   Número : 1")


	datosPadre.set("Padre : " + rob.padre)
	
	if(gen+1 == 1):
		cromoPadre.set("Cromosomas : " + "XY")
		cromoMadre.set("Cromosomas : " + "XY")
	else:
		cromoPadre.set("Cromosomas : " + str(gen))
		cromoMadre.set("Cromosomas : " + str(gen))
	
	datosMadre.set("Madre : " + rob.madre)

	cromoHijo.set("Cromosomas : " + rob.cromosomas)
	bateriaHijo.set("Batería : " + str(rob.motor))
	motorHijo.set("Motor : " + str(rob.bateria))
	camaraHijo.set("Cámara : " + str(rob.camara))

	print(rob.getX(), rob.getY(), rob.nivBateria, rob.exito)
	
	return


def bRob2():
	botonRobot2.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot5.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][1]
	datosHijo.set("Generación : " + str(gen + 1) + "   Número : 1")


	datosPadre.set("Padre : " + rob.padre)
	
	if(gen+1 == 1):
		cromoPadre.set("Cromosomas : " + "XY")
		cromoMadre.set("Cromosomas : " + "XY")
	else:
		cromoPadre.set("Cromosomas : " + str(gen))
		cromoMadre.set("Cromosomas : " + str(gen))
	
	datosMadre.set("Madre : " + rob.madre)

	cromoHijo.set("Cromosomas : " + rob.cromosomas)
	bateriaHijo.set("Batería : " + str(rob.motor))
	motorHijo.set("Motor : " + str(rob.bateria))
	camaraHijo.set("Cámara : " + str(rob.camara))

	print(rob.getX(), rob.getY(), rob.nivBateria, rob.exito)
	
	return


def bRob3():
	botonRobot3.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot2.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot5.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][2]
	datosHijo.set("Generación : " + str(gen + 1) + "   Número : 1")


	datosPadre.set("Padre : " + rob.padre)
	
	if(gen+1 == 1):
		cromoPadre.set("Cromosomas : " + "XY")
		cromoMadre.set("Cromosomas : " + "XY")
	else:
		cromoPadre.set("Cromosomas : " + str(gen))
		cromoMadre.set("Cromosomas : " + str(gen))
	
	datosMadre.set("Madre : " + rob.madre)

	cromoHijo.set("Cromosomas : " + rob.cromosomas)
	bateriaHijo.set("Batería : " + str(rob.motor))
	motorHijo.set("Motor : " + str(rob.bateria))
	camaraHijo.set("Cámara : " + str(rob.camara))

	print(rob.getX(), rob.getY(), rob.nivBateria, rob.exito)
	
	return


def bRob4():
	botonRobot4.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot2.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot5.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][3]
	datosHijo.set("Generación : " + str(gen + 1) + "   Número : 1")


	datosPadre.set("Padre : " + rob.padre)
	
	if(gen+1 == 1):
		cromoPadre.set("Cromosomas : " + "XY")
		cromoMadre.set("Cromosomas : " + "XY")
	else:
		cromoPadre.set("Cromosomas : " + str(gen))
		cromoMadre.set("Cromosomas : " + str(gen))
	
	datosMadre.set("Madre : " + rob.madre)

	cromoHijo.set("Cromosomas : " + rob.cromosomas)
	bateriaHijo.set("Batería : " + str(rob.motor))
	motorHijo.set("Motor : " + str(rob.bateria))
	camaraHijo.set("Cámara : " + str(rob.camara))

	print(rob.getX(), rob.getY(), rob.nivBateria, rob.exito)
	
	return


def bRob5():
	botonRobot5.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot2.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot6.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][4]
	datosHijo.set("Generación : " + str(gen + 1) + "   Número : 1")


	datosPadre.set("Padre : " + rob.padre)
	
	if(gen+1 == 1):
		cromoPadre.set("Cromosomas : " + "XY")
		cromoMadre.set("Cromosomas : " + "XY")
	else:
		cromoPadre.set("Cromosomas : " + str(gen))
		cromoMadre.set("Cromosomas : " + str(gen))
	
	datosMadre.set("Madre : " + rob.madre)

	cromoHijo.set("Cromosomas : " + rob.cromosomas)
	bateriaHijo.set("Batería : " + str(rob.motor))
	motorHijo.set("Motor : " + str(rob.bateria))
	camaraHijo.set("Cámara : " + str(rob.camara))

	print(rob.getX(), rob.getY(), rob.nivBateria, rob.exito)
	
	return


def bRob6():
	botonRobot6.config(bg="#C6FFB9")
	botonRobot1.config(bg = "white")
	botonRobot2.config(bg = "white")
	botonRobot3.config(bg = "white")
	botonRobot4.config(bg = "white")
	botonRobot5.config(bg = "white")

	gen = int(entryGen.get()) - 1
	rob = listaRobots[gen][5]
	datosHijo.set("Generación : " + str(gen + 1) + "   Número : 1")


	datosPadre.set("Padre : " + rob.padre)
	
	if(gen+1 == 1):
		cromoPadre.set("Cromosomas : " + "XY")
		cromoMadre.set("Cromosomas : " + "XY")
	else:
		cromoPadre.set("Cromosomas : " + str(gen))
		cromoMadre.set("Cromosomas : " + str(gen))
	
	datosMadre.set("Madre : " + rob.madre)

	cromoHijo.set("Cromosomas : " + rob.cromosomas)
	bateriaHijo.set("Batería : " + str(rob.motor))
	motorHijo.set("Motor : " + str(rob.bateria))
	camaraHijo.set("Cámara : " + str(rob.camara))

	print(rob.getX(), rob.getY(), rob.nivBateria, rob.exito)
	
	return


def createCrom():
	cromosomas = ""

	motor = "0" + toBin(r.randint(1,3))
	motor = motor[len(motor)-2 : len(motor)]

	bateria = "0" + toBin(r.randint(1,3))
	bateria = bateria[len(bateria)-2 : len(bateria)]

	camara = "0" + toBin(r.randint(1,3))
	camara = camara[len(camara)-2 : len(camara)]

	cromosomas = motor+bateria+camara

	return cromosomas


def convergen():
	global generaciones
	if(generaciones > 5):
		return True
	return False

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

	exito = (dist*4 + pasos + bateriaG)/3
	
	rob.setExito(exito)



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

cromoHijo.set("Cromosomas : ")
bateriaHijo.set("Batería : ")
motorHijo.set("Motor : ")
camaraHijo.set("Cámara : ")



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

listaRobots = []
listaRobots.append([])

generaciones = 1

rob1 = Robot(generaciones, createCrom(), "Tavo B", "Tavo A")
rob2 = Robot(generaciones, createCrom(), "Tavo B", "Tavo A")
rob3 = Robot(generaciones, createCrom(), "Tavo B", "Tavo A")
rob4 = Robot(generaciones, createCrom(), "Tavo B", "Tavo A")
rob5 = Robot(generaciones, createCrom(), "Tavo B", "Tavo A")
rob6 = Robot(generaciones, createCrom(), "Tavo B", "Tavo A")

listaRobots[generaciones-1].append(rob1)
listaRobots[generaciones-1].append(rob2)
listaRobots[generaciones-1].append(rob3)
listaRobots[generaciones-1].append(rob4)
listaRobots[generaciones-1].append(rob5)
listaRobots[generaciones-1].append(rob6)


t1 = Thread(target=caminar, args=(rob1,))
t2 = Thread(target=caminar, args=(rob2,))
t3 = Thread(target=caminar, args=(rob3,))
t4 = Thread(target=caminar, args=(rob4,))
t5 = Thread(target=caminar, args=(rob5,))
t6 = Thread(target=caminar, args=(rob6,))


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


while(not convergen()):
	generaciones += 1
	listaRobots.append([])




v.set("Generaciones: " + str(generaciones))

main.mainloop()
