"""Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares."""

from mypila import Stack # Importamos la clase desde el archivo
from random import randint
import random

pila_numeros = Stack()  # Creamos una pila para almacenar números

for i in range(10):
    num_rand = random.randint (1, 100)  # Generamos un número aleatorio entre 1 y 100
    pila_numeros.push(num_rand)  # Agregamos el número a la pila


def num_impares(pila_numeros):
    pila_aux = Stack()  # Creamos una pila auxiliar para almacenar los números pares

    while pila_numeros.size() > 0:
        valor = pila_numeros.pop()
        if valor % 2 == 0:
            pila_aux.push(valor)

    # Devolvemos los números pares a la pila original

    while pila_aux.size() > 0:
        pila_numeros.push(pila_aux.pop())


def main():

    print ('Pila original:')
    pila_numeros.show()  # Mostramos la pila original

    num_impares(pila_numeros)  # Llamamos a la función para eliminar los impares
    print ('Pila después de eliminar los impares:')
    pila_numeros.show()  # Mostramos la pila después de eliminar los impares
if __name__ == "__main__":
    main()  # Ejecutamos la función principal