from grafo import Grafo

dioses = Grafo(dirigido=False)

dioses.insertar_vertice('Urano', data={'descripcion' : ''})
dioses.insertar_vertice('Cronos', data={'descripcion' : ''})
dioses.insertar_vertice('Rhea', data={'descripcion' : ''})
dioses.insertar_vertice('Zeus', data={'descripcion' : ''})
dioses.insertar_vertice('Hades', data={'descripcion' : ''})
dioses.insertar_vertice('Demeter', data={'descripcion' : ''})
dioses.insertar_vertice('Atenea', data={'descripcion' : ''})
dioses.insertar_vertice('Apollo', data={'descripcion' : ''})
dioses.insertar_vertice('Persefone', data={'descripcion' : ''})

dioses.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['pareja']})
dioses.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Zeus', 'Hades', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Zeus', 'Atenea', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Demeter', 'Persefone', data={'relacion': ['madre', 'hijo']})
origen = dioses.buscar_vertice('Cronos')
# dioses.barrido_amplitud(origen)
print()

# C
def hijosDeUnDios(nombre):
    for i in range (dioses.inicio.tamanio()):
        dios = dioses.inicio.obtener_elemento(i)
        if dios['info'] == nombre:
            for j in range(dios['aristas'].tamanio()):
                arista = dios['aristas'].obtener_elemento(j)
                if len(arista['data']['relacion']) > 1:
                    if arista['data']['relacion'][1] == 'hijo':
                        print(arista['destino'])

# hijosDeUnDios('Zeus')

# D
def infoDios(nombre):
    for i in range (dioses.inicio.tamanio()):
        dios = dioses.inicio.obtener_elemento(i)
        if dios['info'] == nombre:
            for j in range(dios['aristas'].tamanio()):
                arista = dios['aristas'].obtener_elemento(j)
                if len(arista['data']['relacion']) == 1:
                    print('Hermano/s:', arista['destino'])
                if len(arista['data']['relacion']) == 2:
                    if arista['data']['relacion'][0] == 'hijo':
                        print('Padre:', arista['destino'])
                    else:
                        print('Hijo/a:', arista['destino'])

infoDios('Zeus')
print()

# E
def relacionDosDioses(nombre1, nombre2):
    origen = dioses.buscar_vertice(nombre1)
    dios = dioses.inicio.obtener_elemento(origen)

    for i in range (dios['aristas'].tamanio()):
        arista = dios['aristas'].obtener_elemento(i)
        if arista['destino'] == nombre2:
            print(nombre1, 'se relaciona con', nombre2,
            'y es su', arista['data']['relacion'][0])

# relacionDosDioses('Zeus', 'Cronos')

# F
def caminoCorto(nombre1, nombre2):
    vertice_origen = dioses.buscar_vertice(nombre1)
    vertice_destino = dioses.buscar_vertice(nombre2)

    camino = dioses.dijkstra(vertice_origen, vertice_destino)

    destino = nombre2
    costo = None
    while(not camino.pila_vacia()):
        dato = camino.desapilar()
        if(dato[1][0] == destino):
            if(costo is None):
                costo = dato[0]
            print(dato[1][0])
            destino = dato[1][1]
    print('El camino mas rapido es de costo:', costo)

caminoCorto('Zeus', 'Atenea')
print()

# G
def barridos():
    dioses.barrido_amplitud()
    print()
    dioses.barrido_profundidad()
    print()

# barridos()

# H
def madreDeUnDios(nombre):
    for i in range (dioses.inicio.tamanio()):
        dios = dioses.inicio.obtener_elemento(i)
        if dios['info'] == nombre:
            for j in range(dios['aristas'].tamanio()):
                arista = dios['aristas'].obtener_elemento(j)
                if len(arista['data']['relacion']) > 1:
                    if arista['data']['relacion'][1] == 'madre':
                        print('La madre de', nombre, 'es:', arista['destino'])

madreDeUnDios('Persefone')
print()

# I
def padreDeUnDios(nombre):
    for i in range (dioses.inicio.tamanio()):
        dios = dioses.inicio.obtener_elemento(i)
        if dios['info'] == nombre:
            for j in range(dios['aristas'].tamanio()):
                arista = dios['aristas'].obtener_elemento(j)
                if len(arista['data']['relacion']) > 1:
                    if arista['data']['relacion'][1] == 'padre':
                        print(arista['destino'])

def ancestros(nombre):
    origen = dioses.buscar_vertice(nombre)
    dios = dioses.inicio.obtener_elemento(origen)
    for i in range (dios['aristas'].tamanio()):
        arista = dios['aristas'].obtener_elemento(i)
        if len(arista['data']['relacion']) > 1:
            if arista['data']['relacion'][1] == 'padre' or arista['data']['relacion'][1] == 'madre':
                nombre = arista['destino']
                madreDeUnDios(nombre)
                padreDeUnDios(nombre)

print('Ancestros:')
ancestros('Zeus')
print()

# J
def nietosCronos(nombre):
    origen = dioses.buscar_vertice(nombre)
    dios = dioses.inicio.obtener_elemento(origen)
    for i in range (dios['aristas'].tamanio()):
        arista = dios['aristas'].obtener_elemento(i)
        if len(arista['data']['relacion']) > 1:
            if arista['data']['relacion'][1] == 'hijo':
                nombre = arista['destino']
                hijosDeUnDios(nombre)

print('Nietos de Cronos:')
nietosCronos('Cronos')
print()

# K
print('Hijos de Tea:')
hijosDeUnDios('Tea')

