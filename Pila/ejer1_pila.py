#Determinar el número de ocurrencias de un determinado elemento en una pila.
from mypila import Stack #importamos la clase desde el archivo
from typing import Any, Optional


def contar_ocurrencias (pila: Stack, elem_buscado: Any) -> int:
    aux_stack = Stack()  # Pila auxiliar para almacenar los elementos
    contador = 0  # Contador de ocurrencias

    #recorremos la pila
    while pila.size() > 0:
        valor = pila.pop()
        if valor == elem_buscado:
            contador += 1
        aux_stack.push(valor)

    # Devolvemos los elementos a la pila original
    while aux_stack.size() > 0:
        pila.push(aux_stack.pop())

    return contador  # Devolvemos el número de ocurrencias encontradas

def main():
    pila = Stack()

    cant = int(input("Ingrese la cantidad de elementos en la pila: "))  

    for i in range(cant):
        valor = input(f'Ingrese el elemento {i + 1}: ')
        pila.push(valor)

    print('Pila ingresada:')
    pila.show()

    buscado = input("Ingrese el elemento a buscar: ")
    ocurrencias = contar_ocurrencias(pila, buscado)

    print(f'El elemento "{buscado}" se encuentra {ocurrencias} veces en la pila.')

if __name__ == "__main__":
    main()
# Este código define una función para contar las ocurrencias de un elemento en una pila.