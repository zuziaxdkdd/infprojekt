from zaimek import Zaimki
from KreatorPostaci import TworzeniePlci, TworzeniePostaci, TworzenieWlosow, TworzenieWzrostu, TworzenieImienia
from Poboczne import Teksty, Eq, ekwipunek
from instagram import Instagram
from random import randint
from Osiagniecia import achievments
from sklep import Sklep
import time


class Przyjaciel:
    def __init__(self, imie, plec, zawod):
        self.imie = imie
        self.plec = plec
        self.zawod = zawod

    def przedstawsie(self):
        return f"Imie - {self.imie}, plec - {self.plec}, zawod - {self.zawod}"
    
    @staticmethod
    def wyswietlliste(p1, p2):
        return print(f" 1 - {p1.przedstawsie()} \n 2 - {p2.przedstawsie()} ")
    
    @staticmethod
    def wyswietlp1(p1):
        return print(f"{p1.przedstawsie()}")
    
    @staticmethod
    def wyswietlp2(p2):
        return print(f"{p2.przedstawsie()}")


class Przyjacielnumer1(Przyjaciel):
    def __init__(self, imie, plec, zawod):
        super().__init__(imie, plec, zawod)

    def przedstawsie(self):
        return super().przedstawsie()


class Przyjacielnumer2(Przyjaciel):
    def __init__(self, imie, plec, zawod):
        super().__init__(imie, plec, zawod)

    def przedstawsie(self):
        return super().przedstawsie() 

p = Przyjaciel
x = ''
p1 = Przyjacielnumer1(f"{x}", "Mężczyzna", "Pracownik energylandii")
p2 = Przyjacielnumer2(f"{x}", "Kobieta", "Pracownik elektrowni") 

y = ''

class SpotkaniePrzyjaciol:
    def __init__(self):
        self.licznikimienia = 0

    def tworzenieprzyjaciela(self):
        print("Wybierz przyjaciela twojej randki: ")
        Przyjaciel.wyswietlliste(p1, p2)
        global y
        y = input("Którego wybierasz? - ")
        if y == "1":
            x = input("Imie dla przyjaciela - ")
            p1.imie = x
            Przyjaciel.wyswietlp1(p1)
            self.licznikimienia += 2
        if y == "2":
            x = input("Imie dla przyjaciela - ")
            p2.imie = x
            Przyjaciel.wyswietlp2(p2)
            self.licznikimienia += 2

t = Teksty()
eq = Eq()
milosc = t.milosc
szczescie = t.szczescie
smutek = t.smutek
gniew = t.gniew
money = t.money

# --------------------------PIERWSZA CZESC FABULY--------------------------

class Tekscior:
    def __init__(self, zaimek, zaimekjemujej, instagram):
        self.zaimek = zaimek
        self.zaimekjemujej = zaimekjemujej
        self.instagram = instagram


    def spotkanie1(self, t):
        print("---"*10)
        print("Poznaliście się na tinderze, przyszedł czas na pierwsze spotkanie. Poszliście do parku.")
        print(f"Stał{self.zaimek.zaimek} przy wejsciu. Wyglądał{self.zaimek.zaimek} jakby było {self.zaimekjemujej.zaimekjemujej} zimno.")
        print(f"Musisz coś z tym zrobić")
        print(f" 1 - Pożyczasz {self.zaimekjemujej.zaimekjemujej} bluze")
        print(f" 2 - Stwierdzasz, że zaraz wyjdzie słońce i nic więcej nie robisz w tej sytuacji")

        opcja1 = input("Co robisz? - ")
        
        if opcja1 == "1":
            t.milosc += 5; t.szczescie += 15; t.smutek -= 10; t.gniew -= 10; t.money += 10

        elif opcja1 == '2':
            t.milosc -= 10; t.szczescie -= 15; t.smutek += 10; t.gniew += 5

        t.inf()

        print("---"*10)
        print("Idziecie sobie razem parkiem i rozmowa przebiega w maire sprawnie. \n Nagle spotykasz starego znajomego, wypada sie przywitać.")
        print(" 1 - Omijasz znajomego i idziecie dalej razem")
        print(" 2 - Witacie się ale idziecie dalej ponieważ nie chcesz zostawić swojej randki")
        print(" 3 - Zaczynasz z nim rozmawiać")

        opcja2 = input("Co robisz? - ")

        if opcja2 == "1":
            t.milosc += 5; t.szczescie += 30; t.smutek -= 10; t.gniew -= 10; t.money += 10
            xyy = ''

        elif opcja2 == '2':
            t.milosc += 10; t.szczescie += 25; t.smutek -= 5; t.money += 5
            xyy = 'Przywitaliście się i poszliście dalej.'
        
        elif opcja2 == '3':
            print(f"Chyba zapomniałxś o swojej randce, zrobiło się {self.zaimekjemujej.zaimekjemujej} smutno...")
            t.milosc -= 20; t.szczescie -= 35; t.smutek += 20; t.gniew += 30
            xyy = 'Cieszysz się, że mogłxś pogadać z dawnym kolegą ale twoja randka nie wygląda na zadowoloną.'

        t.inf()

        print("---"*10)
        print(f"{xyy} Zobaczyłxś budke z lemoniadą. Zachciało {self.zaimekjemujej.zaimekjemujej} pić.")
        print(" 1 - Podchodzisz po lemionade")
        print(" 2 - Ignorujesz i idziesz dalej")

        opcja3 = input("Co robisz? - ")

        if opcja3 == '2':
            t.milosc -= 20; t.szczescie -= 25; t.smutek += 20; t.gniew += 15

        elif opcja3 == '1':
            print("---"*10)
            print(f"Możesz kupić jedną z lemoniad, masz aktualnie {t.money}$. Wybierz którąś z poniższych:")
            print(" 1 - Lemoniada cytrynowa - 15$ | +15 miłości, +35 szczęścia")
            print(" 2 - Lemoniada arbuzowa - 20$ | +15 miłości, +45 szczęścia")
            print(" 3 - Woda z cytryną - 12$ | +10 miłości, +25 szczęścia")
            print(" 4 - Wyjdź ze sklepu")

            opcja4 = input("Co robisz? - ")

            if opcja4 == '1':
                if t.money >= 15:
                    ekwipunek.append(" <3 - Lemoniada cytrynowa")
                    t.money -= 15
                    print("---"*10)
                    print("Kupiłxś lemoniade cytrynową, czy chcesz otworzyć teraz ekwipunek?")
                    print(" 1 - tak")
                    print(" 2 - nie")

                    opcja5 = input("Co robisz? - ")

                    if opcja5 == '1':
                        print("Twój ekwipunek: ")
                        for el in ekwipunek:
                            print(el)
                        eq.eqw(t, ekwipunek)
                elif t.money <= 15:
                    print("Nie masz wystarczająco dużo pieniędzy!! ;(")

            elif opcja4 == '2':
                if t.money >= 20:
                    ekwipunek.append(" <3 - Lemoniada arbuzowa")
                    t.money -= 20
                    print("---"*10)
                    print("Kupiłxś lemoniade arbuzową, czy chcesz otworzyć teraz ekwipunek?")
                    print(" 1 - tak")
                    print(" 2 - nie")

                    opcja5 = input("Co robisz? - ")

                    if opcja5 == '1':
                        print("Twój ekwipunek: ")
                        for el in ekwipunek:
                            print(el)
                        eq.eqw(t, ekwipunek)
                elif t.money <= 20:
                    print("Nie masz wystarczająco dużo pieniędzy!! ;(")

            elif opcja4 == '3':
                if t.money >= 12:
                    ekwipunek.append(" <3 - Woda z cytryną")
                    t.money -= 12
                    print("---"*10)
                    print("Kupiłxś wodę z cytryną, czy chcesz otworzyć teraz ekwipunek?")
                    print(" 1 - tak")
                    print(" 2 - nie")

                    opcja5 = input("Co robisz? - ")

                    if opcja5 == '1':
                        print("Twój ekwipunek: ")
                        for el in ekwipunek:
                            print(el)
                        eq.eqw(t, ekwipunek)
                elif t.money <= 12:
                    print("Nie masz wystarczająco dużo pieniędzy!! ;(")

            elif opcja4 == '4':
                print("---"*10)
                print("Troche nie fajnie robić nadzieje...")
                t.milosc -= 20; t.szczescie -= 25; t.smutek += 20; t.gniew += 15

            print("---"*10)
            t.inf()
            
        print("---"*10)
        print("Wasza pierwsza randka dobiega końca. Jest już ciemno i pora wracać do domu, nie chcesz zostawić twojej randki samej.")
        print(" 1 - Odprowadzasz na przystanek")
        print(" 2 - Stwierdzasz, że da rade, bo to jest nawet blisko")

        opcja6 = input("Co robisz? - ")

        if opcja6 == '1':
            print(f"Zrobiłxś {self.zaimekjemujej.zaimekjemujej} lepszy humor, ale mówi, że dał{self.zaimek.zaimek}by rade sam{self.zaimek.zaimek}!")
            t.milosc += 5; t.szczescie += 15; t.smutek -= 10; t.gniew -= 10; t.money += 10

        elif opcja6 == '2':
            t.szczescie -= 5

        t.inf()


        print("---"*10)
        print("Jest to koniec waszej pierwszej randki!! Czy chcesz podzielić się tym na Instagramie?")
        print(" 1 - tak - wstaw post")
        print(" 2 - nie")

        instagrampost1 = input("Wstawiasz post? - ")

        if instagrampost1 == '1':
            self.instagram.wpisy.append("Pierwszy meeting, było super xoxo")
            self.instagram.follows += randint(20,30)
            print("Dodano nowy wpis!!")

        achievments.append(" ! - Ukończyłxś pierwszą część fabuły!!! ")
        print("---"*10)
        print("!!!!!!!!!!!!!!!! Otrzymałxś osiągnięcie !!!!!!!!!!!!!!!!")


    def spotkanie2(self, t):
            print("---"*10)
            print("Druga część fabuły")

            print("Decydujesz się na kolejne spotkanie ze swoją randką. Tym razem umawiacie się do Energylandii.")

            print(f"Podczas spaceru, nagle pojawia się XXX , przyjcaiel twojej randki. Wydaje się on{self.zaimek.zaimek} zaskoczon{self.zaimek.zaimek} waszym spotkaniem.")
            print(" 1 - Przedstawiasz się i witasz z nim.")
            print(" 2 - Podchodzicie do niego ale czekasz aż twoja randka ciebei przedstawi.")

            opcja1 = input("Co robisz? - ")

            if opcja1 == '1':
                t.milosc += 5; t.szczescie += 10; t.money += 5

            elif opcja1 == '2':
                t.milosc -=5; t.szczescie -=5; t.smutek += 5; t.gniew += 5

            t.inf()
            print("---"*10)

            print("Poszliście na Zadre, co teraz?")
            print(" 1 - Idziecie na kolejkę razem z przyjacielem randki.")
            print(" 2 - Namawiasz swoją randke aby pójść na coś innego aby mieć więcej czasu dla siebie.")

            opcja2 = input("Co robisz? - ")

            if opcja2 == '1':
                print("Świetnie się razem bawicie a nowy znajomy nie okazuje się być taki zły")
                t.milosc += 5; t.szczescie += 25; t.smutek -= 10; t.money += 10

            elif opcja2 == '2':
                print("Twoja randka jest troche zła za to i stwierdza, że powinniście nawzajem się zapoznać lepiej.")
                t.milosc -= 15; t.szczescie -= 10; t.smutek += 15; t.gniew += 20

            print("---"*10)
            t.inf()

            print("Wieczorem decydujecie się na wspólną kolację w restauracji.")
            print("Podczas kolacji rozmawiacie o różnych tematach, a atmosfera jest bardzo przyjemna.")

            print("Kiedy przychodzi czas na rozstanie się, przyjaciel randki zaprasza was na kolejne spotkanie razem.")
            print(" 1 - Zgadasz się i planujecie kolejne spotkanie we troje.")
            print(" 2 - Dziękujesz za zaproszenie, ale chcesz spędzić czas tylko we dwoje.")

            opcja3 = input("Co robisz? - ")

            if opcja3 == '1':
                print("Decydujecie się na kolejne spotkanie we troje, co sprawia przyjemność zarówno tobie, jak i twojej randce.")
                t.milosc += 5; t.szczescie += 15; t.money += 5

            elif opcja3 == '2':
                print("Twoja randka docenia twoją decyzję, chociaż przyjaciel może być nieco zawiedziony.")
                t.milosc -= 5; t.szczescie -= 5; t.smutek += 5; t.gniew += 5

            t.inf()
            print("---"*10)

            print("Kolejna udana randka!! Czy chcesz wstawić posta na instagrama?")
            print(" 1 - tak - wstaw post")
            print(" 2 - nie")

            instagrampost2 = input("Wstawiasz post? - ")

            if instagrampost2 == '1':
                self.instagram.wpisy.append("Energylandia!!!! o tak!!!!!!! #zajebiscie #skibidi")
                self.instagram.follows += randint(20,30)
                print("Dodano nowy wpis!!")

            t.inf()

            achievments.append(" ! - Ukończyłeś drugą część fabuły! ")
            print("---"*10)
            print("!!!!!!!!!!!!!!!! Otrzymałxś osiągnięcie !!!!!!!!!!!!!!!!")


    def spotkanie3(self, t):
            print("---"*10)
            print("Druga część fabuły")

            print("Poszliście do galerii handlowej. ")


    def spotkanie4(self, t):
        print("Trzecie spotkanie")
        print(f"Umówiliście się wieczorem na trzecie spotkanie. Mieliście się spotkać pod sklepem. Zanim to zdecydowałxś się coś {self.zaimekjemujej.zaimekjemujej} kupić")

        print("Czy chcesz coś teraz kupić? ")
        print(" 1 - tak \n 2 - nie")

        x = input("Numer - ")

        if x == '1':
            s.listarzeczy(t)
        elif x == '2':
            t.szczescie -= 5

        print("---"*10)

        print("Twój ekwipunek:")
        for el in ekwipunek:
            print(el)
        eq.eqw(t, ekwipunek)

        print("---"*10)
        print(f"Po dluższym czasie twoja randka nie pojawiał{self.zaimek.zaimek} się.")
        print(f"Zacząłxś się martwić i zastanawiać co się stało. Nagle dostałxś SMS na telefonie. Okazało się, że został{self.zaimek.zaimek} porwan{self.zaimek.zaimek}")
        print(f"- Musisz teraz zebrać 200$!! Aktualnie masz {t.money}$!!")

        print("---"*10)
        print(" Czy chcesz teraz zapłacić?")
        print(" 1 - tak \n 2 - nie")

        xy = input("Numer -")

        if xy == '1':
            if t.money >= 200:
                t.money -= 200
                tx.spotkaniemafia(t)
            elif t.money < 200:
                print("Nie masz wystarczającej ilości pieniędzy!")
        elif xy == '2':
            print("Zbierz wystarczającą ilość!")


    def mafiaczykasa(self, t):

        print("---"*10)
        print(f" Czy chcesz teraz zapłacić? Masz teraz {t.money}$")
        print(" 1 - tak \n 2 - nie")

        yx = input("Numer -")

        if yx == '1':
            if t.money >= 200:
                t.money -= 200
                tx.spotkaniemafia(t)
            elif t.money < 200:
                print("Nie masz wystarczającej ilości pieniędzy!")
        elif yx == '2':
            print("Zbierz wystarczającą ilość!")

    def spotkaniemafia(self, t):
        t.milosc += 20
        print(f"Zapłaciłxś, ale okazało się, że był to tylko scam! Na szczęście w tym czasie udało się policji znaleźć, kto mógł {self.zaimekjemujej.zaimekjemujej} to zrobić")
        print(f"---------")
        print("CHWILOWY KONIEC")
        return True


    def JULKAZUGAJ(self, ig) :
        print(f"Zdobyłxś już ponad 200 follow na Instagramie!! Zaczepiła cię jedna z żugajek:")
        print("")
        time.sleep(1.0)
        print(f" xskibidizugajka_julci<3: Ej dlacego chejtujes julcie i żugajki pod moim reelsem?")
        
        x = input(" 1 - 'O co ci chodzi?' \n 2 - 'Co ty gadasz xdd'")
        if x == '1':
            odp = " Ty : O co ci chodzi?"
        elif x == '2':
            odp = "Co ty gadasz xdd"

        print(f"Ty: {odp}")
        time.sleep(2.5)
        print(f" xskibidizugajka_julci<3: No przeciesz widziałam nie udawaj teras!!!!!!!!!")
        time.sleep(1.5)
        print(f" xskibidizugajka_julci<3: POrzałójesz tego zobaczysz.....")
        time.sleep(2.0)
        print("")
        print(" Co teraz zrobisz?")
        print(" 1 - Zignorujesz to i zamierzasz żyć jak wcześniej \n 2 - Zaczynasz hejtować ją i piszesz hejty pod reelsami")

        corobisz = input("Numer - ")

        if corobisz == '1':
            ig.follows -= 200
        elif corobisz == '2':
            tx.JULKAZUGAJ2(ig)


    def JULKAZUGAJ2(self, ig):
        print("---"*10)
        print("Minęły 2h od czasu groźby żugajki. Dostajesz znów wiadomość od niej.")
        time.sleep(2.0)
        print(" xskibidizugajka_julci<3: Muwiłąm ze porzalujesz wszystkieko....")
        time.sleep(1.5)
        print(" xskibidizugajka_julci<3: 10....")
        time.sleep(1.0)
        print(" xskibidizugajka_julci<3: 9....")
        time.sleep(1.0)
        print(" xskibidizugajka_julci<3: 8....")
        time.sleep(1.0)
        print(" xskibidizugajka_julci<3: 7....")
        time.sleep(1.0)
        print(" xskibidizugajka_julci<3: 6....")
        time.sleep(1.0)
        print(" xskibidizugajka_julci<3: 5....")
        time.sleep(1.0)
        print(" xskibidizugajka_julci<3: 4....")
        time.sleep(1.0)
        print(" xskibidizugajka_julci<3: 3....")
        time.sleep(1.0)
        print("Nagle ktoś puka do drzwi. Zanim otworzysz spoglądasz przez wizjer.")
        print("Zauważasz gigantyczna armie żugajek z hobby horsami, śpiewające ich hymn. Pukanie do drzwi jest coraz głośniejsze.")
        print("Zaczynasz się bać o siebie więc postanawiasz uciec tylnim wyjściem. Wybierz gdzie uciekniesz: ")
        print(" 1 - do sklepu \n 2 - do znajomego \n 3 - za granice")

        gdzie = input("Gdzie uciekasz? - ")

        if gdzie == '1' or '2' or '3':
            print("Tak naprawdę to nie ma znaczenia gdzie pobiegniesz, i tak żugajki okazały się być silniejsze.")
        
        print("---"*10)
        print("Zostałxś związany i porwany do piwnicy. Nie możesz uwierzyć, że pokonały cię dziewcznyki jeżdżące na patykach. Musisz się uwolnić, co robisz?")
        print(" 1 - Zaczynasz drzeć się z nadzieją, że ktoś cię usłyszy \n 2 - Błagasz o przebaczenie \n 3 - Zaczynasz płakać")

        input("Co robisz? - ")

        print("---"*10)
        print("Nagle przychodzi zastępca przywódcy Julki. Mówi, że zostaniesz wypuszczonx jeśli pojedziesz na obóz żugajkowy. Obiecałxś pojechanie więc zostałxś wypuszczonx.")
        print("Tak naprawdę zrobiłxś to dla podstępu i oszukałxś je.")

        print("---"*10)
        print("Minęły trzy lata a twoja wojna z żugajkami trwała dalej. Nastał dzień zakończenia tego sporu. Czas wstawić story na Instagramie:")
        print(" 1 - 'Julka i wszytskie żugajki, pora na wasz koniec' \n 2 - 'Julka Żugaj śmuerdzi' \n 3 - 'Jxbxć żugajki'")

        ktore = input("Numer - ")

        if ktore == '1':
            numerek = 'Julka i wszytskie żugajki, pora na wasz koniec'
        elif ktore == '2':
            numerek = 'Julka Żugaj śmuerdzi'
        elif ktore == '3':
            numerek = 'Jxbxć żugajki'

        print(f"Wstawiasz story: {numerek}")
        print("Po 5 minutach usłyszałxś zbliżającą się armie żugajek")

        print("---"*10)

        print("nananannaanananan duzo skipnietej walki")

        print("Przykładasz nóż pod gardło Julki. Wybierz, czy poderżniesz jej gardło. Ta decyzja będzie miała wpływ na twoją przyszłość!!!")
        print(" 1 - Zabijasz Julke \n 2 - Oszczędasz ją")

        julkazycie = input("Numer - ")

        if julkazycie == '1':
            print("---"*10)
            print("Wszystkie żugajki się na ciebie rzuciły i zostałxś zabity bez litości")
            print(" ---------------- PRZEGRAŁXŚ ---------------- ")
            print(" - secret bad ending - ")
        
        elif julkazycie == '2':
            print("---"*10)
            print("Oszczędziłxś Julke, żugajki doceniły to i zaproponowały sojusz i koniec wojny. Zgodziłxś się.")
            print(" ---------------- WYGRAŁXŚ ---------------- ")
            print(" - secret good ending -")



s = Sklep()
ZZaimek = Zaimki()
ig = Instagram(fame=0, hate=0, liczbafollow=0, achievments=achievments)

tx = Tekscior(ZZaimek, ZZaimek, ig)

class Wyboryjakies:
    def spotkaniekolejne(t):
        if y == '1':
            tx.spotkanie2(t)
        elif y == '2':
            tx.spotkanie3(t)
