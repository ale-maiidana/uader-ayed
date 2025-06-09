# 7. Eliminar el i-ésimo elemento después del frente de la cola.

from my_cola_mejor import Queue
from random import randint
cola= Queue()
for i in range(10):
    cola.arrive(randint(1, 100))  # Generar números aleatorios entre 1 y 100

    print('Cola original:')
    cola.show()

def eliminar_iesimo(cola, i):
    if i < 1 or i > cola.size():
        print("Índice fuera de rango.")
        return cola
    temp_queue = Queue()
    count = 1
    while cola.size() > 0:
        elemento = cola.attention()
        if count != i:
            temp_queue.arrive(elemento)
        count += 1
        cola.attention()  # Descartar el elemento actual
    while temp_queue.size() > 0:
        cola.arrive(temp_queue.attention())
        temp_queue.attention()
    return cola

def main():
    i = int(input("Ingrese el índice del elemento a eliminar (1 para el primer elemento después del frente): "))
    cola = eliminar_iesimo(cola, i)
    print(f'Cola después de eliminar el {i}-ésimo elemento:')
    cola.show() 

if __name__ == '__main__':
    main()

    # ESTA MALLLLLLLL
    