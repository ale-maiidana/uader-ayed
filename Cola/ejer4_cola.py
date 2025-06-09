# 4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

from my_cola_mejor import Queue
import random
cola = Queue()
def es_primo(cola):
    cola_aux= Queue()
    while cola.size() > 0:
        numero = cola.attention()
        if numero > 2:
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    break
            else:
                cola_aux.arrive(numero)
        elif numero == 2:
            cola_aux.arrive(numero)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())
def main():
    def cargar_numeros():
        for _ in range(10):  # Cambiar a 10 para generar 10 números
            numero = random.randint(1, 100)  # Generar números entre 1 y 100
            cola.arrive(numero)

    cargar_numeros()
    print('Cola original:')
    cola.show()
    
    es_primo(cola)
    
    print('Cola con números primos:')
    cola.show()
if __name__ == '__main__':
    main()

