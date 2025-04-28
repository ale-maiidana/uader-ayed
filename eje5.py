#Desarrollar una función que permita convertir un número romano en un número decimal.
 # Diccionario con los valores de cada símbolo romano
valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def ingresar_numero_romano():
    # Pedimos al usuario que ingrese un número romano
    numero_romano = input("Ingrese un número romano: ").upper()
    
    # Verificamos si el número ingresado es válido
    for letra in numero_romano:
        if letra not in valores:
            print(f"El símbolo '{letra}' no es válido.")
            return None
    
    return numero_romano

def romano_a_decimal(romano):
    if romano is None:
        return None
    
    # Inicializamos el valor decimal y el valor anterior
    decimal = 0
    anterior = 0
    
    # Recorremos el número romano de derecha a izquierda
    for i in reversed(range(len(romano))):
        letra = romano[i]
        valor = valores[letra]
        
        # Si el valor actual es menor que el anterior, restamos
        if valor < anterior:
            decimal -= valor
        else:
            decimal += valor
        
        anterior = valor
    
    return decimal

# Llamamos a las funciones
numero = ingresar_numero_romano()
if numero is not None:
    resultado = romano_a_decimal(numero)
    print(f"El número romano {numero} equivale a {resultado} en decimal.")
