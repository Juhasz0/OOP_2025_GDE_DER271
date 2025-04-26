from auto import berelj_auto
from teherauto import berelj_teherauto

def listaz_foglalasok():
    try:
        with open("foglalasok.txt", "r", encoding="utf-8") as file:
            foglalasok = file.readlines()
        return foglalasok
    except FileNotFoundError:
        return []

def lemondas():
    foglalasok = listaz_foglalasok()

    if not foglalasok:
        print("\nNincs jelenleg aktív foglalás.")
        return

    print("\n--- Aktív foglalások ---")
    aktiv_foglalasok = [f for f in foglalasok if not f.startswith("LEMONDVA:")]

    if not aktiv_foglalasok:
        print("Jelenleg nincs aktív foglalás.")
        return

    for index, foglalas in enumerate(aktiv_foglalasok, 1):
        print(f"{index}. {foglalas.strip()}")
    print(f"{len(aktiv_foglalasok) + 1}. Kilépés")

    try:
        valasztas = int(input("Add meg a lemondandó foglalás számát (vagy válaszd a Kilépést): "))

        if valasztas == len(aktiv_foglalasok) + 1:
            print("\nKilépés a lemondásból...")
            return  

        if 1 <= valasztas <= len(aktiv_foglalasok):
            lemondott_foglalas = aktiv_foglalasok[valasztas - 1]

            uj_foglalasok = []
            for sor in foglalasok:
                if sor == lemondott_foglalas:
                    uj_foglalasok.append(f"LEMONDVA: {sor.strip()}\n") 
                else:
                    uj_foglalasok.append(sor)

            with open("foglalasok.txt", "w", encoding="utf-8") as file:
                file.writelines(uj_foglalasok)

            print(f"\nA következő foglalás sikeresen le lett mondva:\n{lemondott_foglalas.strip()}")
        else:
            print("Érvénytelen választás.")
    except ValueError:
        print("Kérlek, érvényes számot adj meg!")

def ceg_adatok_megtekintese():
    try:
        with open("infok.txt", "r", encoding="utf-8") as file:
            adatok = file.read()
            print("\n--- Cég adatai ---")
            print(adatok)
    except FileNotFoundError:
        print("\nAz információs fájl nem található!")

def aktiv_foglalasok_listazasa():
    foglalasok = listaz_foglalasok()

    print("\n--- Aktív foglalások ---")
    aktiv_foglalasok = [f for f in foglalasok if not f.startswith("LEMONDVA:")]

    if not aktiv_foglalasok:
        print("Jelenleg nincs aktív foglalás.")
        return

    for index, foglalas in enumerate(aktiv_foglalasok, 1):
        print(f"{index}. {foglalas.strip()}")

def main():
    while True:
        print("\nÜdvözöljük a Gyorsjárat Autókölcsönző Kft. rendszerében!")
        print("Kérjük, válasszon az alábbi lehetőségek közül:")
        print("1. Személyautó bérlése")
        print("2. Teherautó bérlése")
        print("3. Foglalás lemondása")
        print("4. Cég adatai megtekintése")
        print("5. Aktív foglalások megtekintése")
        print("6. Kilépés")

        valasztas = input("Kérlek, válassz (1-6): ")

        if valasztas == "1":
            berelj_auto()
        elif valasztas == "2":
            berelj_teherauto()
        elif valasztas == "3":
            lemondas()
        elif valasztas == "4":
            ceg_adatok_megtekintese()
        elif valasztas == "5":
            aktiv_foglalasok_listazasa()
        elif valasztas == "6":
            print("\nKilépés... Köszönjük, hogy a Gyorsjárat Autókölcsönzőt választotta! Viszontlátásra!")
            break
        else:
            print("Érvénytelen választás! Próbáld újra.")

if __name__ == "__main__":
    main()
