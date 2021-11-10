from EstructuraCola import Cola
from EstructuraPila import Pila
from heap import HeapMax

# Ejercicio 11

print("Ejercicio 11")
print()

class PjStarsWars(object):
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

def colaStarsWars():
    cola = Cola()
    cola.arribo(PjStarsWars("Han Solo", "Corelia"))
    cola.arribo(PjStarsWars("Luke Skywalker", "Polis Massa"))
    cola.arribo(PjStarsWars("Greedo", "Rodia"))
    cola.arribo(PjStarsWars("Bail Organa", "Alderaan"))
    cola.arribo(PjStarsWars("Yoda", "Dagobah"))
    cola.arribo(PjStarsWars("Jar Jar Binks", "Naboo"))
    cola.arribo(PjStarsWars("Teebo", "Endor"))
    cola.arribo(PjStarsWars("Watto", "Tatooine"))

    controlCola = 0
    while controlCola < cola.tamanio() and not cola.colaVacia():
        # Punto C
        if cola.enFrente().nombre == "Yoda":
            cola.arribo(PjStarsWars("Jabba", "Nal Hutta"))

        actual = cola.moverAlFinal()

        # Punto A
        if actual.planeta == "Alderaan" or actual.planeta == "Endor" or actual.planeta == "Tatooine":
            print("Proveniente de", actual.planeta, ":", actual.nombre)

        # Punto B
        if actual.nombre == "Luke Skywalker" or actual.nombre == "Han Solo":
            print("Planeta de origen de", actual.nombre, ":", actual.planeta)

        # Punto D
        if actual.nombre == "Jar Jar Binks":
            cola.atencion()

        controlCola += 1

    while not cola.colaVacia():
        print(cola.atencion().nombre)

colaStarsWars()

print()
# Ejercicio 12
print("Ejercicio 12")
print()

def colaOrdenada():
    cola = Cola()
    cola2 = Cola()
    colaMezcla = Cola()
    numeros = [1, 2, 8, 11, 21, 22, 25, 29]
    numeros2 = [3, 4, 6, 9, 15, 28]

    for elementos in numeros:
        cola.arribo(elementos)

    for elementos in numeros2:
        cola2.arribo(elementos)

    while not cola.colaVacia() and not cola2.colaVacia():
        numeroDeCola = cola.enFrente()
        numeroDeCola2 = cola2.enFrente()

        if numeroDeCola <= numeroDeCola2:
            colaMezcla.arribo(cola.atencion())

        if numeroDeCola2 <= numeroDeCola:
            colaMezcla.arribo(cola2.atencion())

    while not cola.colaVacia():
        colaMezcla.arribo(cola.atencion())
    while not cola2.colaVacia():
        colaMezcla.arribo(cola2.atencion())

    while not colaMezcla.colaVacia():
        print(colaMezcla.atencion())

colaOrdenada()

print()
# Ejercicio 16
print("Ejercicio 16")
print()


def colaPrioridad():
    cola = HeapMax()
    cola.arribo('Empleado 1', 1)
    cola.arribo('Empleado 2', 1)
    cola.arribo('Empleado 3', 1)

    cola.arribo('Staff TI 1', 2)
    cola.arribo('Staff TI 2', 2)
    cola.arribo('Gerente 1', 3)

    cola.arribo('Empleado 4', 1)
    cola.arribo('Empleado 5', 1)
    cola.arribo('Gerente 2', 3)

    while not cola.vacio():
        print(cola.atencion())

colaPrioridad()

print()
# Ejercicio 22
print("Ejercicio 22")
print()

class MarvelPersonajes(object):
    def __init__(self, nombre, superheroe, sexo):
        self.nombre = nombre
        self.superheroe = superheroe
        self.sexo = sexo

def colaMarvelPersonajes():
    cola = Cola()
    cola.arribo(MarvelPersonajes("Tony Stark", "iron Man", "M"))
    cola.arribo(MarvelPersonajes("Steve Rogers", "Capitan America", "M"))
    cola.arribo(MarvelPersonajes("Natasha Romanoff", "Viuda Negra", "F"))
    cola.arribo(MarvelPersonajes("Carol Danvers", "Capitana Marvel", "F"))
    cola.arribo(MarvelPersonajes("James Rhodes", "Maquina de Guerra", "M"))
    cola.arribo(MarvelPersonajes("Ivan Vanko", "latigazo", "M"))
    cola.arribo(MarvelPersonajes("Scott Lang", "Ant-Man", "M"))
    cola.arribo(MarvelPersonajes("Daisy Johnson", "Temblores", "F"))

    nombreCapitanaMarvel = None
    carolsDanvers = None
    scottSuperheroe = None
    pjsFemeninos = []
    pjsMasculinos = []
    pjsEmpiezanConS = []

    while not cola.colaVacia():
        pjActual = cola.atencion()


        # Punto A
        if pjActual.superheroe == "Capitana Marvel":
            nombreCapitanaMarvel = pjActual.nombre

        # Punto B
        if pjActual.sexo == "F":
            pjsFemeninos.append(pjActual.nombre)

        # Punto C
        if pjActual.sexo == "M":
            pjsMasculinos.append(pjActual.nombre)

        # Punto D
        if pjActual.nombre == "Scott Lang":
            scottSuperheroe = pjActual.superheroe

        # Punto E
        if pjActual.nombre[0] == "S":
            pjsEmpiezanConS.append(pjActual.nombre)

        # Punto F
        if pjActual.nombre == "Carol Danvers":
            carolDanvers = "Capitana Marvel"

    if nombreCapitanaMarvel != None:
        print("Nombre de Capitana Marvel:", nombreCapitanaMarvel)

    print()
    print("Personajes femeninos: ")
    for elementos in pjsFemeninos:
        print(elementos)

    print()
    print("Personajes masculinos: ")
    for elementos in pjsMasculinos:
        print(elementos)

    print()
    if scottSuperheroe != None:
        print("El nombre de superheroe de Scott Lang es:", scottSuperheroe )

    print()
    print("Personajes que comienzan con la letra S")
    for elementos in pjsEmpiezanConS:
        print(elementos)

    print()
    if carolsDanvers != None:
        print("Carol Danvers se encuentra en la cola y su nombre de superheroe es:", carolDanvers)

colaMarvelPersonajes()