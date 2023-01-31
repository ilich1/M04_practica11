def mostrar_nombre():
  nombres = ['Juan', 'Pedro', 'María', 'Ana', 'Lucía']
  nombre = input("Ingresa un nombre: ")
  if nombre in nombres:
    if nombre == 'Juan':
      print("Bienvenido {}".format(nombre))
    elif nombre == 'Pedro':
      print("Bienvenido {}".format(nombre))
    elif nombre == 'María':
      print("Bienvenida {}".format(nombre))
    elif nombre == 'Ana':
      print("Bienvenida {}".format(nombre))
    else:
      print("Bienvenida {}".format(nombre))
  else:
    print("El nombre {} no está en la lista".format(nombre))

mostrar_nombre()