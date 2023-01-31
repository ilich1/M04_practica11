import random

def adivina_el_numero():
  numero_a_adivinar = random.randrange(0,100)
  adivinanza = int(input("Adivina el número entre 0 y 100: "))
  while adivinanza != numero_a_adivinar:
    if adivinanza < numero_a_adivinar:
      print("El número es mayor {} ".format(adivinanza))
      adivinanza = int(input("Adivina de nuevo el número: "))
    else:
      print("El número es más pequeño {}".format(adivinanza))
      adivinanza = int(input("Adivina de nuevo el número: "))
  print("¡Muy bien! ¡Has adivinado el número!")


adivina_el_numero()