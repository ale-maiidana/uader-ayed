# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un
# algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un
# villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar
# su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver
# las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

import sys

sys.path.append("./Clases")
sys.path.append("./Parciales/Parcial 1")
from arbol import BinaryTree
from superheroes import superheroes

arbol = BinaryTree()

# a.
for superheroes in superheroes:
    arbol.insert(superheroes["name"], superheroes)


# b.
def villain_in_order(tree):
    def __villain_in_order(root):
        if root is not None:
            __villain_in_order(root.left)
            if root.other_values["is_villain"]:
                print(root.value)
            __villain_in_order(root.right)

    __villain_in_order(tree.root)



print("b) Listado alfabéticamente de villanos: ")
villain_in_order(arbol)


# c.
def show_superheroes_with_c(tree):
    def __show(root):
        if root is not None:
            __show(root.left)
            if root.value.startswith("C"):
                print(root.value)
            __show(root.right)

    __show(tree.root)



print("c) Listado de superheroes que empiezan con C: ")
show_superheroes_with_c(arbol)


# d.
def count_superheroes(tree):
    def __count(root):
        if root is None:
            return 0
        is_hero = not root.other_values["is_villain"]
        return (1 if is_hero else 0) + __count(root.left) + __count(root.right)

    return __count(tree.root)



print(f"d) Cantidad de superheroes: {count_superheroes(arbol)
}")


# e.
def modify_doctor_strange(tree, old_name, new_name):
    searched = tree.proximity_search("Dr")
    if searched:
        for node in searched:
            if node.value == old_name:
                deleted_value, other_values = tree.delete(old_name)
                other_values["name"] = new_name
                tree.insert(new_name, other_values)
                print(f"e) Se ha modificado {old_name} por {new_name}")
                return
        print(f"e) Se encontró 'Dr', pero no {old_name}.")
    else:
        print("e) No se encontró nada que empiece con 'Dr'.")



modify_doctor_strange(arbol, "Dr Strange", "Doctor Strange")
arbol.in_order()
print()


# f.
def superheroes_post_order(tree):
    def __post(root):
        if root is not None:
            __post(root.right)
            print(root.value)
            __post(root.left)
    __post(tree.root)



print("f) Listado descendente de superheroes: ")
superheroes_post_order(arbol)


# g.
def generate_forest_in_order(tree):
    villain_tree = BinaryTree()
    heroes_tree = BinaryTree()

    def __generate(root):
        if root is not None:
            __generate(root.left)

            if root.other_values["is_villain"]:
                villain_tree.insert(root.value, root.other_values)
            else:
                heroes_tree.insert(root.value, root.other_values)

            __generate(root.right)

    __generate(tree.root)
    return heroes_tree, villain_tree
   
heroes_tree, villain_tree = generate_forest_in_order(arbol)



# g.I)
def node_counter(tree):
    def __count(root):
        if root is None:
            return 0
        return 1 + __count(root.left) + __count(root.right)

    return __count(tree.root)



print(f"g.I) Cantidad de nodos del árbol de héroes: {node_counter(heroes_tree)}")
print(f"g.I) Cantidad de nodos del árbol de villanos: {node_counter(villain_tree)}")


# g.II)
def in_order(tree):
    def __in_order(root):
        if root is not None:
            __in_order(root.left)
            print(root.value)
            __in_order(root.right)

    __in_order(tree.root)



print("g.II) Barrido ordenado alfabéticamente del árbol de héroes: ")
in_order(heroes_tree)
print("g.II) Barrido ordenado alfabéticamente del árbol de villanos: ")
in_order(villain_tree)