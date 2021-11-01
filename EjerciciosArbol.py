from arbol_binario import Arbol
from EstructuraLista import Lista

# Ejercicio 5
def ejercicio5():
    arbol = Arbol()

    #  Punto A, campo booleano
    personajes = [{"nombre" : "Capitan America", "esVillano" : False},
                  {"nombre" : "Viuda Negra", "esVillano" : False},
                  {"nombre" : "Thanos", "esVillano" : True},
                  {"nombre" : "Doctor Stran", "esVillano" : False}]

    for elementos in personajes:
        arbol = arbol.insertar_nodo(elementos["nombre"], elementos)

    # Punto B
    arbol.inorden_villanos()

    # Punto C
    arbol.heroes_C()

    # Punto D
    print("Cantidad de superheroes", arbol.contar_superheroes())

    # Punto E
    nombre_a_buscar = input("Ingrese el nombre a buscar ")
    arbol.busqueda_proximidad(nombre_a_buscar)
    cambio = input("Ingrese el nombre a modificar ")
    info, datos = arbol.eliminar_nodo(cambio)
    nuevo_nombre = input("Ingrese el nuevo nombre ")
    datos["nombre"] = nuevo_nombre
    nuevo_es_villano = input("Es villano? si/no ")
    if nuevo_es_villano == "si":
        datos["esVillano"] = True
    else:
        datos["esVillano"] = False

    arbol = arbol.insertar_nodo(datos["nombre"], datos)

    arbol.inorden()
    print()

    # Punto F
    arbol.postorden_superheroes()

    # Punto E
    arbolSuperheroe = Arbol()
    arbolVillano    = Arbol()
    arbol.arboles_separados_heroe_villano(arbolSuperheroe, arbolVillano)
    arbolVillano.postorden()
    arbolSuperheroe.postorden()

# ejercicio5()

def ejercicio23():
    arbol = Arbol()

    criaturas = [{'nombre' : "Ceto", 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Tifon', 'derrotadoPor' : 'Zeus', 'descripcion' : '', 'capturadoPor' : ''},
                 {'nombre' : 'Equidna', 'derrotadoPor' : 'Argos Panoptes', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Dino', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Pefredo', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Enio', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Escila', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Medusa', 'derrotadoPor' : 'Perseo', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Ladon', 'derrotadoPor' : 'Heracles', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre': 'Ortro', 'derrotadoPor': 'Heracles', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Talos', 'derrotadoPor' : 'Medea', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Cerbero', 'derrotadoPor' : 'Teseo', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Toro de Creta', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Jabali de Erimanto', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Cierva Cerinea', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Aves de Estinfalo', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Basilisco', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Sirenas', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''}]

    for elementos in criaturas:
        arbol = arbol.insertar_nodo(elementos['nombre'], elementos)

    arbol.inorden()

    print()
    # C
    talos = arbol.busqueda('Talos')
    if talos:
        print(talos.datos)
    # D
    print()
    lista = Lista()
    aux = []
    arbol.nombreDioses(aux)
    for elementos in aux:
        cantidad = arbol.contarMuertes(elementos)
        dict = {'dios' : elementos, 'cantidadMuertes' : cantidad}
        lista.insertar(dict, 'cantidadMuertes')
    print('3 dioses con mas muertes:')
    print(lista.obtener_elemento(lista.tamanio()-3))
    print(lista.obtener_elemento(lista.tamanio()-2))
    print(lista.obtener_elemento(lista.tamanio()-1))
    print()

    # E
    criaturas = []
    print('Criaturas derrotadas por Heracles')
    criaturas = arbol.criaturaDerrotadaPor('Heracles', criaturas)
    for elementos in criaturas:
        print(elementos)

    # F
    print()
    print('Criaturas sin derrotar')
    arbol.criaturasSinDerrotar()

    # H
    print()
    arbol.modificarCapturadoPor()

    # I
    print()
    busquedaCoincidencia = input('Letras iniciales del nombre que desea buscar:')
    arbol.busqueda_proximidad(busquedaCoincidencia)

    # J
    arbol.eliminar_nodo('Basilisco')
    arbol.eliminar_nodo('Sirenas')

    # K
    arbol.modificarAvesEstinfalo

    # L
    ladInfo, ladDatos = arbol.eliminar_nodo('Ladon')
    arbol = arbol.insertar_nodo('Dragon Ladon', ladDatos)

    # M
    print()
    print('Barrido por nivel')
    arbol.barrido_por_nivel()
    print()

    # N
    print('Criaturas capturadas por Heracles')
    arbol.capturadoPor('Heracles')

ejercicio23()