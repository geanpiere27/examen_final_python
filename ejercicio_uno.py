"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
list_numeros = [5,8,9,6,2,10]
def lista(numeros):
    menor = min(numeros)
    mayor = max(numeros)

    return {f"numero menor": menor, "numero mayor": mayor}
salida = lista(list_numeros)
print(salida)  
