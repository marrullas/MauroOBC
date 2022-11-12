import functools, operator
numeros = [20,21,22,23,24,25,26,27,28,29,30,31,32,33]

def sumarImpares(n):    
    if n % 2 != 0:
        return True
    return False
resultados = filter(sumarImpares, numeros)

print(list(resultados))

lista = list(resultados)


print("La suma de los impares es : ", end="")
print(functools.reduce(operator.add, numeros,0))
