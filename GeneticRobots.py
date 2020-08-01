from tkinter import *


main = Tk()
main.configure(bg="#4A4A4F")
main.title("Genetic Robots")
main.geometry("800x600")
main.resizable(False, False)


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
		return "#C78239"
	elif(value == 2):
		return "#914A00"
	elif(value == 3):
		return "#5E3000"

"""
0 = camino bloqueado
1 = camino noraml
2 = camino moderado
3 = camino dificil
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


matriz = readFile()
listaLabels = Carga_Maze(main)

listaLabels[20][1].config(bg="green")
listaLabels[1][20].config(bg="red")



main.mainloop()
