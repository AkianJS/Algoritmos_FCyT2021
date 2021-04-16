# Ejercicio 5

def romano_a_decimal(n_romano):
    numero_rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if len(n_romano) == 1:
        return numero_rom[n_romano[0]]
    elif numero_rom[n_romano[0]] < numero_rom[n_romano[1]]:
        return -(numero_rom[n_romano[0]]) + romano_a_decimal(n_romano[1:])
    else:
        return numero_rom[n_romano[0]] + romano_a_decimal(n_romano[1:])


print("Su numero romano pasado a decimal es: ", romano_a_decimal("CMXXV"))


# Ejercicio 8

def decimal_binario(numero):
    if numero == 0:
        return ""
    else:
        return decimal_binario(numero // 2) + str(numero % 2)


print("El numero decimal en binario es: ", decimal_binario(2))


# Ejercicio 21

def busqueda_binaria_r(lista, x, izq, der) -> object:
    medio = (izq + der) // 2

    if izq > der:
        return -1
    elif lista[medio] == x:
        return medio + 1
    elif lista[medio] < x:
        return busqueda_binaria_r(lista, x, medio + 1, der)
    else:
        return busqueda_binaria_r(lista, x, izq, medio - 1)


lista_n = [1, 3, 5, 7, 9, 11, 13, 15]
print("El indice de su buscado es: ", busqueda_binaria_r(lista_n, 11, 0, len(lista_n) - 1))


# Ejercicio 22

def usar_la_fuerza(mochila, sable, pos):
    if mochila[pos] == sable:
        return pos + 1
    elif pos == len(mochila) - 1:
        return - 1
    else:
        return usar_la_fuerza(mochila, sable, pos + 1)


mochila = ["Cepillo Jedai", "Reloj Jedai", "Foto de Yoda", "Sable de luz", "Regalo de Padme"]
posicion = (usar_la_fuerza(mochila, "Sable de luz", 0))
if posicion != -1:
    print("Se encontro el Sable de luz en la posición: ", posicion)
    print("Se necesitaron sacar", posicion - 1, "objetos para encontrarlo")

# Ejercicio 23

# def escape_laberinto(x, y, matriz):


matriz = [[0, 1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 1],
          [1, 0, 0, 0, 0, 1],
          [0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 2]]


def escapeLaberinto(matriz, x, y, movimiento):

    if matriz[x][y] == 2:
        return 1
    elif movimiento == "der" and matriz [x][y] == 1:
        print("Chocaste contra una pared, retrocede")
        return escapeLaberinto(matriz, x, y - 1, movimiento)
    elif movimiento == "izq" and matriz [x][y] == 1:
        print("Chocaste contra una pared, retrocede")
        return escapeLaberinto(matriz, x, y + 1, movimiento)
    elif movimiento == "arriba" and matriz [x][y] == 1:
        print("Chocaste contra una pared, retrocede")
        return escapeLaberinto(matriz, x + 1, y, movimiento)
    elif movimiento == "abajo" and matriz [x][y] == 1:
        print("Chocaste contra una pared, retrocede")
        return escapeLaberinto(matriz, x - 1, y, movimiento)
    else:
        movimiento = input("Digite direccion de movimiento: der/izq/arriba/abajo ")

        if (y == 0 and movimiento == "izq"):
            print("Hay una pared de ese lado!")
            return escapeLaberinto(matriz, x, y, movimiento)
        elif (x == 0 and movimiento == "arriba"):
            print("Hay una pared de ese lado!")
            return escapeLaberinto(matriz, x, y, movimiento)
        elif (y == 5 and movimiento == "der"):
            print("Hay una pared de ese lado!")
            return escapeLaberinto(matriz, x, y, movimiento)
        elif (x == 5 and movimiento == "abajo"):
            print("Hay una pared de ese lado!")
            return escapeLaberinto(matriz, x, y, movimiento)
        else:
            if movimiento == "der":
                return escapeLaberinto(matriz, x, y + 1, movimiento)
            elif movimiento == "izq":
                return escapeLaberinto(matriz, x, y - 1, movimiento)
            elif movimiento == "arriba":
                return escapeLaberinto(matriz, x - 1, y, movimiento)
            elif movimiento == "abajo":
                return escapeLaberinto(matriz, x + 1, y, movimiento)


escapo = escapeLaberinto(matriz, 0, 0, "")
if escapo == 1: print("Escapo con exito")