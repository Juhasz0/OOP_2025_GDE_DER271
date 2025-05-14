import os
from datetime import datetime
from auto import Szemelyauto, Teherauto
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []
        self.foglalas_file = "foglalasok.txt"
        self.betolt_alapadatok()

    def betolt_alapadatok(self):
        self.autok = [
            Szemelyauto("ABC-123", "Opel Astra", 12000),
            Szemelyauto("DEF-456", "Ford Focus", 11500),
            Szemelyauto("GHI-789", "Volkswagen Golf", 13000),
            Teherauto("TPR-123", "Volkswagen Transporter", 15000),
            Teherauto("TRN-456", "Ford Transit", 14400)
        ]
        if os.path.exists(self.foglalas_file):
            with open(self.foglalas_file, "r", encoding="utf-8") as f:
                for sor in f:
                    if sor.startswith("LEMONDVA") or not sor.strip():
                        continue
                    parts = sor.strip().split(", ")
                    rendszam = parts[1].split(": ")[1]
                    datumok = parts[2].split(": ")[1].split(" - ")
                    mettol = datetime.strptime(datumok[0], "%Y-%m-%d")
                    meddig = datetime.strptime(datumok[1], "%Y-%m-%d")
                    auto = next((a for a in self.autok if a.rendszam == rendszam), None)
                    if auto:
                        self.berlesek.append(Berles(auto, mettol, meddig))

    def foglalhato(self, auto, mettol, meddig):
        for berles in self.berlesek:
            if berles.auto.rendszam == auto.rendszam:
                if not (meddig < berles.mettol or mettol > berles.meddig):
                    return False
        return True

    def listaz_autok(self):
        for i, auto in enumerate(self.autok, 1):
            print(f"{i}. {auto.leiras()}")

    def berel(self):
        self.listaz_autok()
        try:
            valasztas = int(input("Válaszd ki az autó számát: ")) - 1
            auto = self.autok[valasztas]
        except (ValueError, IndexError):
            print("Érvénytelen választás.")
            return

        try:
            mettol = datetime.strptime(input("Kezdő dátum (ÉÉÉÉ-HH-NN): "), "%Y-%m-%d")
            meddig = datetime.strptime(input("Befejező dátum (ÉÉÉÉ-HH-NN): "), "%Y-%m-%d")
        except ValueError:
            print("Hibás dátumformátum!")
            return

        if mettol.date() < datetime.now().date() or meddig.date() < datetime.now().date():
            print("Múltbéli dátum nem adható meg!")
            return

        if meddig < mettol:
            print("A befejező dátum nem lehet korábbi!")
            return

        if not self.foglalhato(auto, mettol, meddig):
            print("Az autó nem elérhető a megadott időszakban.")
            return

        berles = Berles(auto, mettol, meddig)
        self.berlesek.append(berles)
        with open(self.foglalas_file, "a", encoding="utf-8") as f:
            f.write(str(berles) + "\n")
        print("Sikeres foglalás!", str(berles))

    def listaz_aktiv_berlesek(self):
        if not self.berlesek:
            print("Nincs aktív bérlés.")
            return
        for i, b in enumerate(self.berlesek, 1):
            print(f"{i}. {b}")

    def lemond(self):
        self.listaz_aktiv_berlesek()
        try:
            valasztas = int(input("Add meg a lemondandó foglalás számát: ")) - 1
            berles = self.berlesek[valasztas]
        except (ValueError, IndexError):
            print("Érvénytelen választás.")
            return

        self.berlesek.remove(berles)
        with open(self.foglalas_file, "a", encoding="utf-8") as f:
            f.write("LEMONDVA: " + str(berles) + "\n")
        print("Foglalás lemondva:", berles)

    def ceg_adatok(self):
        print(f"\n--- {self.nev} ---")
        print("Cím: Budapest, Példa utca 1.")
        print("Telefon: +36 1 234 5678")
        print("Email: info@gyorsjarat.hu")