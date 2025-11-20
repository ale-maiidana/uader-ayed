# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from arbol import BinaryTree
from criaturas import creatures      

arbol = BinaryTree()


# CARGA INICIAL DEL ÁRBOL

for name, data in creatures.items():
    arbol.insert(name, data)

# a) Listado inorden de criaturas y quiénes la derrotaron

def listado_inorden(tree):
    def __inorden(root):
        if root:
            __inorden(root.left)
            print(f"{root.value} — derrotado por: {root.other_values['defeated_by']}")
            __inorden(root.right)
    __inorden(tree.root)

print("\na) Listado inorden:")
listado_inorden(arbol)


# b) Cargar descripción a cada criatura (ejemplo básico)


def agregar_descripcion(tree, nombre, descripcion):
    nodo = tree.search(nombre)
    if nodo:
        nodo.other_values["description"] = descripcion


agregar_descripcion(arbol, "Medusa", "Gorgona derrotada por Perseo")


# c) Mostrar toda la información de Talos

def mostrar_info(tree, nombre):
    nodo = tree.search(nombre)
    if nodo:
        print(f"\nInformación de {nombre}:")
        print(nodo.other_values)

mostrar_info(arbol, "Talos")


# d) Los 3 héroes o dioses que derrotaron más criaturas

def top3_derrotadores(tree):
    contador = {}

    def __rec(root):
        if root:
            heroe = root.other_values["defeated_by"]
            if heroe not in ("", None):
                contador[heroe] = contador.get(heroe, 0) + 1
            __rec(root.left)
            __rec(root.right)

    __rec(tree.root)

    top3 = sorted(contador.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\nd) Top 3 héroes/dioses que derrotaron más criaturas:")
    for h, c in top3:
        print(f"{h}: {c}")

top3_derrotadores(arbol)


# e) Criaturas derrotadas por Heracles

def derrotadas_por(tree, nombre):
    print(f"\ne) Criaturas derrotadas por {nombre}:")
    def __rec(root):
        if root:
            if root.other_values["defeated_by"] == nombre:
                print(root.value)
            __rec(root.left)
            __rec(root.right)
    __rec(tree.root)

derrotadas_por(arbol, "Heracles")


# f) Criaturas no derrotadas

def no_derrotadas(tree):
    print("\nf) Criaturas no derrotadas:")
    def __rec(root):
        if root:
            if root.other_values["defeated_by"] == "":
                print(root.value)
            __rec(root.left)
            __rec(root.right)
    __rec(tree.root)

no_derrotadas(arbol)


# g) campo "capturada" ya está cargado en el diccionario


# h) marcar criaturas capturadas por Heracles

def marcar_capturadas(tree):
    atrapadas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabali de Erimanto"]
    for criatura in atrapadas:
        nodo = tree.search(criatura)
        if nodo:
            nodo.other_values["captured_by"] = "Heracles"

marcar_capturadas(arbol)


# i) búsqueda por coincidencia

def buscar_por_prefijo(tree, prefijo):
    print(f"\ni) Búsqueda por prefijo '{prefijo}':")
    resultados = tree.proximity_search(prefijo)
    for nodo in resultados:
        print(nodo.value)

buscar_por_prefijo(arbol, "Ca")


# j) eliminar Basilisco y Sirenas

print("\nj) Eliminando Basilisco y Sirenas...")
arbol.delete("Basilisco")
arbol.delete("Sirenas")


# k) modificar “Aves del Estínfalo”

aves = arbol.search("Aves del Estinfalo")
if aves:
    aves.other_values["defeated_by"] = "Heracles (varias)"


# l) modificar Ladón → Dragón Ladón

ladon = arbol.delete("Ladon")
if ladon[0] is not None:
    datos = ladon[1]
    arbol.insert("Dragon Ladon", datos)

# m) listado por niveles

print("\nm) Listado por niveles:")
arbol.by_level()


# n) criaturas capturadas por Heracles

def capturadas_por(tree, nombre):
    print(f"\nn) Criaturas capturadas por {nombre}:")
    def __rec(root):
        if root:
            if root.other_values["captured_by"] == nombre:
                print(root.value)
            __rec(root.left)
            __rec(root.right)
    __rec(tree.root)

capturadas_por(arbol, "Heracles")
