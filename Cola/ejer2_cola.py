'''2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.'''

from my_cola_mejor import Queue

def invertir_cola(cola):
    pila = []
    # Pasar los elementos de la cola a la pila
    while cola.size() > 0:
        pila.append(cola.attention())
    # Pasar los elementos de la pila de vuelta a la cola
    while pila:
        cola.arrive(pila.pop())
    return cola

def main():
    cola = Queue()  # Mover la creación de la cola aquí

    def ingresar_numeros():
        while True:
            numero = input('Ingrese un número (o 0 para terminar): ')
            if numero == '0':  # Cambiar a comparación de cadena
                break
            if numero.isdigit():
                cola.arrive(int(numero))
            else:
                print('Por favor, ingrese un número entero válido.')

    ingresar_numeros()
    print('Cola original:')
    cola.show()
    cola = invertir_cola(cola)
    print('Cola invertida:')
    cola.show()

if __name__ == '__main__':
    main()

