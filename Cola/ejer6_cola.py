# 6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, 
# sin utilizar ningu￾na estructura auxiliar.

from my_cola_mejor import Queue



def contar_ocurrencias(cola, elemento):
    cont = 0
    while cola.size()> 0:
        actual = cola.attention()
        if actual == elemento:
            cont += 1
        cola.arrive(actual)
    return cont

def main():
    cola = Queue()
    def cargar_elemento ():
        while True:
            elemento = input('ingrese un elemento (o "fin" para terminar): ')
            if elemento.lower() == 'fin':
                break
            cola.arrive(elemento)
    cargar_elemento()
    print('Cola original:')
    cola.show()
    elemento = input('Ingrese el elemento a contar: ')
    ocurrencias = contar_ocurrencias(cola, elemento)
    print(f'El elemento "{elemento}" aparece {ocurrencias} veces en la cola.')
if __name__ == '__main__':
    main()


