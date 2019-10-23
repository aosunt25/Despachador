class Procesos:

    def __init__(self, name, tt, tiempoEj, tcc, tvc, tb, ti, tf, tEspera):
        self.name = name
        self.tcc = tcc
        self.tvc = tvc
        self.tb = tb
        self.ti = ti
        self.tt = tt
        self.tf = tf
        self.tiempoEjecucion = tiempoEj
        self.tEspera=tEspera
