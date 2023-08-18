#çokgen alan hesabı
import math
class Cokgen:
    def __init__(self, kenar_sayisi):
        self.kenar_sayisi = kenar_sayisi

    def kenar_uzunluklari_al(self):
        self.kenar_uzunluklari = []
        for i in range(self.kenar_sayisi):
            uzunluk = float(input(f"{i+1}. kenarın uzunluğunu girin: "))
            self.kenar_uzunluklari.append(uzunluk)

    def cevre(self):
        return sum(self.kenar_uzunluklari)

class Ucgen(Cokgen):
    def __init__(self):
        super().__init__(3)

    def alan(self):
        a, b, c = self.kenar_uzunluklari
        yaricap = self.cevre() / 2
        return math.sqrt(yaricap * (yaricap - a) * (yaricap - b) * (yaricap - c))

class Dortgen(Cokgen):
    def __init__(self):
        super().__init__(4)

    def alan(self):
        return self.kenar_uzunluklari[0] * self.kenar_uzunluklari[1]

class Besgen(Cokgen):
    def __init__(self):
        super().__init__(5)

    def alan(self):
        a = self.kenar_uzunluklari[0]
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a**2

# Ana program
secim = int(input("Bir çokgen seçin:\n1. Üçgen\n2. Dörtgen\n3. Beşgen\nSeçiminizi girin: "))

if secim == 1:
    ucgen = Ucgen()
    ucgen.kenar_uzunluklari_al()
    print("Üçgen Alanı:", ucgen.alan())
elif secim == 2:
    dortgen = Dortgen()
    dortgen.kenar_uzunluklari_al()
    print("Dörtgen Alanı:", dortgen.alan())
elif secim == 3:
    besgen = Besgen()
    besgen.kenar_uzunluklari_al()
    print("Beşgen Alanı:", besgen.alan())
else:
    print("Geçersiz seçim")