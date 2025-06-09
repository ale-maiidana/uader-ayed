#1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

""" Un nodo es cada "cajita" de la lista enlazada, que guarda un dato y apunta al siguiente.
    Un nodo es una estructura que contiene un dato (valor) y una referencia (puntero) al siguiente nodo de la lista.
    En listas enlazadas, cada elemento es un nodo.
"""

from mylista import List

personas = [
    {"nombre": "juan", "apellido": "perez", "dni": "23.244.050"},
    {"nombre": "agostina", "apellido": "rios", "dni": "22.349.340"},
    {"nombre": "lucas", "apellido": "mendoza", "dni": "29.644.054"},
    {"nombre": "brian", "apellido": "percincula", "dni": "25.364.090"},
    {"nombre": "juana", "apellido": "perez", "dni": "22.004.058"},    
]

class Personas:

    def __init__ (self, nombre , apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__ (self):
        return f" {self.nombre} - {self.apellido} - {self.dni}"
        #como estan aca es como se muestran en consola (nombre - apellido - dni)

#creo la lista
mi_lista = List()


#cargo la lista
for persona in personas:
    #for persona(variable) in personas(lista):

    perso = Personas (
    #perso(variable) = Personas(clase) (
        nombre = persona ["nombre"],
        #nombre(variable) = persona(variable del for) ["nombre"]--> es la clave del diccionario para entrar al noombre de la persona      
        apellido = persona ["apellido"],
        dni = persona["dni"],
    )
    mi_lista.append(perso)
    #mi_lista.append(perso) --> agrego a la lista el objeto perso que es de la clase Personas
  # en cada ciclo se agrega uno distinto y asi hasta terminar.

"""
    Procesa una lista de diccionarios con información de personas y crea objetos de la clase Personas.

    Esta función recibe una lista de diccionarios donde cada diccionario contiene información
    sobre una persona (nombre, apellido y DNI). Por cada elemento en la lista, crea un objeto
    de la clase Personas y lo añade a una lista.

    Parámetros:
    personas (list): Una lista de diccionarios, donde cada diccionario debe contener las claves:
                     - 'nombre' (str): El nombre de la persona
                     - 'apellido' (str): El apellido de la persona
                     - 'dni' (str/int): El documento de identidad de la persona

    Retorna:
    list: Una lista de objetos de la clase Personas creados a partir de los datos de entrada
"""   

#mostramos la lista 
print("Lista cargada:")
mi_lista.show()
print("--------")
print(f"La cantidad de nodos (elementos) en la lista es: {len(mi_lista)}")