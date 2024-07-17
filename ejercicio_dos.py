"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
lista = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def numeros_primos(lista):
    return list(filter(es_primo, lista))
primos = numeros_primos(lista)
print(primos)  