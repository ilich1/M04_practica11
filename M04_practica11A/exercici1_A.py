def compara_numeros():
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))
    if num1 > num2:
        print("El número mayor es {} y el número menor es {}".format(num1, num2))
    elif num2 > num1:
        print("El número mayor es {} y el número menor es {}".format(num2, num1))
    else:
        print("Los números son iguales")


compara_numeros()