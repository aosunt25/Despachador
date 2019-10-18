import math
from Procesos import Procesos
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

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
    tiempoMenor = 0
    tiempoEn =0
    index = 0
    counter = 0
    microprocesadores = []
    listaDeProcesos = []
    tamanioDeProceso = []
    tiempoDeEntrada = []
    cantidadDeBloqueo = []

    numDeMicro = None
    entryMicro = None
    entryNumMicro = None
    entryQuantums = None
    labelNumDeMicros= None
    canBloque = None
    entryBloque = None
    cambioCon = None
    entryCambio = None
    root = tk.Tk()
    frame_canvasMicro= None
    canvasMicro= None
    frameMicro = None
    accept = True
    frame_canvasListaMicro = None
    tiemposEntrada=[]
    rows = 0

    #Variables de la Tabla de Micros 
    procesoNom = tk.Label(root)
    procesoTCC = tk.Label(root)
    procesoTiempo = tk.Label(root)
    procesoBloq = tk.Label(root) 

    

    def aniadirMicroprocesador(self, num):
        micro = Microprocesador(num)
        self.microprocesadores.append(micro)

    
    def aniadirProcesos(self, duracionQuantum, num, names, tiemposEjecucion, numBloqueos, duracionBloqueo, duracionCambio, tEntrada):

        #Aqui se debe revisar el numero de microprocesadores

        for i in range(num):
            self.tiempoMenor = 100000
            self.accept = True
            tvc = ((math.ceil(tiemposEjecucion[i] / float(duracionQuantum))) - 1) * duracionCambio
            tb = numBloqueos[i]*duracionBloqueo
            
            for j in range(len(self.microprocesadores)):
                if j < num:
                    print(self.microprocesadores[j].procesos)
                    if len(self.microprocesadores[j].procesos) == 0:
                        print("HOLLOOOO")
                        tb = numBloqueos[j]*duracionBloqueo
                        tvc = ((math.ceil(tiemposEjecucion[j] / float(duracionQuantum))) - 1) * duracionCambio
                        tt = tiemposEjecucion[j] + tvc + numBloqueos[j]*duracionBloqueo
                        #proceso = Procesos(names[j], tt, tiemposEjecucion[j], 0, tvc, tb, 0, tt)
                        if tEntrada[j] > 0:
                            ti = tEntrada[j]
                            proceso = Procesos(names[j], tt, tiemposEjecucion[j], 0, tvc, tb, ti, ti + tt)
                        else:
                            ti = 0
                            proceso = Procesos(names[j], tt, tiemposEjecucion[j], 0, tvc, tb, 0, tt)
                        

                        self.microprocesadores[j].procesos.append(proceso)
                        self.accept = False
                        self.counter += 1
                        if j == 0:
                            self.tiempoMenor = tt
                        print(self.tiempoMenor)
            if self.accept != False:
                if len(self.microprocesadores)>1:
                    for k in range(len(self.microprocesadores)):
                        lene = len(self.microprocesadores[k].procesos)
                        if k < num:
                            if self.tiempoMenor> self.microprocesadores[k].procesos[lene-1].tf:
                                self.tiempoMenor = self.microprocesadores[k].procesos[lene-1].tf
                                self.index = k
                    if self.counter < num:
                        self.tiempoEn = tEntrada[self.counter]
                        tb = numBloqueos[self.counter]*duracionBloqueo
                        tvc = ((math.ceil(tiemposEjecucion[self.counter] / float(duracionQuantum))) - 1) * duracionCambio
                        if self.tiempoMenor < self.tiempoEn:
                            #tvc = ((math.ceil(tiemposEjecucion[self.counter] / float(duracionQuantum))) - 1) * duracionCambio
                            ti = self.tiempoEn
                            tt = tiemposEjecucion[self.counter] + tvc + numBloqueos[self.counter]*duracionBloqueo
                            proceso = Procesos(names[self.counter], tt, tiemposEjecucion[self.counter], 0, tvc, tb, ti, ti + tt)
                        else:
                            ti = self.tiempoMenor
                            tt = duracionCambio + tiemposEjecucion[self.counter] + tvc + numBloqueos[self.counter]*duracionBloqueo
                            proceso = Procesos(names[self.counter], tt, tiemposEjecucion[self.counter], duracionCambio, tvc, tb, ti, ti + tt)
                        
                        self.microprocesadores[self.index].procesos.append(proceso)
                    self.counter += 1
                else:
                    if self.microprocesadores[0].procesos[i-1].tf < tEntrada[i]:
                        ti = tEntrada[i]
                        tt = tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                        proceso = Procesos(names[i], tt, tiemposEjecucion[i], 0, tvc, tb, ti, ti + tt)
                    else:
                        ti = self.microprocesadores[0].procesos[i-1].tf
                        tt = duracionCambio + tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                        proceso = Procesos(names[i], tt, tiemposEjecucion[i], duracionCambio, tvc, tb, ti, ti + tt)

                    
                    self.microprocesadores[0].procesos.append(proceso)


    
    
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
                self.listaDeProcesos.append(lineaActual[0])
                self.tamanioDeProceso.append(lineaActual[1])
                self.tiempoDeEntrada.append(lineaActual[2])
                self.cantidadDeBloqueo.append(lineaActual[3])
            
      

    def prueba(self):
        self.lecturaDeArchivo()
        numeroProcesos = 17

        numeroMicros = int(self.entryMicro.get())
        tiempoBloqueo = int(self.entryBloque.get())
        tiempoCambio = int(self.entryCambio.get())
        duracionQuantum = int(self.entryQuantums.get())

        #Procurar ponerlos en orden de ejecucion
        nombres = ["B", "D", "F", "H", "J", "L", "N", "O", "A", "C", "E", "G", "I", "K", "M", "P", "Z"]
        #Estos deben coincidir con las letras de arriba
        numBloqueos = [2,2,3,4,2,5,2,3,2,2,5,2,3,2,2,4,3]
        tiemposEjecucion = [300,100,500,700,300,3000,50,600,400,50,1000,10,450,100,80,800,500]
        tiemposEntrada = [0,0,0,0,1500,1500,1500,1500,3000,3000,3000,3000,3000,4000,4000,4000,8000]

        for i in range(numeroMicros):
            self.aniadirMicroprocesador(i+1)

        self.aniadirProcesos(duracionQuantum, numeroProcesos, nombres, tiemposEjecucion, numBloqueos, tiempoBloqueo, tiempoCambio, tiemposEntrada)
        self.imprimirEstado


        self.frame_canvasListaMicro = tk.Canvas(self.root, bg = "red", highlightbackground="black" , highlightthickness = 2 )
        self.frame_canvasListaMicro.grid(row=3 , column=7,  sticky='nw')
        self.frame_canvasListaMicro.grid_rowconfigure(0, weight=1)
        self.frame_canvasListaMicro.grid_columnconfigure(0, weight=1)

        for j in range(0,len(self.microprocesadores)):

            #Se crea el primer Frame de la lista de Micros  
            self.frame_canvasMicro = tk.Frame(self.frame_canvasListaMicro, bg = "red", highlightbackground="black" , highlightthickness = 2 )
            self.frame_canvasMicro.grid(row=j , column=0,  sticky='nw')
            self.frame_canvasMicro.grid_rowconfigure(0, weight=1)
            self.frame_canvasMicro.grid_columnconfigure(0, weight=1)
            
            #Se creo el Canvas de la Lista de Micros 
            self.canvasMicro = tk.Canvas(self.frame_canvasMicro, bg="gray")
            self.canvasMicro.grid(row=1, column=0, sticky="news")
            
            #Se crea el Frame que tendra guardado los datos de los Micros
            self.frameMicro = tk.Frame(self.frame_canvasMicro, bg="gray", width = self.frame_canvasMicro.winfo_width())

            self.frameMicro.grid_columnconfigure(0,weight = 1, pad = 50)
            self.frameMicro.grid_columnconfigure(1,weight = 1, pad = 35)
            self.frameMicro.grid_columnconfigure(2,weight = 1, pad = 35)
            self.frameMicro.grid_columnconfigure(3,weight = 1, pad = 65)
            self.frameMicro.grid_columnconfigure(4,weight = 1, pad = 40)
            self.frameMicro.grid_columnconfigure(5,weight = 1, pad = 50)
            self.frameMicro.grid_columnconfigure(6,weight = 1, pad = 15)
            self.frameMicro.grid_columnconfigure(7,weight = 1, pad = 30)
            
            
            self.canvasMicro.create_window((0, 0), window=self.frameMicro, anchor='nw')

            #Se creo una ScrollBar para poder mostrar todos los Micros en un espacio compacto
            vsb = tk.Scrollbar(self.frame_canvasMicro, orient="vertical", command=self.canvasMicro.yview, bg = "black")
            vsb.grid(row=1, column=1, sticky='ns')
            self.canvasMicro.configure(yscrollcommand=vsb.set)


            #Se crea el Lable que muestra el menu de la tabla
            menuDeTablaMicros = tk.Label(self.frame_canvasMicro, text = "Proceso	    TCC	    TE	    TVC	    TB	    TT	    TI	    TF       ", bg = "red")
            menuDeTablaMicros.grid(row = 0, column = 0)

            self.frameMicro.update_idletasks() 
            self.canvasMicro.config(scrollregion=self.canvasMicro.bbox("all"))

            self.rows = len(self.microprocesadores[j].procesos)

             
            columns = 3
        #Agrega cada proceso al Frame por Nombre, Tamao, Tiempo de Entrada y Bloqueo
        
            for i in range(0, self.rows):
                self.procesoNom = tk.Label (self.frameMicro, text = self.microprocesadores[j].procesos[i].name, bg = "gray",fg = "white")
                self.procesoNom.grid(row = i, column=0)
                self.procesoTCC = tk.Label (self.frameMicro, text = str(self.microprocesadores[j].procesos[i].tcc),bg = "gray", fg = "white")
                self.procesoTCC.grid(row = i, column=1)
                self.procesoTiempo = tk.Label (self.frameMicro, text = str(self.microprocesadores[j].procesos[i].tiempoEjecucion),bg = "gray",fg = "white")
                self.procesoTiempo.grid(row = i, column=2)
                self.procesoBloq = tk.Label (self.frameMicro, text = str(self.microprocesadores[j].procesos[i].tvc),bg = "gray",fg = "white")
                self.procesoBloq.grid(row = i, column=3)
                self.procesoTiempo = tk.Label (self.frameMicro, text = str(self.microprocesadores[j].procesos[i].tb),bg = "gray",fg = "white")
                self.procesoTiempo.grid(row = i, column=4)
                self.procesoBloq = tk.Label (self.frameMicro, text = str(self.microprocesadores[j].procesos[i].tt),bg = "gray",fg = "white")
                self.procesoBloq.grid(row = i, column=5)
                self.procesoTiempo = tk.Label (self.frameMicro, text = str(self.microprocesadores[j].procesos[i].ti),bg = "gray",fg = "white")
                self.procesoTiempo.grid(row = i, column=6)
                self.procesoBloq = tk.Label (self.frameMicro, text = str(self.microprocesadores[j].procesos[i].tf),bg = "gray",fg = "white")
                self.procesoBloq.grid(row = i, column=7)

        vsb = tk.Scrollbar(self.frame_canvasListaMicro, orient="vertical", command=self.frame_canvasListaMicro.yview)

        vsb.grid(row = 1, column=1, sticky='ns')
        self.frame_canvasListaMicro.configure(yscrollcommand=vsb.set)

        self.frame_canvasListaMicro.config(scrollregion=self.frame_canvasListaMicro.bbox("all"))
       
    def interfaz (self):
        
        self.root.config(width=300, height=200)
        
        #Disenio de las letras
        costumFontTitulo = tkFont.Font(family = "Bernard MT", size = 35, weight=tkFont.BOLD)
        costumFontSubTit = tkFont.Font(family = "Times", size = 14)
        
        #Espacio para dividir las cosas en el root
        labelEspacio = tk.Label(self.root).grid(row = 2, sticky='nw' ,column = 0)
        labelEspacioDos = tk.Label(self.root, width = 5, height = 5).grid(row = 3, sticky='nw' ,column = 5)
        

        #Titulo en la interfaz
        labelTitulo = tk.Label(self.root, text = "Despachador", font = costumFontTitulo).grid(row = 0, sticky='nw' ,column = 0)
       

        #Se crea el frame donde se encuentra Quantums y Num de Micros
        frame_DatosIngreso = tk.Frame(self.root, bg = "white")
        frame_DatosIngreso.grid(row = 1, column = 0, sticky = 'nw')
        frame_DatosIngreso.grid_rowconfigure(0, weight = 1)
        frame_DatosIngreso.grid_columnconfigure(0, weight = 1)

        #Se crea el Canvas de Quantums y Num de Micros
        canvasDatos = tk.Canvas(frame_DatosIngreso, bg = "white")
        canvasDatos.grid(row=0, column=0, sticky = "nw")

        #Se crea el siguiente frame donde se guardan las Lables
        frameDatos = tk.Frame(frame_DatosIngreso)

        canvasDatos.create_window((0, 0), window=frameDatos, anchor='nw')

        #Se crea las Labels y Caja de taxto de Quantums 
        labelQuantums = tk.Label(canvasDatos, text = "Quantums", font = costumFontSubTit).grid(row = 0, sticky='nw', column = 0)
        self.entryQuantums = tk.Entry(canvasDatos)
        self.entryQuantums.grid(row = 0, column = 1, sticky='nw')

         #Se crea las Labels y Caja de taxto de Numero de Micros
        labelMicro = tk.Label(canvasDatos, text = "Cantidad de micros" , font = costumFontSubTit).grid(row = 1, sticky='nw' ,column = 0)
        self.entryMicro = tk.Entry(canvasDatos)
        self.entryMicro.grid(row = 1 , column = 1, sticky='nw')

        #Entry para tiempo de bloqueo seleccionado
        self.labelNumDeMicros = tk.Label(canvasDatos, text = "Tiempo de Bloque", font = costumFontSubTit).grid(row = 2, sticky='nw', column = 0)
        self.entryBloque = tk.Entry(canvasDatos)
        self.entryBloque.grid(row = 2, column = 1, sticky='nw')

         #Entry para tiempo de cambio de contexto seleccionado
        self.labelNumDeMicros = tk.Label(canvasDatos, text = "Tiempo Cambio de Contexto", font = costumFontSubTit).grid(row = 3, sticky='nw', column = 0)
        self.entryCambio = tk.Entry(canvasDatos)
        self.entryCambio.grid(row = 3, column = 1, sticky='nw')
        
        #Se creo el boton de Mostrar tabla
        #Llama a funcion de aniadirMicro
        button = ttk.Button(canvasDatos,text ="Mostrar Tabla", command = self.prueba)
        button.grid(row = 4, column = 0, sticky = "nw")

        #Se crea el primer Frame de la lista de procesos
        
        frame_canvas = tk.Frame(self.root, bg = "red", highlightbackground="black" , highlightthickness = 2 )
        frame_canvas.grid(row=3 , column=0,  sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        
        #Se creo el Canvas de la Lista de procesos 
        canvas = tk.Canvas(frame_canvas, bg="gray")
        canvas.grid(row=1, column=0, sticky="news")
        
        #Se crea el Frame que tendra guardado los datos de los Procesos
        frameProcesos = tk.Frame(frame_canvas, bg="gray", width = frame_canvas.winfo_width())
        frameProcesos.grid_columnconfigure(0,weight = 1, pad = 20)
        frameProcesos.grid_columnconfigure(1,weight = 1, pad = 100)
        frameProcesos.grid_columnconfigure(2,weight = 1, pad = 100)
        frameProcesos.grid_columnconfigure(3,weight = 1, pad = 100)
        canvas.create_window((0, 0), window=frameProcesos, anchor='ne')

        #Se creo una ScrollBar para poder mostrar todos los proceso en un espacio compacto
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=1, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        rows = len(self.listaDeProcesos)
        columns = 3

        #Se crea el Lable que muestra el menu de la tabla
        menuDeTabla = tk.Label(frame_canvas, text = "Proceso  Tiempo de Proceso  Tiempo de Entrada  Cantidad de Bloque", bg = "red")
        menuDeTabla.grid(row = 0, column = 0)
        
        #Agrega cada proceso al Frame por Nombre, Tamao, Tiempo de Entrada y Bloqueo
        for i in range(0, rows):
            procesoNom = tk.Label (frameProcesos, text = self.listaDeProcesos[i], bg = "gray",fg = "white")
            procesoNom.grid(row = i, column=0)
            procesoTamanio = tk.Label (frameProcesos, text = self.tamanioDeProceso[i],bg = "gray", fg = "white")
            procesoTamanio.grid(row = i, column=1)
            procesoTiempo = tk.Label (frameProcesos, text = self.tiempoDeEntrada[i],bg = "gray",fg = "white")
            procesoTiempo.grid(row = i, column=2)
            procesoBloq = tk.Label (frameProcesos, text = self.cantidadDeBloqueo[i],bg = "gray",fg = "white")
            procesoBloq.grid(row = i, column=3)
        

        frameProcesos.update_idletasks() 
        canvas.config(scrollregion=canvas.bbox("all"))


        

        button.pack
        self.root.mainloop()


def main():
    
    despachador = Despachador()
    '''
    despachador.lecturaDeArchivo()
    #Todo esto se va leer del txt
    numeroProcesos = 17
    numeroMicros = 10
    
    tiempoBloqueo = 0
    tiempoCambio = 10
    duracionQuantum = 3000
    #Procurar ponerlos en orden de ejecucion
    nombres = ["B", "D", "F", "H", "J", "L", "N", "O", "A", "C", "E", "G", "I", "K", "M", "P", "Z"]
    #Estos deben coincidir con las letras de arriba
    numBloqueos = [2,2,3,4,2,5,2,3,2,2,5,2,3,2,2,4,3]
    tiemposEjecucion = [300,100,500,700,300,3000,50,600,400,50,1000,10,450,100,80,800,500]
    tiemposEntrada = [0,0,0,0,1500,1500,1500,1500,3000,3000,3000,3000,3000,4000,4000,4000,8000]

    for i in range(numeroMicros):
        despachador.aniadirMicroprocesador(i+1)

    despachador.aniadirProcesos(duracionQuantum, numeroProcesos, nombres, tiemposEjecucion, numBloqueos, tiempoBloqueo, tiempoCambio, tiemposEntrada)
    despachador.imprimirEstado()
    '''
    despachador.interfaz()
    



if __name__ == '__main__':
    main()