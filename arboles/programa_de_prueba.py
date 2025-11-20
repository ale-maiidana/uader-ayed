from cola_ import Queue
from arbol import BinaryTree  # asumo que tu clase BinaryTree está en arbol.py

# Crear un árbol binario
tree = BinaryTree()

# Insertar algunos valores
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

print("=== Recorridos ===")
print("Pre-orden:")
tree.pre_order()

print("\nIn-orden:")
tree.in_order()

print("\nPost-orden:")
tree.post_order()

print("\nPor niveles:")
tree.by_level()

# Buscar valores
print("\n=== Búsquedas ===")
nodo = tree.search(7)
if nodo:
    print(f"Encontrado: {nodo.value}")
else:
    print("No se encontró el 7")

nodo = tree.search(20)
if nodo:
    print(f"Encontrado: {nodo.value}")
else:
    print("No se encontró el 20")
