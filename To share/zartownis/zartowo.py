import random

tresc1 = """Jak się nazywa żona Popa?


Popowa"""

def tworzenie_zartu(nazwa_pliku, tresc):
    plik = open(nazwa_pliku, "w")
    plik.write(tresc)
    plik.close()

#tworzenie_zartu("zart o Popie", tresc1)

plikus = open("zarty.csv", "r")

#Imports a random joke from the file
with open("zarty1.csv", "r") as file:
   zarty = file.read().splitlines()
   losowy_zart = zarty[random.randint(1,74)]
   print(losowy_zart)
