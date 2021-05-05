class Cola(object):

    def __init__(self):
        self.__elementos = []

    def arribo(self, dato):
        self.__elementos.append(dato)

    def atencion(self):
        return self.__elementos.pop(0)

    def colaVacia(self):
        return len(self.__elementos) == 0

    def tamanio(self):
        return len(self.__elementos)

    def enFrente(self):
        return self.__elementos[0]

    def cargaPrioritaria(self, dato):
        self.__elementos.insert(0, dato)

    def moverAlFinal(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato