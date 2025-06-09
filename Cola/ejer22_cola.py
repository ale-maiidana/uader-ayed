# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU),
# de los cuales se cono￾ce el nombre del personaje, el nombre del superhéroe y su género 
# (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M},
# {Natasha Ro￾manoff, Black Widow, F}, etc.,
# desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from my_cola_mejor import Queue

cola = Queue()

cola.arrive({"nombre_personaje": "Tony Stark", "superheroe": "Iron man", "genero": "M"})
cola.arrive({"nombre_personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
cola.arrive({"nombre_personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
cola.arrive({"nombre_personaje": "Bruce Banner", "superheroe": "Hulk", "genero": "M"})
cola.arrive({"nombre_personaje": "Thor Odinson", "superheroe": "Thor", "genero": "M"})
cola.arrive({"nombre_personaje": "Clint Barton", "superheroe": "Hawkeye", "genero": "M"})
cola.arrive({"nombre_personaje": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"})
cola.arrive({"nombre_personaje": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"})
cola.arrive({"nombre_personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"})
cola.arrive({"nombre_personaje": "T'Challa", "superheroe": "Black Panther", "genero": "M"})
cola.arrive({"nombre_personaje": "Carol Danvers", "superheroe": "Captain Marvel", "genero": "F"})
cola.arrive({"nombre_personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})
cola.arrive({"nombre_personaje": "Hope van Dyne", "superheroe": "Wasp", "genero": "F"})
cola.arrive({"nombre_personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"})
cola.arrive({"nombre_personaje": "Bucky Barnes", "superheroe": "Winter Soldier", "genero": "M"})
cola.arrive({"nombre_personaje": "Shuri", "superheroe": "Black Panther (heredado)", "genero": "F"})
cola.arrive({"nombre_personaje": "Marc Spector", "superheroe": "Moon Knight", "genero": "M"})


def buscar_capitana_marvel(cola):
    cola_aux = Queue()
    nombre = None
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['superheroe'].lower() == 'captain marvel':
            nombre = personaje['nombre_personaje']
        cola_aux.arrive(personaje)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())
    return nombre


def mostrar_superheroes_femeninos(cola):
    cola_aux = Queue()
    print("Superhéroes femeninos:")
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['genero'].upper() == 'F':
            print(personaje['superheroe'])
        cola_aux.arrive(personaje)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())


def mostrar_personajes_masculinos(cola):
    cola_aux = Queue()
    print("Personajes masculinos:")
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['genero'].upper() == 'M':
            print(personaje['nombre_personaje'])
        cola_aux.arrive(personaje)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())


def buscar_scottlang(cola):
    cola_aux = Queue()
    encontrado = False

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['nombre_personaje'].lower() == 'scott lang':
            print("¡Scott Lang encontrado!")
            print(f"Superhéroe: {personaje['superheroe']} | Género: {personaje['genero']}")
            encontrado = True
        cola_aux.arrive(personaje)

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

    if not encontrado:
        print("Scott Lang no se encuentra en la cola.")


def mostrar_nombres_con_s(cola):
    cola_aux = Queue()
    print("Personajes o superhéroes que comienzan con 'S':")
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['nombre_personaje'].startswith('S') or personaje['superheroe'].startswith('S'):
            print(personaje)
        cola_aux.arrive(personaje)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())


def buscar_carol(cola):
    cola_aux = Queue()
    encontrado = False

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje['nombre_personaje'].lower() == 'carol danvers':
            print("¡Carol Danvers encontrada!")
            print(f"Superhéroe: {personaje['superheroe']}")
            encontrado = True
        cola_aux.arrive(personaje)

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

    if not encontrado:
        print("Carol Danvers no se encuentra en la cola.")
    return encontrado


def main():
    print("a. Nombre del personaje de la superhéroe Capitana Marvel:")
    cap_marvel = buscar_capitana_marvel(cola)
    if cap_marvel:
        print(f"Nombre del personaje: {cap_marvel}")
    else:
        print("Capitana Marvel no encontrada.")

    print("\nb. Nombres de los superhéroes femeninos:")
    mostrar_superheroes_femeninos(cola)

    print("\nc. Nombres de los personajes masculinos:")
    mostrar_personajes_masculinos(cola)

    print("\nd. Determinar el nombre del superhéroe del personaje Scott Lang:")
    buscar_scottlang(cola)

    print("\ne. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S:")
    mostrar_nombres_con_s(cola)

    print("\nf. Determinar si el personaje Carol Danvers se encuentra en la cola:")
    buscar_carol(cola)


if __name__ == '__main__':
    main()
