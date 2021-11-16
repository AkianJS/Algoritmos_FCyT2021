from EstructuraLista import Lista

# Ejercicio 6
print("Ejercicio 6")
print()


def marvelEjercicio6():
    lista = Lista()
    datos = [
        {"nombre" : "Iron Man", "anio" : 1962, "comic" : "marvel", "biografia" : "filantropo con armadura"},
        {"nombre" : "Linterna Verde", "anio" : 1975, "comic" : "dc", "biografia" : "es verde"},
        {"nombre" : "Dr Strange", "anio" : 1972, "comic" : "dc", "biografia" : "lleva un traje cool"},
        {"nombre" : "Wolverine", "anio" : 1968, "comic" : "dc", "biografia" : "tiene garras de acero"},
        {"nombre": "Capitana Marvel", "anio": 1980, "comic": "marvel", "biografia": "se inspiró en Capitan Marvel"},
        {"nombre": "Mujer Maravilla", "anio": 1960, "comic": "dc", "biografia" : "tiene un latigo"},
        {"nombre": "Star-lord", "anio": 1975, "comic": "marvel", "biografia": "tuvo un accidente en su nave"},
        {"nombre": "Flash", "anio": 1940, "comic": "dc", "biografia": "estudiante universitario, usa un traje"}
        ]

    for elementos in datos:
        lista.insertar(elementos, "nombre")

    # Punto A
    linternaVerdePos = lista.busqueda("Linterna Verde", "nombre")
    if linternaVerdePos != -1:
        lista.eliminar(linternaVerdePos)

    # Punto B
    wolverine = lista.busqueda("Wolverine", "nombre")
    if wolverine != -1:
        jsonWolverine = lista.obtener_elemento(wolverine)
        print("Wolverine aparecio en el anio", jsonWolverine["anio"])
    print()

    # Punto C
    drStrangerPos = lista.busqueda("Dr Strange", "nombre")
    if drStrangerPos != -1:
        jsonDrStrange = lista.obtener_elemento(drStrangerPos)
        jsonDrStrange["comic"] = "marvel"
        lista.modificar_elemento(drStrangerPos, jsonDrStrange, "nombre")
    print()

    # Punto D
    for i in range (0, lista.tamanio()):
        cadenaBiografia = lista.obtener_elemento(i)["biografia"]
        if cadenaBiografia.find("traje") != -1 or cadenaBiografia.find("armadura") != -1:
            print("Nombre del heroe con armadura o traje: ", lista.obtener_elemento(i)["nombre"])
    print()

    # Punto E
    for i in range (0, lista.tamanio()):
        personajesPrevios1963 = lista.obtener_elemento(i)
        if personajesPrevios1963["anio"] < 1963:
            print("Personaje anterior a 1963", personajesPrevios1963["nombre"], personajesPrevios1963["comic"])
    print()

    # Punto F
    posCapitanaMarvel = lista.busqueda("Capitana Marvel", "nombre")
    if posCapitanaMarvel != -1:
        print("Casa de Capitana Marvel:", lista.obtener_elemento(posCapitanaMarvel)["comic"])
    posMujerMaravilla = lista.busqueda("Mujer Maravilla", "nombre")
    if posMujerMaravilla != -1:
        print("Casa de la Mujer Maravilla:", lista.obtener_elemento(posMujerMaravilla)["comic"])
    print()

    # Punto G
    posFlash = lista.busqueda("Flash", "nombre")
    posStarLord = lista.busqueda("Star-lord", "nombre")
    if posFlash != -1:
        print(lista.obtener_elemento(posFlash))
    if posStarLord != -1:
        print(lista.obtener_elemento(posStarLord))
    print()

    # Punto H
    for i in range (0, lista.tamanio()):
        if lista.obtener_elemento(i)["nombre"][0] == "B" or lista.obtener_elemento(i)["nombre"][0] == "M" or lista.obtener_elemento(i)["nombre"][0] == "S":
            print(lista.obtener_elemento(i))
    print()

    # Punto I
    contadorMarvel = 0
    contadorDc = 0
    for i in range (0, lista.tamanio()):
        if lista.obtener_elemento(i)["comic"] == "marvel":
            contadorMarvel += 1
        else:
            contadorDc += 1
    print("Heroes de marvel:", contadorMarvel) # Habra 4 porque cambiamos a Dr Strange de casa
    print("Heroes de DC:", contadorDc) # Habra 3 porque eliminamos a Linterna Verde


marvelEjercicio6()
print()

def ejercicio7():

    lista1 = Lista()
    lista2 = Lista()

    datos = [
        {'nombre': 'Juan', 'edad' : 28},
        {'nombre': 'Tito', 'edad': 32},
        {'nombre': 'Lara', 'edad': 67},
        {'nombre': 'Julia', 'edad': 22}
    ]

    datos2 = [
        {'nombre': 'Juan', 'edad' : 16},
        {'nombre': 'Pedro', 'edad': 25},
        {'nombre': 'Zulma', 'edad': 17},
        {'nombre': 'Tito', 'edad': 42}
         ]

    for elementos in datos:
        lista1.insertar(elementos, 'nombre')

    for elementos in datos2:
        lista2.insertar(elementos, 'nombre')

    for i in range(0, lista2.tamanio()):
        lista1.insertar(lista2.obtener_elemento(i), 'nombre')

    print('Lista concatenada')
    lista1.barrido()
    print()

    lista3 = Lista()
    lista4 = Lista()

    control = False
    repetido = 0

    for elementos in datos:
        lista3.insertar(elementos, 'nombre')

    for elementos in datos2:
        lista4.insertar(elementos, 'nombre')

    print('Lista sin repeticion y cant de repetidos')
    # Punto B y C


    for i in range (0, lista3.tamanio()):
        for j in range (0, lista4.tamanio()):

            if lista3.obtener_elemento(i)['nombre'] != lista4.obtener_elemento(j)['nombre']:
                control = True
            else:
                control = False
                break

        if control:
            lista3.insertar(lista4.obtener_elemento(i), 'nombre')
        else:
            repetido += 1

    lista3.barrido()
    print('Cantidad de repetidos', repetido)
    print()

    # Eliminar y mostrar
    print('Eliminar y mostrar')
    while(not lista1.lista_vacia()):
        print(lista1.obtener_elemento(0))
        lista1.eliminar(0)
    print()

ejercicio7()


print('Ejercicio 15:')

def pokemonEjercicio():
    entrenador = [{'nombre' : 'Ash', 'torneos': 13, 'batallasPerdidas' : 4, 'batallasGanadas' : 22, 'pokemon' : Lista()},
                  {'nombre' : 'Misty', 'torneos': 2, 'batallasPerdidas' : 2, 'batallasGanadas' : 13, 'pokemon' : Lista()},
                  {'nombre': 'Brock', 'torneos': 3, 'batallasPerdidas': 7, 'batallasGanadas': 11, 'pokemon': Lista()}]

    pokemonAsh = {'nombre' : 'Pikachu', 'nivel' : 10, 'tipo' : 'electro', 'subtipo' : 'ninguno'}
    pokemonMisty = {'nombre' : 'Staryu', 'nivel' : 4, 'tipo' : 'agua', 'subtipo' : 'ninguno'}
    pokemonBrock = {'nombre' : 'Geodude', 'nivel' : 6, 'tipo' : 'roca', 'subtipo' : 'ninguno'}

    entrenador[0]['pokemon'].insertar(pokemonAsh, 'nombre')
    entrenador[1]['pokemon'].insertar(pokemonMisty, 'nombre')
    entrenador[2]['pokemon'].insertar(pokemonBrock, 'nombre')

    lista = Lista()
    listaTorneos = Lista()

    for elementos in entrenador:
        lista.insertar(elementos, 'nombre')
        listaTorneos.insertar(elementos, 'torneos')


    print(entrenador[0]['pokemon'].obtener_elemento(0))

    def cantPokemonesEntrenador (nombre):
        print('Cantidad de pokemones de ', nombre)
        pos = lista.busqueda(nombre, 'nombre')
        print(lista.obtener_elemento(pos)['pokemon'].tamanio())

    cantPokemonesEntrenador('Ash')
    print()

    for i in range (0, lista.tamanio()):
        entrenadorPok = lista.obtener_elemento(i)
        if entrenadorPok['torneos'] > 3:
            print(entrenadorPok['nombre'], 'gano mas de 3 torneos')

    pokemones = listaTorneos.obtener_elemento(listaTorneos.tamanio()-1)['pokemon']
    entrenadorCantMayorTorneo = listaTorneos.obtener_elemento(listaTorneos.tamanio()-1)
    pokemonMayorNivel = 0

    for i in range (0, entrenadorCantMayorTorneo['pokemon'].tamanio()):
        if pokemones.obtener_elemento(i)['nivel'] > pokemonMayorNivel:
            pokemonMayorNivel = pokemones.obtener_elemento(i)

    print()
    print('Entrenador con mas torneos', entrenadorCantMayorTorneo['nombre'])
    print('Su pokemon de mayor nivel es', pokemonMayorNivel)
    print()

    def datosEntrenadorYPokemon(lista, nombre):
        pos = lista.busqueda(nombre, 'nombre')
        entrenador = lista.obtener_elemento(pos)
        print('Entrenador:', entrenador)
        print('Sus pokemones')
        for i in range (0, lista.obtener_elemento(pos)['pokemon'].tamanio()):
            print(entrenador['pokemon'].obtener_elemento(i))

    datosEntrenadorYPokemon(lista, 'Ash')
    print()

    def entrenadores79WinRate(lista):
        for i in range (0, lista.tamanio()):
            entrenador = lista.obtener_elemento(i)
            print(entrenador)
            ganadas = entrenador['batallasGanadas']
            perdidas = entrenador['batallasPerdidas']
            total = ganadas + perdidas
            ratio = (ganadas / total) * 100
        if ratio > 79:
            print(entrenador['nombre'], 'tiene un porcentaje de victorias mayor a 79')

    entrenadores79WinRate(lista)

    # def fuegoPlantaAgua

pokemonEjercicio()

print()
print("Ejercicio 22:")

def jedisEjercicio22():
    # Cargar personajes desde archivo
    lista = Lista()
    listaEspecie = Lista()
    file = open('jedis.txt')

    lineas = file.readlines()
    lineas.pop(0)
    for linea in lineas:
        jedi = linea.split(';')
        jedi[7] = float(jedi[7].split('\n')[0])
        datosJedis = {}
        datosJedis['nombre'] = jedi[0].title()
        datosJedis['rango'] = jedi[1]
        datosJedis['especie'] = jedi[2]
        datosJedis['maestro'] = jedi[3].split('/')
        datosJedis['colorSable'] = jedi[4].split('/')
        datosJedis['mundoNatal'] = jedi[5]
        datosJedis['nacimiento'] = jedi[6]
        datosJedis['altura'] = jedi[7]
        if (len(jedi) > 8):
            datosJedis['to_darkside'] = jedi[8]
            datosJedis['come_lightside'] = jedi[9]
        lista.insertar(datosJedis, 'nombre')
        listaEspecie.insertar(datosJedis, 'especie')

    file.close()

    # Comienzo del ejercicio
    # Punto A
    print("Ordenados por nombre")
    lista.barrido()
    print()
    print("Ordenados por especie")
    listaEspecie.barrido()
    print()

    # Punto B
    posAhsoka = lista.busqueda("Ahsoka Tano", "nombre")
    posKitFisto = lista.busqueda("Kit Fisto", "nombre")
    print("Info de:", lista.obtener_elemento(posAhsoka))
    print("Info de:", lista.obtener_elemento(posKitFisto))

    # Punto C
    print("Padawans de Yoda")
    for i in range (0, lista.tamanio()):
        if "yoda" in lista.obtener_elemento(i)["maestro"]:
            print(lista.obtener_elemento(i))
    print()
    print("Padawans de Anakin")
    for i in range (0, lista.tamanio()):
        if "anakin skywalker" in lista.obtener_elemento(i)["maestro"]:
            print(lista.obtener_elemento(i))
    print()

    # Punto D
    print("Jedi especie humana:")
    for i in range (0, lista.tamanio()):
        if "human" in lista.obtener_elemento(i)["especie"]:
            print(lista.obtener_elemento(i))
    print()
    print("Jedi especie twi'lek:")
    for i in range (0, lista.tamanio()):
        if "twi'lek" in lista.obtener_elemento(i)["especie"]:
            print(lista.obtener_elemento(i))
    print()

    print("Jedis que comienzan con A")
    for i in range (0, lista.tamanio()):
        if "A" == lista.obtener_elemento(i)["nombre"][0]:
            print(lista.obtener_elemento(i))
    print()

    print("Jedis que usaron sables de mas de un color")
    for i in range (0, lista.tamanio()):
        if  1 < len(lista.obtener_elemento(i)["colorSable"]):
            print(lista.obtener_elemento(i))
    print()

    print("Padawans de Qui-Gon Jin:")
    for i in range (0, lista.tamanio()):
        if "qui-gon jin" in lista.obtener_elemento(i)["maestro"]:
            print(lista.obtener_elemento(i))
    print()

    print("Padawans de Mace Windu")
    for i in range (0, lista.tamanio()):
        if "mace windu" in lista.obtener_elemento(i)["maestro"]:
            print(lista.obtener_elemento(i))

# jedisEjercicio22()