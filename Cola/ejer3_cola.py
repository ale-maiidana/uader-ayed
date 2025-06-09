# 3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar
# si es un palíndromo

from my_cola_mejor import Queue

def palindromo(cola):
    pila =[]
    while cola.size()> 0:
        caracter = cola.attention()
        pila.append(caracter)
        while pila:
            if caracter == pila.pop():
                return True
    return False

def main():
    cola = Queue()

    def ingresar_palabras():
        while True:
            palabra = input ('ingrese 2 palabras o "fin" para terminar: ')
            if palabra.lower()== 'fin':
                break
            if palabra.isalpha():
                for caracter in palabra:
                    cola.arrive(caracter)
            else:
                print('Por favor, ingrese solo caracteres alfabéticos.')
    ingresar_palabras()
    print('Cola original:')
    cola.show()
    if palindromo(cola):
        print('La secuencia es un palíndromo.')
    else:
        print('La secuencia no es un palíndromo.')
if __name__ == '__main__':
    main()