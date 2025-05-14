from autokolcsonzo import Autokolcsonzo

def main():
    kolcsonzo = Autokolcsonzo("Gyorsjárat Autókölcsönző Kft.")

    while True:
        print("\n--- Főmenü ---")
        print("1. Autó bérlése")
        print("2. Foglalás lemondása")
        print("3. Aktív foglalások listázása")
        print("4. Cég adatok megtekintése")
        print("5. Kilépés")
        valasz = input("Választásod: ")

        if valasz == "1":
            kolcsonzo.berel()
        elif valasz == "2":
            kolcsonzo.lemond()
        elif valasz == "3":
            kolcsonzo.listaz_aktiv_berlesek()
        elif valasz == "4":
            kolcsonzo.ceg_adatok()
        elif valasz == "5":
            print("Kilépés... Viszontlátásra!")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
