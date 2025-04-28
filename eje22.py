# 22. El problema de la mochila Jedi.
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.


mochila = ['sable de luz', 'agua', 'cuchillo', 'linterna', 'curitas', 'don satur', 'mate', 'anteojos'];

def ordenamiento(mochila):
    for i in range(len(mochila)):
        for j in range(i + 1, len(mochila)):
            if mochila[i] > mochila[j]:
                mochila[i], mochila[j] = mochila[j], mochila[i]
    return mochila



# def usar_la_fuerza (mochila, buscado, pri, last, cont): 
#     middle=(pri + last) // 2
    
#     if pri >= last :
#         return -1, cont + 1
#     elif mochila [middle]== buscado:
#         return middle, cont + 1
#     else:
#         if mochila [middle]> buscado:
#             return usar_la_fuerza(mochila,buscado,pri , last -1, cont + 1)
#         else:
#             return usar_la_fuerza(mochila, buscado, middle + 1, last, cont + 1)
#         return cont

def usar_la_fuerza(mochila, buscado):
    pos = -1
    pri = 0
    ult = len(mochila) - 1
    cont = 0  

    while pri <= ult and pos == -1:
        medio = (pri + ult) // 2
        if mochila[medio] == buscado:
            pos = medio
        else:
            if mochila[medio] > buscado:
                ult = medio - 1
            else:
                pri = medio + 1
            cont += 1  
    return pos, cont  


buscado = 'sable de luz'

mochila_ordenada = ordenamiento(mochila)
pos, cont = usar_la_fuerza(mochila_ordenada, buscado) 

if pos != -1:
    print(f'El sable de luz fue encontrado (posición {pos}) después de sacar {cont} objetos.')
else:
    print('El sable de luz no está en la mochila.')


