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
    accept = True
    tiemposEntrada=[]
    aux = []
    tiEntrada = False
    noMoreZeros = False
    des = False

    rows = 0

    frame_canvasMicro= tk.Frame()
    canvasMicro= tk.Canvas()
    frameMicro = tk.Frame()
    frame_canvasListaMicro = tk.Frame()

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
        for j in range(len(self.microprocesadores)):
                proceso = Procesos(" ",0,0,0,0,0,0,0,0)
                self.microprocesadores[j].procesos.append(proceso)
            
        for i in range(num):
            self.des = False
            print("AQUI")
            print(names[i])
            print(tEntrada[i])
            self.tiEntrada = True
            self.tiempoMenor = 100000
            self.accept = True
            tvc = ((math.ceil(tiemposEjecucion[i] / float(duracionQuantum))) - 1) * duracionCambio
            tb = numBloqueos[i]*duracionBloqueo
            
            if len(self.microprocesadores) == 1:
                print(self.microprocesadores[0].procesos[i].tf) 
                print(tEntrada[i])
                if self.microprocesadores[0].procesos[i].tf >= tEntrada[i]:
                    if i == 0:
                        tt = tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                        tcc = 0
                        ti = 0
                    else:
                        tt = duracionCambio + tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                        ti = self.microprocesadores[0].procesos[i].tf
                        tcc = duracionCambio
                    proceso = Procesos(names[i], tt, tiemposEjecucion[i], tcc,tvc, tb, ti, ti + tt,0)
                    self.microprocesadores[0].procesos.append(proceso)
                else:
                    print("Holi")
                    ti = self.microprocesadores[0].procesos[i].tf
                    proceso = Procesos("Descanso", tEntrada[i] - ti,0,0,0,0,ti,tEntrada[i],0)
                    self.microprocesadores[0].procesos.append(proceso)
                    num = num +1
                    self.des = True
            else:
                #En caso de que se requiera poner descansos

                for k in range(len(self.microprocesadores)):
                    lene = len(self.microprocesadores[k].procesos)
                    if self.microprocesadores[k].procesos[lene-1].tf < tEntrada[i]:
                        lene = len(self.microprocesadores[k].procesos)
                        ti = self.microprocesadores[k].procesos[lene-1].tf
                        proceso = Procesos("Descanso", tEntrada[i] - ti,0,0,0,0,ti,tEntrada[i],0)
                        self.noMoreZeros = True
                        self.microprocesadores[k].procesos.append(proceso)
                        num = num +1

                #Fin de poner descansos
                self.noMoreZeros = True
                for j in range(len(self.microprocesadores)):
                    lene = len(self.microprocesadores[j].procesos)
                    if self.microprocesadores[j].procesos[lene-1].tf == 0:
                        self.noMoreZeros = False
                        break

                for k in range(len(self.microprocesadores)):
                    #print("LENEEEEEEE")
                    lene = len(self.microprocesadores[k].procesos)
                    lene2 = len(self.microprocesadores[0].procesos)
                    
                    self.index = 0
                    self.tiempoMenor = self.microprocesadores[0].procesos[lene2-1].tf
                    #Obtener el menor tiempo de ejecucion
                    if self.tiempoMenor> self.microprocesadores[k].procesos[lene-1].tf and self.microprocesadores[k].procesos[lene-1].tf >= tEntrada[i]:
                        print("Tiempo ")
                        print(self.tiempoMenor)
                        print(self.microprocesadores[k].procesos[lene-1].tf)
                        self.tiempoMenor = self.microprocesadores[k].procesos[lene-1].tf
                        self.index = k
                        if self.microprocesadores[k].procesos[lene-1].tf == 0:
                            self.index = k
                            break
                        
                        for j in range(k, len(self.microprocesadores)):
                            lene = len(self.microprocesadores[j].procesos)
                            if self.microprocesadores[j].procesos[lene-1].tf < self.tiempoMenor:
                                self.tiempoMenor = self.microprocesadores[j].procesos[lene-1].tf
                                self.index = j
                        if self.noMoreZeros == True:
                            break
                


                #Crear el proceso 
                print("INDEXXXXXX")
                print(self.tiempoMenor)
                print(self.index)
                lene = len(self.microprocesadores[self.index].procesos)
                if len(self.microprocesadores[self.index].procesos) == 1 :
                    tt = tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                    tcc = 0
                    ti = 0
                elif self.microprocesadores[self.index].procesos[lene-1].name == "Descanso":
                    tt = tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                    ti = self.microprocesadores[self.index].procesos[lene-1].tf
                    tcc = 0
                else:
                    tt = duracionCambio + tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                    ti = self.microprocesadores[self.index].procesos[lene-1].tf
                    tcc = duracionCambio
                proceso = Procesos(names[i], tt, tiemposEjecucion[i], tcc,tvc, tb, ti, ti + tt,0)
                self.microprocesadores[self.index].procesos.append(proceso)
                    


    def imprimirEstado(self):
        for i in range(len(self.microprocesadores)):
            print( "Microprocesador " + str(i+1))
            print( " Proceso " + " TCC    "+" TE    "+" TVC    "	+"  TB   "	+ "    TT   "	+"     TI   "+ 	"     TF   ")
            for j in range(len(self.microprocesadores[i].procesos)):
                if self.microprocesadores[i].procesos[j].tEspera > 0:
                    aux = self.microprocesadores[i].procesos[j].tEspera

                if self.microprocesadores[i].procesos[j].name != " ":
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

        self.microprocesadores.clear()
        self.tiempoMenor = 0
        self.tiempoEn =0
        self.index = 0
        self.counter = 0

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
        self.imprimirEstado()

        self.frame_canvasListaMicro.destroy()
        self.frame_canvasMicro.destroy()
        self.procesoNom.destroy()
        self.procesoTCC.destroy() 
        self.procesoTiempo.destroy() 
        self.procesoBloq.destroy() 
        self.canvasMicro.destroy()
        self.frameMicro.destroy()

        self.frame_canvasListaMicro = tk.Frame(self.root, bg = "white", highlightbackground="black" , highlightthickness = 2)
        self.frame_canvasListaMicro.grid(row=3 , column=7,  sticky='nw')
        self.frame_canvasListaMicro.grid_rowconfigure(0, weight=1)
        self.frame_canvasListaMicro.grid_columnconfigure(0, weight=1)

        canvas = tk.Canvas(self.frame_canvasListaMicro, bg="white")
        canvas.grid(row=1, column=0, sticky="news")

        frame = tk.Frame(self.frame_canvasListaMicro, bg="white")
        

        vsb = tk.Scrollbar(self.frame_canvasListaMicro, orient="vertical", command=canvas.yview)
        vsb.grid(row = 1, column=1, sticky='ns')

        canvas.configure(yscrollcommand=vsb.set)
        
        canvas.create_window((0, 0), window=frame, anchor='nw')

        menuDeTablaMicros = tk.Label(self.frame_canvasListaMicro, text = "Proceso	    TCC	    TE	    TVC	    TB	    TT	    TI	    TF       llllllllllllllll", bg = "white", fg="white")
        menuDeTablaMicros.grid(row = 0, column = 0)
        
    
        for j in range(0,len(self.microprocesadores)):

            #Se crea el primer Frame de la lista de Micros  
            self.frame_canvasMicro = tk.Frame(frame, bg = "white", highlightbackground="black" , highlightthickness = 2)
            self.frame_canvasMicro.grid(row=j , column=0,  sticky='nw')
            self.frame_canvasMicro.grid_rowconfigure(0, weight=1)
            self.frame_canvasMicro.grid_columnconfigure(0, weight=1)
            
            
            #Se creo el Canvas de la Lista de Micros 
            self.canvasMicro = tk.Canvas(self.frame_canvasMicro, bg="gray")
            self.canvasMicro.grid(row=1, column=0, sticky="news")
            
            #Se crea el Frame que tendra guardado los datos de los Micros
            self.frameMicro = tk.Frame(self.frame_canvasMicro, bg="gray")

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

            menuDeTablaMicros = tk.Label(self.frame_canvasMicro, text = "Proceso	 TCC	  TE	     TVC	      TB	        TT	           TI	           TF        ", bg = "red")
            menuDeTablaMicros.grid(row = 0, column = 0)


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

            self.frameMicro.update_idletasks() 
            self.canvasMicro.config(scrollregion=self.canvasMicro.bbox("all"))

       
        self.frame_canvasListaMicro.update_idletasks() 
        canvas.config(scrollregion=canvas.bbox("all"))
        
       
    def interfaz (self):
        
        self.root.config(width=700, height=200)
        
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
    despachador.lecturaDeArchivo()
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