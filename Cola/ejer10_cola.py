# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, 
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, 
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya 
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 
# 11:43 y las 15:57, y determinar cuántas son.

from my_cola_mejor import Queue



def eliminar_facebook(cola):
    cola_aux = Queue()
    while cola.size() > 0:
        notificacion =  cola.attention()
        if notificacion['aplicacion'] != 'Facebook':
            cola_aux.arrive(notificacion)
    return cola_aux

def mostrar_twitter(cola):
    cola_aux = Queue()
    resultado = Queue()
    while cola.size() > 0:
        notificacion = cola.attention()
        if notificacion['aplicacion'].lower() == 'twitter' and 'python' in notificacion['mensaje'].lower():
            resultado.arrive(notificacion)
        cola_aux.arrive(notificacion)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())
    return resultado

def contar_notificaciones(cola, hora_inicio, hora_fin):
    pila = []
    contador = 0
    cola_aux = Queue()
    while cola.size() > 0:
        notificacion = cola.attention()
        if hora_inicio <= notificacion ['hora']<= hora_fin:
            pila.append(notificacion)
            contador += 1
        cola_aux.arrive(notificacion)
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())
    return pila, contador


def main():
    cola = Queue()

# Ejemplo de notificaciones
    cola.arrive({"hora": "11:30","aplicacion": "Facebook","mensaje": "Nueva foto en tu muro"})
    cola.arrive( {"hora":"11:45", "aplicacion":"Twitter", "mensaje":"Nuevo tweet sobre Python"})
    cola.arrive( {"hora":"12:00", "aplicacion":"Instagram", "mensaje":"Nueva historia"})
    cola.arrive({"hora":"12:30", "aplicacion":"Facebook","mensaje": "Comentario en tu publicación"})
    cola.arrive({"hora":"13:00", "aplicacion":"Twitter", "mensaje":"Python es genial"})
    cola.arrive({"hora":"14:00", "aplicacion":"Facebook","mensaje": "Mensaje nuevo"})
    cola.arrive( {"hora":"15:00", "aplicacion":"Twitter", "mensaje":"Aprendiendo Python"})
    cola.arrive( {"hora":"15:30", "aplicacion":"Instagram", "mensaje":"Nueva foto en tu perfil"})
    cola.arrive( {"hora":"16:00", "aplicacion":"Facebook", "mensaje":"Actualización de estado"})
    cola.arrive({"hora":"16:30", "aplicacion":"Twitter","mensaje": "Python en redes sociales"})
    print("cola original:")
    cola.show()
    cola = eliminar_facebook(cola)
    print("Cola después de eliminar notificaciones de Facebook:")
    cola.show()
    cola_twitter = mostrar_twitter(cola)
    print("Notificaciones de Twitter que contienen 'Python':")
    cola_twitter.show()
    pila, contador = contar_notificaciones(cola, "11:43", "15:57")
    print(f"Cantidad de notificaciones entre las 11:43 y las 15:57: {contador}")
    print("Notificaciones entre las 11:43 y las 15:57:")
    for notificacion in pila:
        print(notificacion)

if __name__ == '__main__':
    main()
