from KreatorPostaci import TworzeniePostaci, TworzeniePlci, TworzenieWlosow, TworzenieWzrostu, WybierzKolorOczu, TworzenieImienia
from spotkaniaprzyjaciol import SpotkaniePrzyjaciol, Tekscior
from Poboczne import PoziomTrudnosci, Teksty, Eq, ekwipunek
from minigry import MiniGierki
from sklep import Sklep, Pieniadze
from Osiagniecia import Osiagniecia, achievments
from instagram import Instagram
from zaimek import Zaimki

# --------------------------TWORZENIE POSTACI--------------------------

yourname = input("Wybierz swoje imię: ")
print(f"Teraz nazywasz się {yourname} !!")
print("---" * 10)

print("Stwórz postać swojego ukochanego bądź ukochanej")

p = TworzeniePlci()
w = TworzenieWlosow()
wz = TworzenieWzrostu()
o = WybierzKolorOczu()
i = TworzenieImienia()
calapostac = TworzeniePostaci(p, w, wz, o, i)
calapostac.inf()

print("---" * 10)
achievments.append(" ! - Stworzyłxś postać! ")
print("!!!!!!!!!!!!!!!! Otrzymałxś osiągnięcie !!!!!!!!!!!!!!!!")

# --------------------------CLASSY ITP--------------------------

ZZaimek = Zaimki()
ZZaimek.ustaw_zaimek(p)

t = Teksty()
milosc = t.milosc
szczescie = t.szczescie
smutek = t.smutek
gniew = t.gniew
money = t.money

pt = PoziomTrudnosci(t)

ig = Instagram(fame=0, hate=0, liczbafollow=0, achievments=achievments)
osi = Osiagniecia(achievments=achievments)
tekst = Tekscior(ZZaimek, ZZaimek, ig)
sprz = SpotkaniePrzyjaciol()
mg = MiniGierki()
s = Sklep()
eq = Eq()

# --------------------------WYBIERANIE POZIOMU TRUDNOSCI--------------------------

for el in pt.listapoziomow:
    print("---" * 10)
    print(el)

trudnosc = input("Numer - ")

if trudnosc == '0':
    pt.EasyMode()
elif trudnosc == '1':
    pt.NormalMode()
elif trudnosc == '2':
    pt.HardMode()

print("---" * 10)
t.inf()


# --------------------------OGOLNE WYBORY--------------------------

def ogolnywyboropcji():
        print("---" * 10)
        print("Wybierz co chcesz teraz zrobić: ")
        print("0 - Typowa randka - konwersacje - COMMING SOON")
        print("1 - Spotkania - fabuła")
        print("2 - Wyświetl informacje o postaciach")
        print("3 - Zagraj w grę (po coiny)")
        print("4 - Sklep")
        print("5 - Zobacz osiągnięcia")
        print("6 - Instagram")
        print("7 - Ekwipunek")
        print("123 - Zakończ grę")

x = 0
game_over = False
powtorki = 0

tx = Tekscior(ZZaimek, ZZaimek, ig)

from spotkaniaprzyjaciol import Wyboryjakies
wj = Wyboryjakies

while x == 0:
    if t.milosc >= 100:
        print("---"*10)
        print(" ---------------- WYGRAŁXŚ ---------------- ")
        print("Finałowo polecieliście za granice, pobraliście się i zamieszkaliście razem!! \n !!!KONIEC GRY!!!")
        print(" - good ending -")
        break
    elif t.smutek >= 100 or t.milosc <= -1:
        print("---"*10)
        print(" ---------------- PRZEGRAŁXŚ ---------------- ")
        print(" - bad ending - ")
        break

    ogolnywyboropcji()
    wybor = input("Twój wybór - ")

    if wybor == "0":
        print("--- narazie nie dziala ---")

    if wybor == "1":
        if ig.follows >= 200:
            tx.JULKAZUGAJ(ig)
            if ig.follows >= 200:
                break
            else:
                continue

        if sprz.licznikimienia == 0:
            sprz.tworzenieprzyjaciela()
            print("---"*10)
            achievments.append(" ! - Stworzyłeś przyjaciela twojej randki! ")
            print("!!!!!!!!!!!!!!!! Otrzymałeś osiągnięcie !!!!!!!!!!!!!!!!")
        elif sprz.licznikimienia >= 1:
            if powtorki == 0:
                tx.spotkanie1(t)
                powtorki += 1
            elif powtorki == 1:
                wj.spotkaniekolejne(t)
                powtorki += 1
            elif powtorki == 2:
                tx.spotkanie4(t)
                powtorki += 1
            elif powtorki == 3:
                tx.mafiaczykasa(t)
                game_over = tx.spotkaniemafia(t) 
                if t.milosc >= 0:
                    print("---"*10)
                    print(" ---------------- WYGRAŁXŚ ---------------- ")
                    print(" cos tam")
                    print(" - common ending -")
                    break


    if wybor == "2":
        print("---" * 10)
        calapostac.inf()
        print("---" * 10)
        t.inf()
        print("---" * 10)

    if wybor == "3":
        mg.listagier(t)

    if wybor == "4":
        s.listarzeczy(t)

    if wybor == '5':
        osi.osiagnieciaogolnie()

    if wybor == '6':
        ig.Wyswietlopcje()

    if wybor == '7':
        print("Twój ekwipunek:")
        for el in ekwipunek:
            print(el)
        eq.eqw(t, ekwipunek)

    if wybor == "123":
        print("---" * 10)
        print("KONIEC GRY")
        print("---" * 10)
        t.inf()
        break