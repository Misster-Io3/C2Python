# El programa que desarrollarás debe tener las siguientes características: 
# Que en un bucle infinito solicite al usuario una letra (debes especificar al usuario la condición para terminar el programa. Por ejemplo, para salir, escriba alto, presione 0 o cualquier otra que se te ocurra).
# Harás una función que imprima en la pantalla la letra siguiente en el alfabeto y la letra anterior a la ingresada.
# El programa debe continuar en el bucle hasta que el usuario decida salir del programa.

 
def letra_siguiente(letra):    # Función que devuelve la letra siguiente en el alfabeto
    letra_siguiente = chr(ord(letra) + 1) # Se obtiene la letra siguiente en el alfabeto con la función chr()
    return letra_siguiente  

letra = input("Ingrese una letra: ")
while letra != "alto":
    print(letra_siguiente(letra)) # imprime la letra siguiente en el alfabeto
    letra = input("Ingrese una letra: ") # solicita la letra al usuario para continuar el programa y se repite el bucle infinito hasta que el usuario ingrese "alto"


# E}jemplo de uso de ciclos while

while