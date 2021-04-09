def fibonacci_recursivo(numero):
    if numero == 1 or numero == 0:
        return numero
    else:
        return (numero - 1) + (numero - 2)

print(fibonacci_recursivo(8))

