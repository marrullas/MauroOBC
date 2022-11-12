#lalista = ['Canada', 'Austria', 'Chile', 'Mexico', 'Portugal', 'Colombia', 'Chile', 'Canada']
paises = []
pais = ''
while pais != '1':
    pais = input("Digite nombre de un pais o 1 para salir': ")
    if(pais != '1'):
        paises.append(pais)

set_lista = set(paises)

ordenada = sorted(list(set_lista))

print(ordenada)


