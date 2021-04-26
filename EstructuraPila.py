class Pila(object):

    def __init__(self):
        self.__elementos = []

    def apilar(self, dato):
        self.__elementos.append(dato)

    def desapilar(self):
        return self.__elementos.pop()

    def pilaVacia(self):
        return len(self.__elementos) == 0

    def tamanio(self):
        return len(self.__elementos)

    def elementoUltimo(self):
        return self.__elementos[-1]