"""Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres."""


from mylista import List

lista = List()

lista.append('a')
lista.append('f')
lista.append('j')
lista.append('e')
lista.append('p')

def delete_vowels(lista):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for letter in lista[:]:
        if letter in vowels:
            lista.delete_value(letter)
    
    return lista

print(delete_vowels(lista))
        
     