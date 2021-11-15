from arbol_binario import Arbol
from grafo import Grafo

def ejercicioParcialArbol():
    dinosaurios = [{"nombre": "T-rex", "codigo": 22553, 'ubicacion' : '3B'},
                   {"nombre": "T-rex", "codigo": 32423, 'ubicacion' : '7G'},
                   {"nombre": "Velocirraptor", "codigo": 35623, 'ubicacion' : '7G'},
                   {"nombre": "Triceratop", "codigo": 75673, 'ubicacion' : '2A'},
                   {"nombre": "Allosaurus", "codigo": 756, 'ubicacion' : '2A'},
                   {"nombre": "Sgimoloch", "codigo": 22873, 'ubicacion' : '8R'},
                   {"nombre": "Raptor", "codigo": 56734, 'ubicacion' : '3C'},
                   {"nombre": "Raptor", "codigo": 11938, 'ubicacion' : '9B'},
                   {"nombre": "Diplodocus", "codigo": 425, 'ubicacion' : '10C'},
                   {"nombre": "Diplodocus", "codigo": 16364, 'ubicacion' : '2H'},
                   {"nombre": "Diplodocus", "codigo": 45243, 'ubicacion' : '8F'},
                   {"nombre": "Velocirraptor", "codigo": 467, 'ubicacion' : '10F'},
                   {"nombre": "Baryonix", "codigo": 44521, 'ubicacion' : '8F'},
                   {"nombre": "Styracosaurus", "codigo": 98437, 'ubicacion' : '5D'},
                   {"nombre": "Diplodocus", "codigo": 52345, 'ubicacion' : '11A'},
                   {"nombre": "Raptor", "codigo": 31245, 'ubicacion' : '3B'},
                   {"nombre": "Stygimoloch", "codigo": 56623, 'ubicacion' : '3C'}]

    arbolNombre = Arbol()
    arbolCodigo = Arbol()

    for elementos in dinosaurios:
        arbolNombre = arbolNombre.insertar_nodo(elementos["nombre"], elementos)
        arbolCodigo = arbolCodigo.insertar_nodo(elementos["codigo"], elementos)

    # Punto 2
    arbolNombre.inorden()
    print()

    # Punto 3
    pos  = arbolCodigo.busqueda(756)
    print(pos.datos)
    print()

    # Punto 5
    arbolNombre.tRexEnIsla('T-rex')
    print()

    # Punto 6
    nombre, datos = arbolNombre.eliminar_nodo('Sgimoloch')
    arbolNombre = arbolNombre.insertar_nodo(nombre, datos) # Eliminar y re-insertar porque el campo clave es el nombre
    arbolCodigo.modificarSgimoloch('Sgimoloch')

    # Punto 7
    print('Ubicacion de los raptores: ')
    arbolNombre.ubicacionRaptores('Raptor')
    print()

    # Punto 8
    cantidadDiplodocus = arbolNombre.contarDiplodocus('Diplodocus')
    print('La cantidad de Diplodocus en el parque es', cantidadDiplodocus)

# ejercicioParcialArbol()

def ejercicioParcialGrafo():
    equipo = Grafo(dirigido=False)

    equipo.insertar_vertice('Guarani', data={'tipo': 'servidor'})
    equipo.insertar_vertice('Debian', data={'tipo': 'notebook'})
    equipo.insertar_vertice('Ubuntu', data={'tipo': 'pc'})
    equipo.insertar_vertice('Impresora', data={'tipo': 'impresora'})
    equipo.insertar_vertice('Mint', data={'tipo': 'pc'})
    equipo.insertar_vertice('Switch 1', data={'tipo': 'switch'})
    equipo.insertar_vertice('Switch 2', data={'tipo': 'switch'})
    equipo.insertar_vertice('Arch', data={'tipo': 'notebook'})
    equipo.insertar_vertice('Red Hat', data={'tipo': 'notebook'})
    equipo.insertar_vertice('Router 1', data={'tipo': 'router'})
    equipo.insertar_vertice('Router 2', data={'tipo': 'router'})
    equipo.insertar_vertice('Router 3', data={'tipo': 'router'})
    equipo.insertar_vertice('Manjaro', data={'tipo': 'pc'})
    equipo.insertar_vertice('Parrot', data={'tipo': 'pc'})
    equipo.insertar_vertice('Fedora', data={'tipo': 'pc'})
    equipo.insertar_vertice('MongoDB', data={'tipo': 'servidor'})

    equipo.insertar_arista(22, 'Impresora', 'Switch 1')
    equipo.insertar_arista(18, 'Ubuntu', 'Switch 1')
    equipo.insertar_arista(17, 'Debian', 'Switch 1')
    equipo.insertar_arista(80, 'Mint', 'Switch 1')
    equipo.insertar_arista(37, 'Router 1', 'Router 2')
    equipo.insertar_arista(25, 'Router 2', 'Red Hat')
    equipo.insertar_arista(9, 'Guarani', 'Router 2')
    equipo.insertar_arista(50, 'Router 2', 'Router 3')
    equipo.insertar_arista(40, 'Manjaro', 'Switch 2')
    equipo.insertar_arista(40, 'Parrot', 'Switch 2')
    equipo.insertar_arista(40, 'Arch', 'Switch 2')
    equipo.insertar_arista(40, 'Fedora', 'Switch 2')

    equipo.insertar_arista(29, 'Switch 1', 'Router 1')
    equipo.insertar_arista(43, 'Router 1', 'Router 3')
    equipo.insertar_arista(61, 'Router 3', 'Switch 2')
    equipo.insertar_arista(22, 'Switch 2', 'MongoDB')

    origenRedHat = equipo.buscar_vertice('Red Hat')
    origenDebian = equipo.buscar_vertice('Debian')
    origenArch = equipo.buscar_vertice('Arch')

    # print('Barrido profundidad Red Hat')
    # equipo.barrido_profundidad(origenRedHat)
    # print()
    # equipo.barrido_profundidad(origenDebian)
    # equipo.barrido_profundidad(origenArch)
    # print()
    # equipo.barrido_amplitud(origenRedHat)
    # equipo.barrido_amplitud(origenDebian)
    # equipo.barrido_amplitud(origenArch)

    # Punto 3
    def caminoMasCorto(grafo, origen, destino):


        verticeOrigen = grafo.buscar_vertice(origen)
        verticeDestino = grafo.buscar_vertice(destino)
        costo = None

        if verticeOrigen != -1 and verticeDestino != -1:
            camino = grafo.dijkstra(verticeOrigen, verticeDestino)
            while (not camino.pila_vacia()):
                dato = camino.desapilar()
                if (dato[1][0] == destino):
                    if (costo is None):
                        costo = dato[0]
                    print('paso por: ', dato[1][0])
                    destino = dato[1][1]
            print('el costo total del camino es: ', costo)

    caminoMasCorto(equipo, 'Debian', 'MongoDB')
    print()
    caminoMasCorto(equipo, 'Red Hat', 'MongoDB')
    print()

    print('Arbol de exp min')
    bosqueExpMin = equipo.prim()
    peso = 0
    for elemento in bosqueExpMin:
        print(elemento[1][0], '-', elemento[1][1])
        peso += elemento[0]

    print()
    print('Barrido sin Impresora')
    equipo.eliminar_vertice('Impresora')
    # equipo.barrido_profundidad(origenRedHat)

ejercicioParcialGrafo()