maka = float(input("Podaj ile masz gram mąki"))
drozdze = float(input("Podaj ile masz gram suchych drozdzy"))
sol = float(input("Podaj ile masz łyczeczek soli"))
cukier = float(input("Podaj ile masz łyczeczek cukru"))
woda = float(input("Podaj ile masz gramów letniej wody"))
olej = float(input("Podaj ile masz łyżek oleju"))
#list of needed ingredients
maka_needed = 150
drozdze_needed = 10
sol_needed = 0.5
cukier_needed = 0.25
woda_needed = 69
olej_needed = 0.5

piczka = [maka_needed, drozdze_needed, sol_needed, cukier_needed, woda_needed, olej_needed]

porcja_maka = maka/maka_needed
porcja_drozdze = drozdze/drozdze_needed
porcja_sol = sol/sol_needed
porcja_cukier = cukier/cukier_needed
porcja_woda = woda/woda_needed
porcja_olej = olej/olej_needed

min_porc = int(min(porcja_maka, porcja_drozdze, porcja_sol, porcja_cukier, porcja_woda, porcja_olej))
if min_porc == 0:
      print("\nChuja zrobisz a nie pizzę\n")
elif min_porc == 1:
      print("Możesz zrobić 1 porcję")
elif min_porc >1:
      print("Liczba porcji możliwych do zrobienia: \n", min_porc)

maka_left = maka - (min_porc*maka_needed)
drozdze_left = drozdze - (min_porc*drozdze_needed)
sol_left = sol - (min_porc*sol_needed)
cukier_left = cukier - (min_porc*cukier_needed)
woda_left = woda - (min_porc*woda_needed)
olej_left = olej - (min_porc*olej_needed)


if maka_left < maka_needed:
      print("dokup", maka_needed-maka_left, "g mąki, aby liczba porcji wynosiła:", min_porc+1)
if drozdze_left < drozdze_needed:
      print("dokup", drozdze_needed-drozdze_left, "g drożdży, aby liczba porcji wynosiła:", min_porc+1)
if sol_left < sol_needed:
      print("dokup", sol_needed-sol_left, "łyczeczek soli, aby liczba porcji wynosiła:", min_porc+1)
if cukier_left < cukier_needed:
      print("dokup", cukier_needed-cukier_left, "łyczeczek cukru, aby liczba porcji wynosiła:", min_porc+1)
if woda_left < woda_needed:
      print("zdobądź", woda_needed-woda_left, "g wody, aby liczba porcji wynosiła:", min_porc+1)
if olej_left < olej_needed:
      print("zdobądź", olej_needed-olej_left, "g oleju, aby liczba porcji wynosiła:", min_porc+1)

"""
Testowa wersja z wodą
woda = float(input("ile jest litrów wody? "))
sok = float(input("ile jest litrów soku? "))

woda_needed = 0.5
sok_needed = 0.1
woda_sokowa = [woda_needed, sok_needed]

porcje_wody = (woda/woda_needed)
porcje_soku = (sok/sok_needed)

print("Z z tej ilości wodu uda się zrobić",
      int(porcje_wody), "soków. Do następnej porcji brakuje",
      woda-(porcje_wody*woda_needed)
      )

print("Z tej ilości soku uda się zrobić",
      int(porcje_soku), "soków",
      sok-(porcje_soku*sok_needed)
      )
min_porc = min(porcje_soku, porcje_wody)

print("Minimalna ilość porcji to", min_porc)

woda_left = woda - (min_porc*woda_needed)
sok_left = sok - (min_porc*sok_needed)
print("zostalo", woda_left, "wody, oraz", sok_left, "soku")

if woda_left == 0:
      print("dokup", woda_needed, "wody, aby mieć", min_porc+1, "porcji")
if sok_left == 0:
      print("dokup", sok_needed, "soku aby mieć", min_porc+1, "porcji")"""









