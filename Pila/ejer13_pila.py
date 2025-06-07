# 13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni￾verse (MCU) `
# de los cuales se conoce el nombre del modelo, nombre de la película en la que se 
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), 
# resolver las siguientes actividades:
# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, 
# además mostrar el nombre de dichas películas;
# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar 
# más de un modelo de traje, estos deben cargarse por separado;
# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos 
# repetidos en una misma película;
# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y 
# “Capitan America: Civil War”.

from mypila import Stack 
from typing import Any, Optional

pila = Stack()

#carga de datos a la pila

pila.push({'modelo': 'Mark I', 'pelicula': 'Iron Man 2008', 'estado': 'destruido'})
pila.push({'modelo': 'Mark II', 'pelicula': 'Iron Man 2008', 'estado': 'impecable'})
pila.push({'modelo': 'Mark III', 'pelicula': 'Iron Man 2008', 'estado': 'destruido'})
pila.push({'modelo': 'Mark IV', 'pelicula': 'Iron Man 2', 'estado': 'dañado'})
pila.push({'modelo': 'Mark V', 'pelicula': 'Iron Man 2', 'estado': 'dañado'})
pila.push({'modelo': 'Mark VI', 'pelicula': 'The Avengers', 'estado': 'dañado'})
pila.push({'modelo': 'Mark VII', 'pelicula': 'The Avengers', 'estado': 'destruido'})
pila.push({'modelo': 'Mark XLVII', 'pelicula': 'spider-man homecoming', 'estado': 'impecable'})
pila.push({'modelo': 'Mark XLIV', 'pelicula': 'capitan america civil war', 'estado': 'impecable'})

def buscar_modelo(pila):
    pila_aux = Stack()
    encontrado = False
    while pila.size() > 0:
        traje = pila.pop()
        if (traje['modelo'] == 'Mark XLIV'):
            print(f"El modelo {traje['modelo']} fue utilizado en la película: {traje['pelicula']}")
            encontrado = True
        pila_aux.push(traje)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    if not encontrado:
        print("El modelo Mark XLIV no fue utilizado en ninguna película.")

def mostrar_trajes_danados(pila):
    pila_aux = Stack()

    while pila.size() > 0:
        traje = pila.pop()
        if traje['estado'] == 'dañado':
         print(f"Traje dañado: {traje['modelo']} de la película {traje['pelicula']}")
        pila_aux.push(traje)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())


def eliminar_trajes_destruidos(pila):
    pila_aux = Stack()

    while pila.size() > 0:
        traje = pila.pop()
        if traje['estado'] == 'destruido':
            print(f'eliminando traje destruido: {traje["modelo"]} de la película {traje["pelicula"]}')
        else:
            pila_aux.push(traje)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

def agregar_traje(pila, modelo, pelicula):
    pila_aux = Stack()
    existe = False 

    while pila.size() > 0:
        traje = pila.pop()
        if traje['modelo'] == modelo and traje['pelicula'] == pelicula:
            existe = True
        pila_aux.push(traje)
    if not existe:
        pila.push({'modelo': modelo, 'pelicula': pelicula, 'estado': 'impecable'})
        print(f"Traje {modelo} agregado a la película {pelicula}.")
    else:
        print(f"El traje {modelo} ya existe en la película {pelicula}. No se puede agregar.")

def mostrar_trajes_peliculas(pila, peliculas):
    pila_aux = Stack()

    while pila.size() > 0:
        traje = pila.pop()
        if traje['pelicula'].lower() in peliculas:
            print(f"Traje: {traje['modelo']} de la película {traje['pelicula']}")
        pila_aux.push(traje)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())


def main():
    print("a. Buscar modelo Mark XLIV:")
    buscar_modelo(pila)

    print("\nb. Mostrar trajes dañados:")
    mostrar_trajes_danados(pila)

    print("\nc. Eliminar trajes destruidos:")
    eliminar_trajes_destruidos(pila)

    print("\nd. Agregar modelo Mark LXXXV:")
    agregar_traje(pila, 'Mark LXXXV', 'Avengers: Endgame')

    print("\ne. Mostrar trajes de Spider Man Homecoming y Capitan America Civil War:")
    mostrar_trajes_peliculas(pila, ['spider-man homecoming', 'capitan america civil war'])

if __name__ == "__main__":
    main()  # Ejecutamos la función principal

   


        