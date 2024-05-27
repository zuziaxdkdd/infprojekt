from Poboczne import Teksty, ekwipunek

class Pieniadze:
    def __init__(self):
        money = self.money

t = Teksty()
milosc = t.milosc
szczescie = t.szczescie
smutek = t.smutek
gniew = t.gniew
money = t.money

listarzeczykupczych = [
    "1 - Słodycze",
    "2 - ",
    "3 - ",
]

slodyczelista = [
    ' 1 - kinderki - 35$ | szczęście + 25, smutek - 25',
    ' 2 - milka czekolada - 40$ | szczęście + 25, miłość + 5',
    ' 3 - zelki - 20$ | smutek - 20',
    ' 4 - kwasne zelki - 25$ | gniew - 20'
]


class Sklep:
    def listarzeczy(self, t):
        for el in listarzeczykupczych:
            print(el)
        p = Przedmioty()
        p.Pytanie(t)


class Przedmioty:
    def Pytanie(self, t):
        xy = input("Numer - ")

        abc = ''

        while abc == '':

            if xy == '1':
                for el in slodyczelista:
                    print(el)
                
                print("Aby cofnąc napisz '123' ")
                ktore = input("Numer zakupu - ")

                if ktore == '123':
                    break

                elif ktore == '1':
                    if t.money >= 35:
                        ekwipunek.append(" <3 - Kinderki | szczęście + 25, smutek - 25")
                        t.money -= 35
                        print("---"*10)
                        print(f"Kupiłxś kinderki, masz teraz {t.money}")
                    elif t.money <= 35:
                        print("Nie masz wystarczająco dużo pieniędzy!! ;(")
                        print("---"*10)
                        
                elif ktore == '2':
                    if t.money >= 40:
                        ekwipunek.append(" <3 - Czekolada Milka | szczęście + 25, miłość + 5")
                        t.money -= 40
                        print("---"*10)
                        print(f"Kupiłxś czekolade Milke, masz teraz {t.money}")
                    elif t.money <= 40:
                        print("Nie masz wystarczająco dużo pieniędzy!! ;(")
                        print("---"*10)
                        
                elif ktore == '3':
                    if t.money >= 20:
                        ekwipunek.append(" <3 - Zelki | smutek - 20")
                        t.money -= 20
                        print("---"*10)
                        print(f"Kupiłxś zelki, masz teraz {t.money}")
                    elif t.money <= 20:
                        print("Nie masz wystarczająco dużo pieniędzy!! ;(")
                        print("---"*10)
                        
                elif ktore == '4':
                    if t.money >= 25:
                        ekwipunek.append(" <3 - Kwasne zelki | gniew - 20")
                        t.money -= 25
                        print("---"*10)
                        print(f"Kupiłxś kinderki, masz teraz {t.money}")
                    elif t.money <= 25:
                        print("Nie masz wystarczająco dużo pieniędzy!! ;(")
                        print("---"*10)

                if xy == '123':
                    break
