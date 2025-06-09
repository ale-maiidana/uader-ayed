'''1. Eliminar de una cola de caracteres todas las vocales que aparecen.'''

from my_cola_mejor import Queue

def eliminar_vocales(cola):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cola_aux = Queue()
    
    # Paso 1: eliminar vocales
    while cola.size() >  0:
        caracter = cola.attention()
        if caracter not in vocales:
            cola_aux.arrive(caracter)
    
    # Paso 2: devolver los elementos a la cola original
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())
    
    return cola

def main():
    cola = Queue()

    def ingresar_caracteres():
        while True:
            caracter = input('Ingrese un carácter o "fin" para terminar: ')
            if caracter.lower() == 'fin':
                break
            if len(caracter) == 1 and caracter.isalpha(): # Verificar si es un solo carácter alfabético
                cola.arrive(caracter)
            else:
                print('Por favor, ingrese un solo carácter alfabético.')

    ingresar_caracteres()

    print('Cola original:')
    cola.show()

    eliminar_vocales(cola)

    print('Cola sin vocales:')
    cola.show()

if __name__ == '__main__':
    main()


