import random
latwa_wersja_trupa = [">",">-",">--",">-->",">-->-",">-->--",">-->--)",">-->--):"]
liczba_wymyslona = random.randint(1, 9)
zle = []
negatywne_odpowiedzi = ["Nooo nieee....", "Nie, to nie to.",
                        "Leć dalej!","Domyśl się!",
                        "Zgaduj, zgaduj!", "Jeszcze raz!",
                        "No nie wiem...", "Może coś innego?",
                        "Myśl jak komputer!", "Try again!"
                        ]
def czy_to(liczba, proba, liczba_wymyslona, zle):
    while liczba != liczba_wymyslona:
        liczba = int(input("Podaj liczbe: \n"))
        if liczba == liczba_wymyslona:
            print("Super")
            return
        else:
            zle += str(liczba)
            odp = random.choice(negatywne_odpowiedzi)
            print(odp)
            print(random.choice((
                ("Liczba jest mniejsza niż", liczba_wymyslona + random.randint(1, 4)),
                ("Liczba jest większa niż", liczba_wymyslona - random.randint(1, 4)),
                ("Czy liczba jest parzysta?", liczba_wymyslona % 2 == 0),
                ("Czy liczba jest nieparzysta?", liczba_wymyslona % 3 == 0),
                ("Czy liczba jest podzielna przez 2?", liczba_wymyslona % 2 == 0),
                ("Czy liczba jest podzielna przez 3?", liczba_wymyslona % 3 == 0),
                ("Liczba jest pomiędzy",liczba_wymyslona - random.randint(1, 4),
                             "a", liczba_wymyslona + random.randint(1, 4)))))
            print(latwa_wersja_trupa[proba-1])
            print("Nie są to liczby", zle)
            proba += 1
            if proba == 8:
                print(latwa_wersja_trupa[proba - 1])
                print("Przegrana.\n Koniec gry")
                break

czy_to(1,1,liczba_wymyslona, zle)
