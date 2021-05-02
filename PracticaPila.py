from EstructuraPila import Pila


# Ejercicio 14

numeros = [1, 4, 2, 12, 6]

print("Ejercicio numero 14: ")
def pilaOrdenada():
    pila = Pila()
    pilaAux = Pila()
    for i in range(0, 5):
        numero = numeros[i]

        if pila.pilaVacia():
            pila.apilar(numero)
        else:
            if pila.elementoUltimo() >= numero:
                    pila.apilar(numero)
            else:
                while not pila.pilaVacia() and pila.elementoUltimo() < numero:
                    pilaAux.apilar(pila.desapilar())
                pila.apilar(numero)

            while not pilaAux.pilaVacia():
                pila.apilar(pilaAux.desapilar())

    while not pila.pilaVacia():
        print(pila.desapilar())

pilaOrdenada()

print()

print("Ejercicio numero 16: ")
# Ejercicio 16
def starWarsPersonajes():
    pilaForce = Pila()
    pilaEmpire = Pila()
    pilaCoincide = Pila()

    theForceAw = ["Luke Skywalker", "Rey", "Kylo Ren", "Han Solo"]
    empireStrike = ["Yoda", "Darth Vader", "Luke Skywalker", "Leia Organa", "Han Solo"]

    for elementos in theForceAw:
        pilaForce.apilar(elementos)

    for elementos in empireStrike:
        pilaEmpire.apilar(elementos)

    while not pilaEmpire.pilaVacia():
        if pilaForce.desapilar() == pilaEmpire.elementoUltimo():
            pilaCoincide.apilar(pilaEmpire.desapilar())

        if pilaForce.pilaVacia():
            pilaEmpire.desapilar()
            for i in theForceAw:
                pilaForce.apilar(i)

    while not pilaCoincide.pilaVacia():
        print(pilaCoincide.desapilar())

starWarsPersonajes()
print()

# Ejercicio 22

print("Ejercicio numero 22: ")
print()
class Misiones(object):
    def __init__(self, planeta, captura, recompensa):
        self.planeta = planeta
        self.captura = captura
        self.recompensa = recompensa

def theMandalorian():
    naveBoba = Pila()
    naveDin = Pila()
    pilaAux = Pila()

    mision = Misiones("Anoat", "Lando", 12000)
    naveDin.apilar(mision)
    mision = Misiones("Bespin", "Han Solo", 25000)
    naveBoba.apilar(mision)
    mision = Misiones("Corellia", "Ahsoka", 5400)
    naveBoba.apilar(mision)
    mision = Misiones("Atollon", "Yoda", 15000)
    naveDin.apilar(mision)
    mision = Misiones("Terra", "Chewbaca", 17500)
    naveBoba.apilar(mision)

    # Punto A
    print("Boba Fett visito: ")
    while not naveBoba.pilaVacia():
        pilaAux.apilar(naveBoba.desapilar())
    while not pilaAux.pilaVacia():
        print(pilaAux.elementoUltimo().planeta)
        naveBoba.apilar(pilaAux.desapilar())
    print()
    print("Din Djarin visito: ")
    while not naveDin.pilaVacia():
        pilaAux.apilar(naveDin.desapilar())
    while not pilaAux.pilaVacia():
        print(pilaAux.elementoUltimo().planeta)
        naveDin.apilar(pilaAux.desapilar())
    print()

    # Punto B
    creditosBoba = 0
    creditosDin = 0
    while not naveBoba.pilaVacia():
        creditosBoba += naveBoba.elementoUltimo().recompensa
        pilaAux.apilar(naveBoba.desapilar())
    while not pilaAux.pilaVacia():
        naveBoba.apilar(pilaAux.desapilar())

    while not naveDin.pilaVacia():
        creditosDin += naveDin.elementoUltimo().recompensa
        pilaAux.apilar(naveDin.desapilar())
    while not pilaAux.pilaVacia():
        naveDin.apilar(pilaAux.desapilar())
    print("Din Djarin recaudo " , creditosDin , " creditos")
    print("Boba Fett recaudo " , creditosBoba , " creditos")
    if creditosDin > creditosBoba:
        print("Din Djarin obtuvo mas creditos galacticos")
    else:
        print("Boba Fett obtuvo mas creditos galacticos")
    print()

    # Punto C
    contHan = 0
    encontroHan = False
    while not naveDin.pilaVacia():
        pilaAux.apilar(naveDin.desapilar())
    while not pilaAux.pilaVacia():
        contHan += 1
        if pilaAux.elementoUltimo().captura == "Han Solo":
            encontroHan = True
            misionHan = contHan
        naveDin.apilar(pilaAux.desapilar())
    if encontroHan:
        print("Han Solo fue capturado en la mision " , misionHan , " de Din Djarin")

    contHan = 0
    while not naveBoba.pilaVacia():
        pilaAux.apilar(naveBoba.desapilar())
    while not pilaAux.pilaVacia():
        contHan += 1
        if pilaAux.elementoUltimo().captura == "Han Solo":
            encontroHan = True
            misionHan = contHan
        naveBoba.apilar(pilaAux.desapilar())
    if encontroHan:
        print("Han Solo fue capturado en la mision " , misionHan , " de Boba Fett")
    print()

    # Punto D
    contDinCapturas = 0
    contBobaCapturas = 0
    while not naveBoba.pilaVacia():
        if naveBoba.elementoUltimo().captura != "":
            contBobaCapturas += 1
        pilaAux.apilar(naveBoba.desapilar())
    while not pilaAux.pilaVacia():
        naveBoba.apilar(pilaAux.desapilar())

    while not naveDin.pilaVacia():
        if naveDin.elementoUltimo().captura != "":
            contDinCapturas += 1
        pilaAux.apilar(naveDin.desapilar())
    while not pilaAux.pilaVacia():
        naveDin.apilar(pilaAux.desapilar())

    print("Din Djarin realizo: ", contDinCapturas, " capturas")
    print("Boba Fett realizo: ", contBobaCapturas, " capturas")

theMandalorian()

# Ejercicio 24
print()
print("Ejercicio 24:")
print()

class MarvelPersonajes(object):
    def __init__(self, personaje, cantPeliculas):
        self.personaje = personaje
        self.cantPeliculas = cantPeliculas

def marvel():
    pila = Pila()
    pilaMasDeCinco = Pila()
    pilaCDG = Pila()


    pila.apilar(MarvelPersonajes("Iron Man", 9))
    pila.apilar(MarvelPersonajes("Viuda Negra", 3))
    pila.apilar(MarvelPersonajes("Hulk", 6))
    pila.apilar(MarvelPersonajes("Capitan America", 7))
    pila.apilar(MarvelPersonajes("Rocket Raccoon", 0))

    cantPelisViuda = -1
    contPersonajes = 0
    posRocketRaccoon = -1
    posGroot = -1
    letraCDG = ['C', 'D', 'G']

    while not pila.pilaVacia():
        personajeActual = pila.desapilar()
        contPersonajes += 1

        # A
        if personajeActual.personaje == "Rocket Raccoon":
            posRocketRaccoon = contPersonajes
        elif personajeActual.personaje == "Groot":
            posGroot = contPersonajes

        # B
        if personajeActual.cantPeliculas > 5:
            pilaMasDeCinco.apilar(personajeActual)

        # C
        if personajeActual.personaje == "Viuda Negra":
            cantPelisViuda = personajeActual.cantPeliculas

        # D
        if personajeActual.personaje[0] == letraCDG[0] or personajeActual.personaje[0] == letraCDG[1] or personajeActual.personaje[0] == letraCDG[2]:
            pilaCDG.apilar(personajeActual)

    if posRocketRaccoon != -1:
        print("Se encontro a Rocket Raccoon en la posicion: ", posRocketRaccoon)
    else:
        print("No se encontro a Rocket Raccoon")
    if posGroot != -1:
        print("Se encontro a Groot en la posicion: ", posGroot)
    else:
        print("No se encontro a Groot")

    print()
    print("Los personajes con mas de 5 peliculas son:")
    while not pilaMasDeCinco.pilaVacia():
        personajeActual = pilaMasDeCinco.desapilar()
        print("Personaje:", personajeActual.personaje, "presente en", personajeActual.cantPeliculas, "peliculas")

    print()
    if cantPelisViuda != -1:
        print("La Viuda Negra participo en:", cantPelisViuda, "peliculas")

    print()
    print("Personajes que comienzan con la letra C, D o G:")
    while not pilaCDG.pilaVacia():
        personajeActual = pilaCDG.desapilar()
        print(personajeActual.personaje)

marvel()