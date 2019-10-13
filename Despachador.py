import math

class Microprocesador():
    procesos = []
    #Class Attribute 
    def __init__(self, num):
        self.num = num

    def anadirProceso(self, proceso):
        self.procesos.append(proceso)


class Proceso():

    #Class Attribute 
    def __init__(self, name,tcc, tvc, tiempoEj, tb, ti, tt, tf):
        self.name = name
        self.tcc = tcc
        self.tvc = tvc
        self.tb = tb
        self.ti = ti
        self.tt = tt
        self.tf = tf
        self.tiempoEjecucion = tiempoEj


class Despachador():
    pass
    microprocesadores = []

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
                proceso = Proceso(names[i], 0, tvc, tiemposEjecucion[i], tb, 0, tt, tt)

                self.microprocesadores[0].procesos.append(proceso)

            else:
                #AQUI SE DEBE CHECAR QUE MICRO TIENE MENOS TIEMPO FINAL EN SU ULTIMA POSICION DE PROCESOS .TF
                tt = duracionCambio + tiemposEjecucion[i] + tvc + numBloqueos[i]*duracionBloqueo
                ti = self.microprocesadores[0].procesos[i-1].tf
                proceso = Proceso(names[i], duracionCambio, tvc, tiemposEjecucion[i], tb, ti, tt, ti + tt)
                self.microprocesadores[0].procesos.append(proceso)

        #Aqui checar si hay mas de un micro
    
    def imprimirEstado(self):
        
        for i in range(len(self.microprocesadores)):
            print( "Microprocesador " + str(i+1))
            print( " Proceso " + " TCC    "+" TE    "+" TVC    "	+"  TB   "	+ "    TT   "	+"     TI   "+ 	"     TF   ")
            for j in range(len(self.microprocesadores[i].procesos)):
                print("      " +self.microprocesadores[i].procesos[j].name + "      " +  str(self.microprocesadores[i].procesos[j].tcc) + "      " +str(self.microprocesadores[i].procesos[j].tiempoEjecucion) +"     " + str(self.microprocesadores[i].procesos[j].tvc) + "      " +str(self.microprocesadores[i].procesos[j].tb) +"     " + str(self.microprocesadores[i].procesos[j].tt) +"    " + str(self.microprocesadores[i].procesos[j].ti) +"   " + str(self.microprocesadores[i].procesos[j].tf))

def main():
    despachador = Despachador()

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
    despachador.imprimirEstado()



if __name__ == '__main__':
    main()