# Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The 
# Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada 
# misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó, 
# costo de la recompensa. Resolver las siguientes actividades:
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
# de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos 
# quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la 
# que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

from mypila import Stack
pila = Stack()
# Supongamos que Stack ya está importado
boba_fett = Stack()
din_djarin = Stack()

# Datos para Boba Fett
boba_fett.push({'planeta': 'Tatooine', 'capturado': 'Criminal Rodiano', 'recompensa': 4500})
boba_fett.push({'planeta': 'Naboo', 'capturado': 'Contrabandista Twi\'lek', 'recompensa': 6200})
boba_fett.push({'planeta': 'Kamino', 'capturado': 'Desertor Clon', 'recompensa': 7000})
boba_fett.push({'planeta': 'Bespin', 'capturado': 'Espía Imperial', 'recompensa': 5300})
boba_fett.push({'planeta': 'Mustafar', 'capturado': 'Cazarrecompensas traidor', 'recompensa': 8000})

# Datos para Din Djarin (The Mandalorian)
din_djarin.push({'planeta': 'Nevarro', 'capturado': 'Cazarrecompensas rival', 'recompensa': 5100})
din_djarin.push({'planeta': 'Sorgan', 'capturado': 'Mercenario Weequay', 'recompensa': 4600})
din_djarin.push({'planeta': 'Arvala-7', 'capturado': 'Trandoshan agresivo', 'recompensa': 5500})
din_djarin.push({'planeta': 'Tatooine', 'capturado': 'Cazarrecompensas novato', 'recompensa': 4300})
din_djarin.push({'planeta': 'Coruscant', 'capturado': 'Ex-militar rebelde', 'recompensa': 6700})

def mostrar_planetas_visitados(pila):
    pila_aux = Stack()
    while pila.size() > 0:
        mision =pila.pop()
        print (f'planeta visitado: {mision['planeta']}')
        pila_aux.push(mision)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

def calcular_recompensas(pila):
    total_recompensa = 0
    while pila.size() > 0:
        mision = pila.pop()
        total_recompensa += mision['recompensa']
    return total_recompensa

def mayor_fortuna(boba_fett, din_djarin):
    total_boba = calcular_recompensas(boba_fett)
    total_din = calcular_recompensas(din_djarin)
    
    if total_boba > total_din:
        print(f"Boba Fett obtuvo mayor fortuna: {total_boba} créditos galácticos.")
    elif total_din > total_boba:
        print(f"Din Djarin obtuvo mayor fortuna: {total_din} créditos galácticos.")
    else:
        print("Ambos cazarrecompensas obtuvieron la misma fortuna.")

def mision_boba_fett(pila):
    pila_aux = Stack()
    mision_numero = 0
    while pila.size() > 0:
        mision = pila.pop()
        mision_numero += 1
        if mision['capturado'] == 'Han Solo':
            print(f"Boba Fett capturó a Han Solo en la misión número {mision_numero}.")
            break
        pila_aux.push(mision)
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    else:
        print("Boba Fett no capturó a Han Solo.")

def capturas_realizadas(pila):
    contador = 0
    pila_aux = Stack()
    while pila.size() > 0:
        mision = pila.pop()
        contador += 1
        pila_aux.push(mision)
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    print(f"Cantidad de capturas realizadas: {contador}")

def main():
    print("Planetas visitados por Boba Fett:")
    mostrar_planetas_visitados(boba_fett)
    
    print("\nPlanetas visitados por Din Djarin:")
    mostrar_planetas_visitados(din_djarin)
    
    print("\nTotal de créditos galácticos recaudados:")
    total_boba = calcular_recompensas(boba_fett)
    total_din = calcular_recompensas(din_djarin)
    print(f"Boba Fett: {total_boba} créditos galácticos.")
    print(f"Din Djarin: {total_din} créditos galácticos.")
    
    mayor_fortuna(boba_fett, din_djarin)
    
    print("\nMisión en la que Boba Fett capturó a Han Solo:")
    mision_boba_fett(boba_fett)
    
    print("\nCantidad de capturas realizadas por Boba Fett:")
    capturas_realizadas(boba_fett)
    
    print("\nCantidad de capturas realizadas por Din Djarin:")
    capturas_realizadas(din_djarin)
if __name__ == "__main__":
    main()  # Ejecutamos la función principal