"""Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra."""

from mypila import Stack  # Importamos la clase desde el archivo
from typing import Any, Optional

pila = Stack()

def invertir_pila(pila: Stack) -> None:
    pila_aux = Stack ()

    while pila.size() > 0:
        valor = pila.pop()
        pila_aux.push(valor)

        # Devolvemos los elementos a la pila original en orden invertido
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

def main():
    cant = int(input("Ingrese la cantidad de elementos en la pila: "))  

    for i in range(cant):
        valor = input(f'Ingrese el elemento {i + 1}: ')
        pila.push(valor)

    print('Pila ingresada:')
    pila.show()

    invertir_pila(pila)

    print('Pila después de invertir:')
    pila.show()

if __name__ == "__main__":
    main()  # Ejecutamos la función principal