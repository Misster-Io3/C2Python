lista = ['Este es mi primer archivo\n', 'Este es mi primer archivo 2Este es mi primer archivo 3\n', '\tEste es mi primer archivo 4']

# Al segundo elemento de la lista lo separamos despues del 2
lista[1] = 'Este es mi primer archivo 2\n'
# inserta un elemento en la posicion 2
lista.insert(2, 'Este es mi primer archivo 3\n')
print(lista)