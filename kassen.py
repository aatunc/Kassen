

produkte = {
    "Apfel": 0.50,
    "Banane": 0.60,
    "Orange": 0.70,
    "Brot": 2.00,
    "Milch": 1.00
}


def bestellung_aufnehmen():
    bestellung = []
    gesamtbetrag = 0

    while True:
        produkt = input("Bitte geben Sie das Produkt ein oder 'fertig', um die Bestellung abzuschließen: ")
        if produkt == "fertig":
            break
        menge = int(input("Bitte geben Sie die Menge ein: "))
        preis = produkte.get(produkt, 0)
        gesamtbetrag += (preis * menge)
        bestellung.append((produkt, menge, preis))

    return bestellung, gesamtbetrag


def quittung_drucken(bestellung, gesamtbetrag):
    print("\n\nIhre Bestellung:")
    for produkt, menge, preis in bestellung:
        print(produkt, "x", menge, "-", preis*menge, "CHF")
    print("\nGesamtbetrag:", gesamtbetrag, "CHF")


bestellung, gesamtbetrag = bestellung_aufnehmen()
quittung_drucken(bestellung, gesamtbetrag)
