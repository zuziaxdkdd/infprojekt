from Poboczne import Teksty
from random import randint
import random

t = Teksty()
milosc = t.milosc
szczescie = t.szczescie
smutek = t.smutek
gniew = t.gniew
money = t.money

gry = [
    '1 - CoinFlip',
    '2 - Blackjack',
    '3 - ',
    '4 - Wyjdz'
]

class MiniGierki:

    def listagier(self, t):

        xyz = ''

        while xyz == '':

            print("---"*10)
            print("Wybierz jedną z gier:")
            for el in gry:
                print(el)

            wybor = input("Numer - ")
            if wybor == '1':
                game = CoinFlipGame()
                game.gra(t)
            if wybor == '2':
                game = Blackjack()
                game.gra(t)
            if wybor == '4':
                break


class CoinFlipGame:
    def __init__(self):
        self.wynik = None

    def rzuc_monetą(self):
        self.wynik = random.choice(['1', '2'])

    def gra(self, t):
        print("---"*10)
        print("Witaj w grze Coin Flip!")
        self.rzuc_monetą()
        
        print("Zgadnij co będzie: \n 1 - orzel \n 2 - reszka")
        zgaduj = input("Numer - ")
        
        if zgaduj == self.wynik:
            print(f"Odgadłxś poprawnie! Wynik to - {self.wynik}.")
            x = randint(5,10)
            t.money += x
            print(f"Wygrałxś {x}$!!! Masz aktualnie {t.money}$ na koncie!!!")
        elif zgaduj == '200coin':
            t.money += 200
        else:
            print(f"Niestety, nie odgadłxś...")


class Blackjack:
    def __init__(self):
        self.talia = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 
        random.shuffle(self.talia)
        self.reka_gracza = []
        self.reka_krupiera = []

    def rozdaj_karty(self):
        self.reka_gracza.append(self.talia.pop())
        self.reka_gracza.append(self.talia.pop())

        self.reka_krupiera.append(self.talia.pop())
        self.reka_krupiera.append(self.talia.pop())

    def suma_reki(self, reka):
        suma = sum(reka)
        if suma > 21 and 11 in reka:
            reka[reka.index(11)] = 1
            suma = sum(reka)
        return suma

    def sprawdz_wygrana(self, t):
        suma_gracza = self.suma_reki(self.reka_gracza)
        suma_krupiera = self.suma_reki(self.reka_krupiera)

        kasa = randint(10,20)

        if suma_gracza > 21:
            t.money -= kasa
            return f"Przegrałxś!!! Przekroczyłxś 21 punktów. Straciłxś {kasa}$! Masz teraz {t.money}$ na koncie"
        elif suma_krupiera > 21 or suma_gracza > suma_krupiera:
            t.money += kasa 
            return f"Wygrałxś!!! Zyskałxś {kasa}$! Masz teraz {t.money}$ na koncie"
        elif suma_gracza == suma_krupiera:
            return "Remis!"
        else:
            t.money -= kasa
            return f"Przegrałxś!!! Straciłxś {kasa}$! Masz teraz {t.money}$ na koncie "

    def gra(self, t):
        print("---"*10)
        print("Witaj w grze Blackjack!")

        self.rozdaj_karty()
        print(f"Twoje karty: {self.reka_gracza} (Razem: {self.suma_reki(self.reka_gracza)})")
        print(f"Karta krupiera: {self.reka_krupiera[0]}")

        while True:
            print("Czy chcesz dobrać kartę?: \n 1 - tak \n 2 - nie")
            decyzja = input("Numer - ")
            if decyzja == '1':
                self.reka_gracza.append(self.talia.pop())
                print(f"Twoje karty: {self.reka_gracza} (Suma: {self.suma_reki(self.reka_gracza)})")
                suma_gracza = self.suma_reki(self.reka_gracza)
                if suma_gracza >= 21:
                    break
            elif decyzja == '2':
                break

        if self.suma_reki(self.reka_gracza) <= 21:
            while self.suma_reki(self.reka_krupiera) < 17:
                self.reka_krupiera.append(self.talia.pop())

        print(f"Twoje karty: {self.reka_gracza} (Suma: {self.suma_reki(self.reka_gracza)})")
        print(f"Karty krupiera: {self.reka_krupiera} (Suma: {self.suma_reki(self.reka_krupiera)})")
        print(self.sprawdz_wygrana(t))
