

def tipoano(ano):
    if(ano % 4 == 0 and (ano % 100  != 0 or ano % 400 == 0)):
        print(ano, " es un año Bisiesto")
    else:
        print(ano, " no Bisiesto")

tipoano(2020)