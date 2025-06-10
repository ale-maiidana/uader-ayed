# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.

superheroes = [
    "Iron Man",
    "Captain America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Scarlet Witch",
    "Ant-Man",
    "Wasp",
    "Vision",
    "Falcon",
    "Winter Soldier"
]

def buscar_heroe(lista, objetivo, indice=0):
    if indice >= len(lista):
        print(f"El superhéroe '{objetivo}' no se encuentra en la lista.")
        return -1
    if lista[indice] == objetivo:
        return indice
    return buscar_heroe(lista, objetivo, indice + 1)

def mostrar(lista):
    if not lista:
        return
    print(lista[0])
    mostrar(lista[1:])


indice = buscar_heroe(superheroes, "Captain America")

if indice != -1:
    print(f"'Captain America' está en la lista.")


print("\nLista de superhéroes:")
mostrar(superheroes)
