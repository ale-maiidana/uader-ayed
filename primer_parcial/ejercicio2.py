# Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
# a. Listado ordenado de manera ascendente por nombre de los personajes.
# b. Determinar en que posicion esta The Thing y Rocket Raccoon.
# c. Listar todos los villanos de la lista.
# d. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# e. Listar los superheores que comienzan con  Bl, G, My, y W.
# f. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# g. Listado de superheroes ordenados por fecha de aparación.
# h. Modificar el nombre real de Ant Man a Scott Lang.
# i. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# j. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from lista_parc import List 
from superheroes import SuperHeroe
from cola_parc import Queue 

def order_by_nombre(item):
    return str(item.nombre)

def order_by_anio(item):
    return item.anio

lista = List(SuperHeroe)
aux = SuperHeroe()
class superHeroes:
    def __init__(self, nombre, alias, nombre_real, biografia, aparicion, es_villano):
        self.nombre = nombre
        self.alias = alias
        self.nombre_real = nombre_real
        self.biografia = biografia
        self.aparicion = aparicion
        self.es_villano = es_villano
        self.movies = List()
        self.movies.add_criterion('nombre', order_by_nombre)
        self.movies.add_criterion('anio', order_by_anio)

    def ordenar_por_nombre(self, lista):
        lista.add_criterion('name', lambda x: x['name'])
        lista.sort_by_criterion('name')
        return lista

    def buscar_posiciones(self, lista):
        self.ordenar_por_nombre(lista)
        posiciones = {}
        for index, personaje in enumerate(lista):
            if personaje['name'] in ["The Thing", "Rocket Raccoon"]:
                posiciones[personaje['name']] = index
        return posiciones

    def listar_villanos(self, lista):
        villanos = List()
        for personaje in lista:
            if personaje['is_villain']:
                villanos.append(personaje)
        return villanos

    def cola_villanos(self, lista):
        cola = Queue()
        for personaje in lista:
            if personaje['is_villain']:
                cola.arrive(personaje)
        return cola

    def listar_por_iniciales(self, lista, iniciales):
        personajes = []
        for personaje in lista:
            if any(personaje['name'].startswith(prefijo) for prefijo in iniciales):
                personajes.append(personaje)
        return personajes

    def ordenar_por_nombre_real(self, lista):
        lista.add_criterion('real_name', lambda x: x['real_name'])
        lista.sort_by_criterion('real_name')
        return lista

    def ordenar_por_aparicion(self, lista):
        lista.add_criterion('first_appearance', lambda x: x['first_appearance'])
        lista.sort_by_criterion('first_appearance')
        return lista

    def modificar_nombre_real(self, lista, nombre_personaje, nuevo_nombre_real):
        for personaje in lista:
            if personaje['name'] == nombre_personaje:
                personaje['real_name'] = nuevo_nombre_real
                return personaje
        return None

    def buscar_por_palabras_biografia(self, lista, palabras_clave):
        personajes_encontrados = []
        for personaje in lista:
            biografia = personaje['short_bio'].lower()
            if any(palabra.lower() in biografia for palabra in palabras_clave):
                personajes_encontrados.append(personaje)
        return personajes_encontrados

    def eliminar_personajes(self, lista, nombres_a_eliminar):
        eliminados = []
        i = 0
        while i < len(lista):
            if lista[i]['name'] in nombres_a_eliminar:
                eliminados.append(lista.pop(i))
            else:
                i += 1
        return eliminados

# Función para listar villanos aparecidos antes de 1980 desde la cola
def villanos_antes_1980(cola):
    villanos_80 = []
    for personaje in cola:
        if personaje['first_appearance'] < 1980:
            villanos_80.append(personaje)
    return villanos_80

# Agrega este método en cola_parc.Queue para que sea iterable:
# def __iter__(self):
#     return iter(self.__elements)

# Ejemplo de uso:

# Supongamos que tienes tu lista superheroes cargada (lista de diccionarios)


# a. Listado ordenado ascendente por nombre
print("a) Lista ordenada por nombre:")
for personaje in aux.ordenar_por_nombre(lista):
    print(personaje['name'])

# b. Posiciones de The Thing y Rocket Raccoon
print("\nb) Posiciones de The Thing y Rocket Raccoon:")
pos = aux.buscar_posiciones(lista)
for nombre in ["The Thing", "Rocket Raccoon"]:
    if nombre in pos:
        print(f"{nombre} está en la posición {pos[nombre]}")
    else:
        print(f"{nombre} no se encontró en la lista.")

# c. Listar todos los villanos
print("\nc) Villanos:")
for personaje in aux.listar_villanos(lista):
    print(f"{personaje['name']} - {personaje['alias']}")

# d. Cola con villanos para ver quienes aparecieron antes de 1980
cola_villanos = aux.cola_villanos(lista)
villanos_80 = villanos_antes_1980(cola_villanos)
print("\nd) Villanos antes de 1980:")
for v in villanos_80:
    print(f"{v['name']} - Apareció en {v['first_appearance']}")

# e. Superhéroes que comienzan con Bl, G, My, y W
iniciales = ["Bl", "G", "My", "W"]
personajes_filtrados = aux.listar_por_iniciales(lista, iniciales)
print("\ne) Superhéroes que comienzan con Bl, G, My y W:")
for p in personajes_filtrados:
    print(f"{p['name']} - Apareció en {p['first_appearance']}")

# f. Listado ordenado por nombre real
print("\nf) Lista ordenada por nombre real:")
for personaje in aux.ordenar_por_nombre_real(lista):
    print(personaje['real_name'])

# g. Listado de superheroes ordenados por fecha de aparición
print("\ng) Lista ordenada por fecha de aparición:")
for personaje in aux.ordenar_por_aparicion(lista):
    print(f"{personaje['name']} - {personaje['first_appearance']}")

# h. Modificar el nombre real de Ant Man a Scott Lang
modificado = aux.modificar_nombre_real(lista, "Ant Man", "Scott Lang")
print("\nh) Modificación de nombre real:")
if modificado:
    print(f"Nombre real modificado: {modificado['name']} - {modificado['real_name']}")
else:
    print("Personaje no encontrado")

# i. Mostrar personajes con 'time-traveling' o 'suit' en la biografía
palabras = ["time-traveling", "suit"]
resultados = aux.buscar_por_palabras_biografia(lista, palabras)
print("\ni) Personajes con 'time-traveling' o 'suit' en la biografía:")
for p in resultados:
    print(f"{p['name']} - Biografía: {p['short_bio']}")

# j. Eliminar a Electro y Baron Zemo de la lista y mostrar info
nombres_a_eliminar = ["Electro", "Baron Zemo"]
eliminados = aux.eliminar_personajes(lista, nombres_a_eliminar)
print("\nj) Personajes eliminados:")
if eliminados:
    for p in eliminados:
        print(f"{p['name']} - Alias: {p['alias']} - Nombre real: {p['real_name']}")
else:
    print("No se encontraron personajes para eliminar.")

