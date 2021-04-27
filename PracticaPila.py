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