from KreatorPostaci import TworzeniePlci

class Zaimki:

    def __init__(self):
        self.zaimek = ""
        self.zaimekjemujej = ''

    def ustaw_zaimek(self, plec_obj):
        if plec_obj.wybranaplec == 0 or plec_obj.wybranaplec == 2:
            self.zaimek = ""
            self.zaimekjemujej = 'mu'
        elif plec_obj.wybranaplec == 1 or plec_obj.wybranaplec == 3:
            self.zaimek = "a"
            self.zaimekjemujej = 'jej'