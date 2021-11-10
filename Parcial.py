from EstructuraCola import Cola
from EstructuraPila import Pila
from EstructuraLista import Lista

print("Ejercicio 1 Parcial")
print()

personajesStarWars = ['Luke Skywalker', 'Anakin Skywalker', 'Yoda', 'Chewbaca', 'Darth Vader']

def barridoRecursivo(personajes, n):
    if n == len(personajes):
        return 0
    else:
        print(personajes[n])
        return barridoRecursivo(personajes, n+1)

barridoRecursivo(personajesStarWars, 0)

def saberSiYoda(personajes, n):
    if personajes[n] == 'Yoda':
        return 1
    elif n == len(personajes):
        return -1
    else:
        return saberSiYoda(personajes, n+1)

print()
if saberSiYoda(personajesStarWars, 0) != -1:
    print('Yoda esta en el vector')
print()

print('Ejercicio parcial 2')
print()

class Notificacion(object):
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

def notificacionSmarthphone():
    cola = Cola()
    colaAux = Cola()
    pila = Pila()

    cola.arribo(Notificacion(1, 'Facebook', 'Te escribieron'))
    cola.arribo(Notificacion(2, 'Instagram', 'Nueva foto'))
    cola.arribo(Notificacion(3, 'Facebook', 'Cumpleanios'))
    cola.arribo(Notificacion(6, 'Twitter', 'Revisa estas imagenes'))
    cola.arribo(Notificacion(12, 'Twitter', 'Comentario nuevo'))
    cola.arribo(Notificacion(22, 'Twitter', 'Aprende Python'))
    cola.arribo(Notificacion(20, 'Instagram', 'Actualizate'))

    # Punto a
    while not cola.colaVacia():
        if cola.enFrente().aplicacion == 'Facebook':
            cola.atencion()
        # Punto B
        elif cola.enFrente().aplicacion == 'Twitter' and 'Python' in cola.enFrente().mensaje:
            print('App: ',cola.enFrente().aplicacion,', mensaje:' , cola.enFrente().mensaje)
            colaAux.arribo(cola.atencion())
        # Punto C
        elif cola.enFrente().aplicacion == 'Instagram':
            pila.apilar(cola.enFrente())
            colaAux.arribo(cola.atencion())
        else:
            colaAux.arribo((cola.atencion()))

    while not colaAux.colaVacia():
        cola.arribo(colaAux.atencion())

    while not pila.pilaVacia():
        print('Elementos de la pila: ', pila.elementoUltimo().aplicacion, pila.desapilar().mensaje)

notificacionSmarthphone()

print()
print('Ejercicio 3')
print()

def avengersEjercicio():
    lista = Lista()
    datosAvengers = ['Iron Man', 'Nick Fury', 'Capitan America', 'Thor', 'Scalet Witch']
    for elementos in datosAvengers:
        lista.insertar(elementos)

    # Punto A
    posThor = lista.busqueda('Thor')
    if posThor != -1:
        print('Thor se encuentra en la pos', posThor)
    print()

    # Punto B
    posScarlet = lista.busqueda('Scalet Witch')
    if posScarlet != -1:
        lista.modificar_elemento(posScarlet, 'Scarlet Witch')
    print()

    # Punto C
    datosAux = ['Black Widow', 'Hulk', 'Rocket Racoon', 'Loki']
    listaAux = Lista()

    for elementos in datosAux:
        listaAux.insertar(elementos)

    for i in range (0, listaAux.tamanio()):
        lista.insertar(listaAux.obtener_elemento(i))

    # Punto D

    lista.barrido() # Barrido ascendente
    print()
    for i in reversed(range(lista.tamanio())): # Barrido descendente
        print(lista.obtener_elemento(i))

    print()
    # Punto E
    print('Personaje posicion 7', lista.obtener_elemento(6))

    print()
    # Punto F
    for i in range (0, lista.tamanio()):
        if lista.obtener_elemento(i)[0] == 'C' or lista.obtener_elemento(i)[0] == 'S':
            print('Personaje con C o S:', lista.obtener_elemento(i))

    print()
    # Punto G
    listaDatosCambiados = Lista()
    listaDatosCambiadosAnio = Lista()
    datosCambiados = [{'nombre' : 'Iron Man', 'anio' : 1952, 'esHeroe' : True},
                      {'nombre' : 'Nick Fury', 'anio' : 1974, 'esHeroe' : True},
                      {'nombre': 'Black Widow', 'anio': 1968, 'esHeroe': True},
                      {'nombre': 'Capitan America', 'anio': 1980, 'esHeroe': True},
                      {'nombre': 'Thor', 'anio': 1982, 'esHeroe': False},
                      {'nombre': 'Hulk', 'anio': 1958, 'esHeroe': True},
                      {'nombre': 'Rocket Racoon', 'anio': 1986, 'esHeroe': True},
                      {'nombre': 'Loki', 'anio': 1973, 'esHeroe': False}
                      ]
    for datos in datosCambiados:
        listaDatosCambiados.insertar(datos, 'nombre')
        listaDatosCambiadosAnio.insertar(datos, 'anio')

    print('Barrido listado por nombre')
    listaDatosCambiados.barrido()

    print()
    print('Barrido listado por anio de aparicion:')
    listaDatosCambiadosAnio.barrido()




avengersEjercicio()