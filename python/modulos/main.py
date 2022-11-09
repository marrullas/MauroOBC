import calculadora


def main():#función que se ejecuta
    num1 = int(input("Digite numero 1: "))
    num2 = int(input("Digite numero 2: "))

    print("La suma de ", num1, " mas ", num2, " es: ", calculadora.suma(num1,num2))
    print("La resta de ", num1, " mas ", num2, " es: ", calculadora.resta(num1,num2))
    print("La multiplicación de ", num1, " mas ", num2, " es: ", calculadora.multiplicar(num1,num2))
    print("La división de ", num1, " mas ", num2, " es: ", calculadora.dividir(num1,num2))

if __name__ == '__main__': #se usa como convención de py para que no existan variables globales en los modulos
    main()