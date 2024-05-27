class TworzeniePlci:
    wyborplci = [
        '0 - mezczyzna',
        '1 - kobieta',
        '2 - furry mezczyzna',
        '3 - furry kobieta'
    ]
    
    def __init__(self) -> None:
        print("Wybierz plec:")

        for el in self.wyborplci:
            print(el)

        self.wybranaplec = int(input("Numer: "))
        if self.wybranaplec == 0:
            self.plec = 'mezczyzna'
            print(f"Wybrałxś: {self.plec}!")
        elif self.wybranaplec == 1:
            self.plec = 'kobieta'
            print(f"Wybrałxś: {self.plec}!")
        elif self.wybranaplec == 2:
            self.plec = 'furry mezczyzna'
            print(f"Wybrałxś: {self.plec}!")
        elif self.wybranaplec == 3:
            self.plec = 'furry kobieta'
            print(f"Wybrałxś: {self.plec}!")

        print("---" * 10)


class TworzenieWlosow:
    wlosydowyboru = [
        '0 - bez wlosow',
        '1 - krotkie wlosy',
        '2 - srednie wlosy',
        '3 - dlugie wlosy'
    ]

    kolorwlosowdowyboru = [
        '0 - blond',
        '1 - braozwy',
        '2 - czarny',
        '3 - rudy',
        '4 - kolor jakis (do wyboru)'
    ]

    def __init__(self) -> None:
            print("Wybierz wlosy:")

            for el in self.wlosydowyboru:
                print(el)

            wyborwlosow = int(input("Numer: "))
            if wyborwlosow == 0:
                self.wlosy = 'bez wlosow'
                print(f"Wybrałxś: {self.wlosy}!")
            elif wyborwlosow == 1:
                self.wlosy = 'krotkie'
            elif wyborwlosow == 2:
                self.wlosy = 'srednie'
            elif wyborwlosow == 3:
                self.wlosy = 'dlugie'

            print("---"*10)

            if wyborwlosow != 0 and wyborwlosow <= 3:
                print("Wybierz kolor włosów:")
                    
                for el in self.kolorwlosowdowyboru:
                    print(el)
                    
                kolorwlosow = int(input("Numer: "))
                if kolorwlosow == 0:
                    self.wlosy += ' i blond'
                elif kolorwlosow == 1:
                    self.wlosy += ' i brazowe'
                elif kolorwlosow == 2:
                    self.wlosy += ' i czarne'
                elif kolorwlosow == 3:
                    self.wlosy += ' i rude'
                elif kolorwlosow == 4:
                    x = input("Wpisz jakie wlosy? (kolor dowolny) ")
                    self.wlosy += (f" i {x}")

                print(f"Wybrałxś: {self.wlosy}!")
                print("---"*10)
                pass


class TworzenieWzrostu:
    
    wzrostdowybory = [
        '0 - 160 cm',
        '1 - 170 cm',
        '2 - 180 cm',
        '3 - 190 cm',
        '4 - dowolny wzrost'
    ]
    def __init__(self) -> None:
        print("Wybierz wzrost:")

        for el in self.wzrostdowybory:
            print(el)

        wyborwzrostu = int(input("Numer: "))
        if wyborwzrostu == 0:
            self.wzrost = 'ok. 160'
        elif wyborwzrostu == 1:
            self.wzrost = 'ok. 170'
        elif wyborwzrostu == 2:
            self.wzrost = 'ok. 180'
        elif wyborwzrostu == 3:
            self.wzrost = 'ok. 190'
        elif wyborwzrostu == 4:
            self.wzrost = input("Napisz dowolny wzrost: ")

        print(f"Wybrałxś wzrost: {self.wzrost} cm!")
        print("---"*10)
        pass


class WybierzKolorOczu:
    oczykolor = [
        '0 - brazowy',
        '1 - zielony',
        '2 - niebieski',
        '3 - soczewki (do wyboru)'
    ]
    def __init__(self) -> None:
        print("Wybierz oczy:")

        for el in self.oczykolor:
            print(el)

        wybraneoczy = int(input("Numer: "))
        if wybraneoczy == 0:
            self.oczy = 'brazowy'
        elif wybraneoczy == 1:
            self.oczy = 'zielony'
        elif wybraneoczy == 2:
            self.oczy = 'niebieski'
        elif wybraneoczy == 3:
            self.oczy = input("Podaj dowolny kolor oczu: ")

        print("---"*10)
        pass

class TworzenieImienia:
    def __init__(self) -> None:
        self.imiepostaci = input("Wybierz imie postaci = ")
        imieukochanego = self.imiepostaci
        print(imieukochanego)
        print(f"Wybrałxś imię: {self.imiepostaci}!")
        print("---"*10)
        pass


class TworzeniePostaci:

    def __init__(self, plec:TworzeniePlci, wlosy:TworzenieWlosow, wzrost:TworzenieWzrostu, oczy:WybierzKolorOczu, imie:TworzenieImienia) -> None:
        self.plec = plec
        self.wlosy = wlosy
        self.wzrost = wzrost
        self.oczy = oczy
        self.imie = imie

        
    def inf(self):
        print(f'Imię: {self.imie.imiepostaci}')
        print(f'Płeć: {self.plec.plec}')
        print(f'Oczy: {self.oczy.oczy}')
        print(f'Włosy: {self.wlosy.wlosy}')
        print(f'Wzrost: {self.wzrost.wzrost} cm!')