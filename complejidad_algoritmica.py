import time
import sys
sys.setrecursionlimit(1000000)


def factorial(n):
    """
    Esta funcion es una prueba de complejidad algoritmica
    """
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_r(n):
    """
    Esta funcion es una prueba de complejidad algoritmica
    """
    if n == 1:
        return 1
    else:
        return n * factorial_r(n-1)


if __name__ == "__main__":
    n = 100000
    sys.setrecursionlimit(1000000)
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print("Esta es la funcion no recursiva")
    print(final-comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print("Esta es la funcion recursiva")
    print(final-comienzo)
