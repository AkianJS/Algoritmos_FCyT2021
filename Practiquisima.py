from EstructuraPila import Pila
#
# def ejercicioRecursivo7(num, n):
#     if n == num:
#         return 1/n
#     else:
#         return 1/n + ejercicioRecursivo7(num, n+1)
#
# print(ejercicioRecursivo7(4, 1))

'''Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejem-
plo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del

objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras ex-
tras, no se pueden utilizar métodos de ordenamiento.'''

class Objeto(object):
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

def ejercicioPilaPractica():
    pila = Pila()
    pilaAux = Pila()
    pilaOrdenada = Pila()

    pila.apilar(Objeto('monitor', 3))
    pila.apilar(Objeto('mouse', 0.63))
    pila.apilar(Objeto('telefono', 1.5))
    pila.apilar(Objeto('teclado', 0.400))
    pila.apilar(Objeto('silla', 7))
    pila.apilar(Objeto('mesa', 30))

    for i in range (0, pila.tamanio()):
        while not pila.pilaVacia():
            aux = pila.desapilar()
            if pilaOrdenada.pilaVacia():
                pilaOrdenada.apilar(aux)
            else:
                if pilaOrdenada.elementoUltimo().peso >= aux.peso:
                    pilaOrdenada.apilar(aux)
                else:
                    while not pilaOrdenada.pilaVacia() and pilaOrdenada.elementoUltimo().peso < aux.peso:
                        pilaAux.apilar(pilaOrdenada.desapilar())
                    pilaOrdenada.apilar(aux)

                while not pilaAux.pilaVacia():
                    pilaOrdenada.apilar(pilaAux.desapilar())


    while not pilaOrdenada.pilaVacia():
        print(pilaOrdenada.desapilar().peso)

ejercicioPilaPractica()

from lista import Lista

jedis = Lista()
file = open('jedis.txt')

lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    # print(jedi)
    jedi[7] = float(jedi[7].split('\n')[0])
    # print(jedi)
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1]
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5]
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = jedi[7]
    if(len(jedi) > 8):
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] = jedi[9]
    jedis.insertar(jedi_data, 'name')


file.close()