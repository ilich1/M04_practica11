def comp_num():
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    if num1 > num2:
        print("El número més gran és", num1)

    elif num2 > num1:
        print("El número més gran és", num2)

    else:
        print("los numeros son iguals")


comp_num()