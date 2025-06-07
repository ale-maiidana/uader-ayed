"""Reemplazar todas las ocurrencias de un determinado elemento en una pila."""
from mypila import Stack  # Importamos la clase desde el archivo
from typing import Any, Optional

pila = Stack()  # Creamos una pila para almacenar elementos

def reemplazar_ocurrencias(pila: Stack, elem_buscado: Any, nuevo_elem: Any) -> None:
    aux_stack = Stack() # Pila auxiliar para almacenar los elementos
   
    while pila.size() > 0:
        valor = pila.pop()
        if valor == elem_buscado:
            aux_stack.push(nuevo_elem)
        else:
            aux_stack.push(valor)

    # Devolvemos los elementos a la pila original
    while aux_stack.size() > 0:
        pila.push(aux_stack.pop())


def main():
    cant = int(input("Ingrese la cantidad de elementos en la pila: "))  

    for i in range(cant):
        valor = input(f'Ingrese el elemento {i + 1}: ')
        pila.push(valor)

    print('Pila ingresada:')
    pila.show()

    buscado = input("Ingrese el elemento a buscar: ")
    nuevo = input("Ingrese el nuevo elemento: ")
    
    reemplazar_ocurrencias(pila, buscado, nuevo)

    print('Pila después de reemplazar las ocurrencias:')
    pila.show()

if __name__ == "__main__":
    main()  # Ejecutamos la función principal