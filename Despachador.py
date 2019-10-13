class Despachador:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def lecturaDeArchivo():
        archivo = open("proceso.txt", "r")
        if archivo.mode == 'r':
           linea=archivo.readlines()
           for x in linea:
                print(x)



def main():
    Despachador.lecturaDeArchivo()

if __name__== '__main__':
    main()