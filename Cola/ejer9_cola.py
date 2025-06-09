#9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.

from my_cola_mejor import Queue
from random import randint

cola = Queue()

for i in range(15):
    numero = randint(-50, 50)  # Generar números aleatorios entre -50 y 50
    cola.arrive(numero)

cola.show()

valmax, valmin = cola.attention(), cola.attention()

negativos = 0

while cola.size() > 0:
    numero = cola.attention()
    if numero < valmin:
        valmin = numero
        if numero < 0:
            negativos += 1
    elif numero > valmax:
        valmax = numero
        if numero < 0:
            negativos += 1
    else:
        if numero < 0:
            negativos += 1
    cola.attention()  # Descartar el elemento actual
rango = valmax - valmin
print(f'El rango de la cola es: {rango}')
print(f'Cantidad de elementos negativos: {negativos}')

