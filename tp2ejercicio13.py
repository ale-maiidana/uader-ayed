class nodoPila: 
    def __init__(self, info=None):
        self.info = info
        self.sig = None

class pila: 
    def __init__(self):
        self.cima = None
        self.tamanio = 0
    
    def vacia(self):
        return self.cima is None
    
    def apilar(self, dato):
        nodo = nodoPila(dato)
        nodo.sig = self.cima
        self.cima = nodo 
        self.tamanio += 1

    def desapilar(self):
        if self.vacia():
            return None
        else:
            x = self.cima.info
            self.cima = self.cima.sig
            self.tamanio -= 1
            return x
    
    def tamanio_pila(self):
        return self.tamanio
    
    def mostrar_pila(self):
        paux = pila()
        while not self.vacia():
            dato = self.desapilar()
            print(dato)
            paux.apilar(dato)
        while not paux.vacia():
            self.apilar(paux.desapilar())

# Función a. Buscar modelo Mark XLIV
def buscar_modelo(p, campo):
    paux = pila()
    encontrado = False 
    while not p.vacia():
        dato = p.desapilar()
        if dato[campo].lower() == 'mark xliv':
            encontrado = True 
            print(f"El modelo {dato['modelo']} fue utilizado en la película {dato['pelicula']}")
        paux.apilar(dato)
    while not paux.vacia():
        p.apilar(paux.desapilar())
    if not encontrado:
        print('El modelo no fue utilizado en ninguna película')

# Función b. Mostrar modelos dañados
def mostrar_danados(p):
    paux = pila()
    while not p.vacia():
        dato = p.desapilar()
        if dato['estado'] == 'dañado':
            print(f"El modelo {dato['modelo']} quedó dañado")
        paux.apilar(dato)
    while not paux.vacia():
        p.apilar(paux.desapilar())

# Función c. Eliminar modelos destruidos
def eliminar_destruidos(p):
    paux = pila()
    while not p.vacia():
        dato = p.desapilar()
        if dato['estado'] == 'destruido':
            print(f"El modelo {dato['modelo']} fue destruido y eliminado")
        else:
            paux.apilar(dato)
    while not paux.vacia():
        p.apilar(paux.desapilar())

# Función d. Cargar modelo desde teclado
def cargar_modelo(p):
    respuesta = input('¿Desea cargar un modelo, película y estado? (s/n): ').lower()
    if respuesta == 's':
        modelo = input('Ingrese el modelo: ')
        pelicula = input('Ingrese la película: ')
        estado = input('Ingrese el estado: ')
        p.apilar({'modelo': modelo, 'pelicula': pelicula, 'estado': estado})
    else:
        print('No se cargaron datos.')

# Función e. Agregar modelo sin repetir en una película
def agregar_modelo(p, modelo, pelicula, estado):
    paux = pila()
    repetido = False
    while not p.vacia():
        dato = p.desapilar()
        if dato['modelo'].lower() == modelo.lower() and dato['pelicula'].lower() == pelicula.lower():
            repetido = True
        paux.apilar(dato)
    
    while not paux.vacia():
        p.apilar(paux.desapilar())
    
    if repetido:
        print(f"El modelo {modelo} ya fue utilizado en la película {pelicula}")
    else:
        p.apilar({'modelo': modelo, 'pelicula': pelicula, 'estado': estado})
        print(f"Modelo {modelo} agregado correctamente.")

# Función f. Mostrar trajes usados en dos películas específicas
def mostrar_trajes(p):
    paux = pila()
    while not p.vacia():
        dato = p.desapilar()
        if dato['pelicula'].lower() in ['spider-man homecoming', 'capitan america civil war']:
            print(f"El modelo {dato['modelo']} fue utilizado en la película {dato['pelicula']}")
        paux.apilar(dato)
    while not paux.vacia():
        p.apilar(paux.desapilar())

# Cuerpo principal del programa
if __name__ == "__main__":
    p = pila()
    p.apilar({'modelo': 'Mark I', 'pelicula': 'Iron Man 2008', 'estado': 'destruido'})
    p.apilar({'modelo': 'Mark II', 'pelicula': 'Iron Man 2008', 'estado': 'impecable'})
    p.apilar({'modelo': 'Mark III', 'pelicula': 'Iron Man 2008', 'estado': 'destruido'})
    p.apilar({'modelo': 'Mark IV', 'pelicula': 'Iron Man 2', 'estado': 'dañado'})
    p.apilar({'modelo': 'Mark V', 'pelicula': 'Iron Man 2', 'estado': 'dañado'})
    p.apilar({'modelo': 'Mark VI', 'pelicula': 'The Avengers', 'estado': 'dañado'})
    p.apilar({'modelo': 'Mark VII', 'pelicula': 'The Avengers', 'estado': 'destruido'})
    p.apilar({'modelo': 'Mark XLVII', 'pelicula': 'spider-man homecoming', 'estado': 'impecable'})
    p.apilar({'modelo': 'Mark XLIV', 'pelicula': 'capitan america civil war', 'estado': 'impecable'})

    while True:
        print("\n--- Menú de funciones ---")
        print("1. Buscar modelo 'Mark XLIV'")
        print("2. Mostrar modelos dañados")
        print("3. Eliminar modelos destruidos")
        print("4. Cargar nuevo modelo")
        print("5. Agregar modelo 'Mark LXXXV'")
        print("6. Mostrar modelos de películas específicas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_modelo(p, 'modelo')
        elif opcion == "2":
            mostrar_danados(p)
        elif opcion == "3":
            eliminar_destruidos(p)
        elif opcion == "4":
            cargar_modelo(p)
        elif opcion == "5":
            agregar_modelo(p, 'Mark LXXXV', 'endgame', 'impecable')
        elif opcion == "6":
            mostrar_trajes(p)
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
