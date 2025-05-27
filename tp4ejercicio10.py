class nodoCola:
    def __init__(self):
        self.info = None
        self.sig = None

class cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato

def cola_vacia(cola):
    return cola.frente is None

def en_frente(cola):
    return cola.frente.info

from my_cola import cola, arribo, atencion, cola_vacia, en_frente

notificaciones = cola()
# Ejemplo de notificaciones
arribo(notificaciones, {"hora": "11:30","aplicacion": "Facebook","mensaje": "Nueva foto en tu muro"})
arribo(notificaciones, {"hora":"11:45", "aplicacion":"Twitter", "mensaje":"Nuevo tweet sobre Python"})
arribo(notificaciones, {"hora":"12:00", "aplicacion":"Instagram", "mensaje":"Nueva historia"})
arribo(notificaciones, {"hora":"12:30", "aplicacion":"Facebook","mensaje": "Comentario en tu publicación"})
arribo(notificaciones, {"hora":"13:00", "aplicacion":"Twitter", "mensaje":"Python es genial"})
arribo(notificaciones, {"hora":"14:00", "aplicacion":"Facebook","mensaje": "Mensaje nuevo"})
arribo(notificaciones, {"hora":"15:00", "aplicacion":"Twitter", "mensaje":"Aprendiendo Python"})
arribo(notificaciones, {"hora":"15:30", "aplicacion":"Instagram", "mensaje":"Nueva foto en tu perfil"})
arribo(notificaciones, {"hora":"16:00", "aplicacion":"Facebook", "mensaje":"Actualización de estado"})
arribo(notificaciones, {"hora":"16:30", "aplicacion":"Twitter","mensaje": "Python en redes sociales"})

def eliminar_facebook(c):
    caux = cola()
    while not cola_vacia(c):
        notificaciones = atencion(c)
        if notificaciones ['aplicacion'].lower() != 'facebook':
            arribo(caux, notificaciones)
    while not cola_vacia(caux):
        arribo(c, atencion(caux))

def notificaciones_twitter_python(c):
    caux = cola()
    while not cola_vacia(c):
        notificaciones = atencion(c)
        if notificaciones['aplicacion'].lower() == 'twitter' and 'python' in notificaciones["mensaje"].lower():
            arribo(caux, notificaciones)
    
    while not cola_vacia(caux):
        print(atencion(caux))

def notificaciones_entre_horas(c, hora_inicio, hora_fin):
    pila = []
    caux = cola()
    contador = 0

    while not cola_vacia(c):
        notificacion = atencion(c)
        hora_notificacion = notificacion['hora']
        
        if hora_inicio <= hora_notificacion <= hora_fin:
            pila.append(notificacion)
            contador += 1
        else:
            arribo(caux, notificacion)

    while not cola_vacia(caux):
        arribo(c, atencion(caux))

    return contador, pila

     

while True:
    print("\n--- MENÚ DE NOTIFICACIONES ---")
    print("1. Eliminar notificaciones de Facebook")
    print("2. Mostrar notificaciones de Twitter con 'Python'")
    print("3. Mostrar notificaciones entre las 11:43 y 15:57")
    print("4. Salir")

    opcion = input("Elegí una opción (1-4): ")

    if opcion == '1':
        eliminar_facebook(notificaciones)
        print(" Notificaciones de Facebook eliminadas.")
    elif opcion == '2':
        print(" Notificaciones de Twitter con 'Python':")
        notificaciones_twitter_python(notificaciones)
    elif opcion == '3':
        cantidad, pila = notificaciones_entre_horas(notificaciones, "11:43", "15:57")
        print(f"\n Total de notificaciones entre 11:43 y 15:57: {cantidad}")
        for n in pila:
            print(n)
    elif opcion == '4':
        print(" Saliendo del programa.")
        break
    else:
        print(" Opción inválida. Probá de nuevo.")
