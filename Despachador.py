import math
from Procesos import Procesos
import tkinter as tk
from tkinter import ttk

class Microprocesador():
    
    
    #Class Attribute 
    def __init__(self, num):
        self.num = num
        self.procesos = []
        self.cantidadProceso = len(self.procesos)

    def anadirProceso(self, proceso):
        self.procesos.append(proceso)




class Despachador():
    pass
    microprocesadores = []
    listaDeProcesos = []
    numDeMicro = None
    entryMicro = None
    entryQuantums = None

    

    def aniadirMicroprocesador(self, num):
        micro = Microprocesador(num)
        self.microprocesadores.append(micro)

    
    def aniadirProcesos(self, duracionQuantum, num, names, tiemposEjecucion, numBloqueos, duracionBloqueo, duracionCambio):

        #Aqui se debe revisar el numero de microprocesadores

        for i in range(num-1):
            tvc = ((math.ceil(tiemposEjecucion[i] / float(duracionQuantum))) - 1) * duracionCambio

            tb = numBloqueos[i]*duracionBloqueo

            if i == 0:
                tt = tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo  
                proceso = Procesos(names[i], 0, tvc, tiemposEjecucion[i], tb, 0, tt, tt)

                self.microprocesadores[0].procesos.append(proceso)

            else:
                #AQUI SE DEBE CHECAR QUE MICRO TIENE MENOS TIEMPO FINAL EN SU ULTIMA POSICION DE PROCESOS .TF
                tt = duracionCambio + tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                ti = self.microprocesadores[0].procesos[i-1].tf
                proceso = Procesos(names[i], duracionCambio, tvc, tiemposEjecucion[i], tb, ti, tt, ti + tt)
                self.microprocesadores[0].procesos.append(proceso)

        #Aqui checar si hay mas de un micro
    
    def imprimirEstado(self):
        
        for i in range(len(self.microprocesadores)):
            print( "Microprocesador " + str(i+1))
            print( " Proceso " + " TCC    "+" TE    "+" TVC    "	+"  TB   "	+ "    TT   "	+"     TI   "+ 	"     TF   ")
            for j in range(len(self.microprocesadores[i].procesos)):
                print("      " +self.microprocesadores[i].procesos[j].name + "      " +  str(self.microprocesadores[i].procesos[j].tcc) + "      " +str(self.microprocesadores[i].procesos[j].tiempoEjecucion) +"     " + str(self.microprocesadores[i].procesos[j].tvc) + "      " +str(self.microprocesadores[i].procesos[j].tb) +"     " + str(self.microprocesadores[i].procesos[j].tt) +"    " + str(self.microprocesadores[i].procesos[j].ti) +"   " + str(self.microprocesadores[i].procesos[j].tf))


    def lecturaDeArchivo(self):
        archivo = open("proceso.txt", "r")
        if archivo.mode == 'r':
           linea=archivo.readlines()
           for x in linea:
                lineaActual = x.split(',')
                print(lineaActual[0], " ", lineaActual[1], " ", lineaActual[2])
                proceso = Procesos(lineaActual[0],lineaActual[1],lineaActual[2],0,0,0,0,0)
                self.listaDeProcesos.append(proceso)
            
        for i in range(len(self.listaDeProcesos)):
            print(self.listaDeProcesos[i])

    def prueba(self):
        self.numDeMicro = self.entryMicro.get()
        print(self.numDeMicro)
        print("hola l")

    def interfaz (self):
        root = tk.Tk()
        root.config(width=300, height=200)
        
        #grid = Grid()
        labelQuantums = tk.Label(root, text = "Quantums").grid(row = 0)
        self.entryQuantums = tk.Entry(root).grid(row = 0, column = 1)
        labelMicro = tk.Label(root, text = "Numero de micros").grid(row = 1)
        self.entryMicro = tk.Entry(root)
        self.entryMicro.grid(row = 1 , column = 1)
        frame_canvas = tk.Frame(root)
        frame_canvas.grid(row=7 , column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        canvas = tk.Canvas(frame_canvas, bg="gray")
        canvas.grid(row=0, column=0, sticky="news")
        rows = len(self.listaDeProcesos)
        columns = 3
        #procesos = [[tk.Lable() for j in range(columns)] for i in range(rows)]
        '''
        for i in range(0, rows):
            procesoNom = tk.Label (text = self.listaDeProcesos[i].name)
            procesoNom.grid(row = i, columns=0)
            proceso = tk.Label (text = self.listaDeProcesos[i].tt)
            procesoNom.grid(row = i, columns=1)
        '''

            
        
        button = ttk.Button(root,text ="Mostrar Tabla", command = self.prueba)
        button.grid(row = 6)
        button.pack
        root.mainloop()


def main():
    
    despachador = Despachador()
    despachador.lecturaDeArchivo()
    #Todo esto se va leer del txt
    numeroProcesos = 17
    numeroMicros = 1
    tiempoBloqueo = 10
    tiempoCambio = 10
    duracionQuantum = 100
    #Procurar ponerlos en orden de ejecucion
    nombres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Q", "O", "P"]
    #Estos deben coincidir con las letras de arriba
    numBloqueos = [1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2]
    tiemposEjecucion = [1000,300,208,100,1000,300,200,100,1000,1200,200,100,300,400,100,210]

    for i in range(numeroMicros):
        despachador.aniadirMicroprocesador(i+1)

    despachador.aniadirProcesos(duracionQuantum, numeroProcesos, nombres, tiemposEjecucion, numBloqueos, tiempoBloqueo, tiempoCambio)
    despachador.interfaz()
    #despachador.imprimirEstado()



if __name__ == '__main__':
    main()