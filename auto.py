from datetime import datetime

def datum_formaz(datum_szoveg):
    return datetime.strptime(datum_szoveg, "%Y-%m-%d")

def jelenlegi_ido():
    return datetime.now()

def ellenoriz_foglalast(kivant_rendszam, mettol, meddig):
    try:
        with open("foglalasok.txt", "r", encoding="utf-8") as file:
            foglalasok = file.readlines()
    except FileNotFoundError:
        return False 

    for sor in foglalasok:
        if kivant_rendszam in sor:
            adat = sor.strip().split(", ")
            rendszam = adat[1].replace("Rendszám: ", "")
            datumok = adat[2].replace("Bérlés: ", "").split(" - ")
            foglalt_mettol = datum_formaz(datumok[0])
            foglalt_meddig = datum_formaz(datumok[1])

            if not (meddig < foglalt_mettol or mettol > foglalt_meddig):
                return True
    return False

def berelj_auto():
    autok = [
        {"nev": "Opel Astra", "rendszam": "ABC-123", "dij": 12000},
        {"nev": "Ford Focus", "rendszam": "DEF-456", "dij": 11500},
        {"nev": "Volkswagen Golf", "rendszam": "GHI-789", "dij": 13000},
        {"nev": "Toyota Corolla", "rendszam": "JKL-321", "dij": 12500},
        {"nev": "Skoda Octavia", "rendszam": "MNO-654", "dij": 11800}
    ]

    while True:
        print("\nElérhető személyautók:")
        for index, auto in enumerate(autok, 1):
            print(f"{index}. {auto['nev']} (Rendszám: {auto['rendszam']}, Napi díj: {auto['dij']} Ft)")

        try:
            valasztas = int(input("Válaszd ki a kívánt autó számát: "))
            if 1 <= valasztas <= len(autok):
                kivalasztott_auto = autok[valasztas - 1]
                print(f"Sikeresen kiválasztottad: {kivalasztott_auto['nev']} ({kivalasztott_auto['rendszam']})")

                mettol_str = input("Add meg a bérlés kezdő dátumát (ÉÉÉÉ-HH-NN): ")
                meddig_str = input("Add meg a bérlés befejező dátumát (ÉÉÉÉ-HH-NN): ")

                try:
                    mettol = datum_formaz(mettol_str)
                    meddig = datum_formaz(meddig_str)
                except ValueError:
                    print("Hibás dátumformátum! Próbáld újra.")
                    continue

                if mettol.date() < jelenlegi_ido().date() or meddig.date() < jelenlegi_ido().date():
                    print("Múltbéli dátumot nem adhatsz meg! Kérlek, próbáld újra.")
                    continue

                if meddig < mettol:
                    print("A befejező dátum nem lehet korábbi, mint a kezdő dátum.")
                    continue

                if ellenoriz_foglalast(kivalasztott_auto['rendszam'], mettol, meddig):
                    print("Sajnálom, az autó az adott időpontban már foglalt. Válassz másik autót!")
                    continue
                else:
                    
                    napok_szama = (meddig - mettol).days + 1
                    osszeg = napok_szama * kivalasztott_auto['dij']

                    with open("foglalasok.txt", "a", encoding="utf-8") as file:
                        file.write(f"Autó: {kivalasztott_auto['nev']}, Rendszám: {kivalasztott_auto['rendszam']}, Bérlés: {mettol_str} - {meddig_str}, Napi díj: {kivalasztott_auto['dij']} Ft, Összesen: {osszeg} Ft\n")

                    print(f"\nFoglalás sikeresen mentve!")
                    print(f"Bérlés hossza: {napok_szama} nap")
                    print(f"Összesen fizetendő: {osszeg} Ft")
                    break
            else:
                print("Érvénytelen választás!")
        except ValueError:
            print("Kérlek, érvényes számot adj meg!")
