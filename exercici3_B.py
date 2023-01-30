def declaracio_impuestos():
    edat = int(input("Introdueix la teva edat:" ))
    ingressos = int(input("Introdueix els teus ingressos mensuals: "))
    if edat >= 18 and ingressos > 1200:
        print("És necessani que facis la declaració d'impuedstos")
    else:
        print("Encara no pots fer la declaració ")

declaracio_impuestos()
