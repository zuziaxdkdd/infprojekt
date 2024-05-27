from random import randint

class Instagram:
    def __init__(self, fame, hate, liczbafollow, achievments):
        self.fame = fame
        self.hate = hate
        self.follows = liczbafollow
        self.wpisy = []
        self.achievments = achievments

    def Wyswietlopcje(self):

        xyz = ''

        while xyz == '':
            print("---" * 10)
            print("0 - Stwórz własny wpis")
            print("1 - Wyświetl swoje wpisy")
            print("2 - Wyjście")
            x = input("Wybierz opcje - ")
            if x == "0":
                print("---" * 10)
                self.WpisywanieWlasnegoWpisu()
                self.fame += 5
                self.follows += randint(1, 10)
                print(f"Masz aktualnie: {self.follows} follow!")

                if len(self.wpisy) <= 1:
                    self.achievments.append(" ! - Upublikowałxś swój pierwszy własny wpis!")
                    print("---"*10)
                    print("!!!!!!!!!!!!!!!! Otrzymałxś osiągnięcie !!!!!!!!!!!!!!!!")

            elif x == '1':
                print("Twoje wpisy: ")
                self.wyswietlwpisy()
                print(f"Masz aktualnie: {self.follows} follow!!")

            elif x == '2':
                break

    def WpisywanieWlasnegoWpisu(self):
        print("Napisz jaki chciałbyś dodać wpis:")
        wpis = input("")
        self.wpisy.append(wpis)
        
        if wpis == "200follow":
            self.follows += 200

    def wyswietlwpisy(self):
        print("---"*10)
        for el in self.wpisy:
            print(el)