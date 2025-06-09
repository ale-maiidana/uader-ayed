# 5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.

from my_cola_mejor import Queue
from my_pila_cola import Stack
from random import randint

cola = Queue()
pila = Stack()

for i in range(10):
    pila.push(randint(1, 100))  # Generar números aleatorios entre 1 y 100

print ('Contenido de la pila original:')
pila.show()

while pila.size()> 0:
    cola.arrive(pila.pop())

while cola.size() > 0:
    pila.push(cola.attention())

print('Contenido de la pila invertida:')
pila.show()



