ekwipunek = []

class Uczucia:
    def __init__(self, milosc, szczescie, smutek, gniew):
        self.milosc = milosc
        self.szczescie = szczescie
        self.smutek = smutek
        self.gniew = gniew


class PoziomTrudnosci:
    def __init__(self, u):
        self.u = u
        self.listapoziomow = [
            "Wybierz poziom trudności:",
            "0 - easy mode",
            "1 - normal mode",
            "2 - hard mode"
        ]

    def EasyMode(self):
        self.u.smutek = 0
        self.u.szczescie = 80
        self.u.milosc = 30
        self.u.gniew = 0
        self.u.money = 100

    def NormalMode(self):
        self.u.smutek = 20
        self.u.szczescie = 60
        self.u.milosc = 10
        self.u.gniew = 0
        self.u.money = 50

    def HardMode(self):
        self.u.smutek = 50
        self.u.szczescie = 30
        self.u.milosc = 0
        self.u.gniew = 30
        self.u.money = 0


class Teksty:
    def __init__(self) -> None:
        self.smutek = 0
        self.szczescie = 0
        self.milosc = 0
        self.gniew = 0
        self.money = 0
        pass

    def inf(self):
        print(f"Milosc: {self.milosc}")
        print(f"Szczescie: {self.szczescie}")
        print(f"Smutek: {self.smutek}")
        print(f"Gniew: {self.gniew}")
        print(f"Pieniądze: {self.money}$")

t = Teksty()
milosc = t.milosc
szczescie = t.szczescie
smutek = t.smutek
gniew = t.gniew
money = t.money


class Eq:
    def eqw(self, t, ekwipunek):
        print("Czy chcesz użyć któryś z przedmiotów?")
        print(" 1 - tak")
        print(" 2 - nie")
        x = input("Numer - ")

        if x == '1':
            print("Który chcesz użyć?")
            for i, el in enumerate(ekwipunek):
                print(f"{i+1} - {el}")

            wybranyprzedmiotindex = int(input("Który chcesz użyć? ")) - 1
            
            if wybranyprzedmiotindex < 0 or wybranyprzedmiotindex >= len(ekwipunek):
                print("Niepoprawny numer przedmiotu.")
                return

            wybranyprzedmiot = ekwipunek[wybranyprzedmiotindex]
            
            if "Lemoniada cytrynowa" in wybranyprzedmiot:
                t.milosc += 15
                t.szczescie += 35
                ekwipunek.remove(wybranyprzedmiot)
                print("Użyłxś Lemoniady cytrynowej!")
                print("---"*10)

            elif "Lemoniada arbuzowa" in wybranyprzedmiot:
                t.milosc += 15
                t.szczescie += 45
                ekwipunek.remove(wybranyprzedmiot)
                print("Użyłxś Lemoniady arbuzowej!")
                print("---"*10)

            elif "Woda z cytryną" in wybranyprzedmiot:
                t.milosc += 10
                t.szczescie += 25
                ekwipunek.remove(wybranyprzedmiot)
                print("Użyłxś Wody z cytryną!")
                print("---"*10)

            elif "Kinderki" in wybranyprzedmiot:
                t.szczescie += 25
                t.smutek -= 25
                ekwipunek.remove(wybranyprzedmiot)
                print("Użyłxś Kinderków!")
                print("---"*10)

            elif "Czekolada Milka" in wybranyprzedmiot:
                t.szczescie += 25
                t.milosc += 5
                ekwipunek.remove(wybranyprzedmiot)
                print("Użyłxś Czekolady!")
                print("---"*10)

            elif "Zelki" in wybranyprzedmiot:
                t.smutek -= 20
                ekwipunek.remove(wybranyprzedmiot)
                print("Użyłxś Zelek!")
                print("---"*10)

            elif "Kwasne zelki" in wybranyprzedmiot:
                t.gniew -= 20
                ekwipunek.remove(wybranyprzedmiot)
                print("Użyłxś Kwasnych zelek!")
                print("---"*10)