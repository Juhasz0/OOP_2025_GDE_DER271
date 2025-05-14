from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.dij = dij

    @abstractmethod
    def leiras(self):
        pass

class Szemelyauto(Auto):
    def leiras(self):
        return f"Személyautó - {self.tipus} (Rendszám: {self.rendszam}, Napi díj: {self.dij} Ft)"

class Teherauto(Auto):
    def leiras(self):
        return f"Teherautó - {self.tipus} (Rendszám: {self.rendszam}, Napi díj: {self.dij} Ft)"


# === berles.py ===
class Berles:
    def __init__(self, auto, mettol, meddig):
        self.auto = auto
        self.mettol = mettol
        self.meddig = meddig

    def osszeg(self):
        napok = (self.meddig - self.mettol).days + 1
        return napok * self.auto.dij

    def __str__(self):
        return (f"Autó: {self.auto.tipus}, Rendszám: {self.auto.rendszam}, "
                f"Bérlés: {self.mettol.date()} - {self.meddig.date()}, "
                f"Napi díj: {self.auto.dij} Ft, Összesen: {self.osszeg()} Ft")