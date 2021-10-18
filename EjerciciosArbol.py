from arbol_binario import Arbol

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

    criaturas = [{'nombre' : "Ceto", 'derrotadoPor' : '', 'descripcion': ''},
                 {'nombre' : 'Tifon', 'derrotadoPor' : 'Zeus'},
                 {'nombre' : 'Equidna', 'derrotadoPor' : 'Argos Panoptes', 'descripcion': ''},
                 {'nombre' : 'Dino', 'derrotadoPor' : '', 'descripcion': ''},
                 {'nombre' : 'Pefredo', 'derrotadoPor' : '', 'descripcion': ''},
                 {'nombre' : 'Enio', 'derrotadoPor' : '', 'descripcion': ''},
                 {'nombre' : 'Escila', 'derrotadoPor' : '', 'descripcion': ''},
                 {'nombre' : 'Medusa', 'derrotadoPor' : 'Perseo', 'descripcion': ''},
                 {'nombre' : 'Ladón', 'derrotadoPor' : 'Heracles', 'descripcion': ''}]

    for elementos in criaturas:
        arbol = arbol.insertar_nodo(elementos['nombre'], elementos)

    arbol.inorden()



ejercicio23()