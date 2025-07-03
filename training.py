def ucitaj_vezbe():
    try:
        n = int(input())
        vezbe = []

        for _ in range(n):
            linija = input().strip()
            delovi = linija.split(",")
            if len(delovi) != 4:
                return None

            naziv = delovi[0].strip()
            grupa = delovi[1].strip()
            trajanje = int(delovi[2].strip())
            kalorije_10min = int(delovi[3].strip())

            vezbe.append({
                "naziv": naziv,
                "grupa": grupa,
                "trajanje": trajanje,
                "kalorije_10min": kalorije_10min
            })

        return vezbe
    except:
        return None


def ucitaj_zelje():
    linija = input().strip()
    delovi = linija.split(" ")
    if len(delovi) != 3:
        return None
    try:
        max_trajanje = int(delovi[0])
        grupa = delovi[1]
        intenzitet = delovi[2]
        return max_trajanje, grupa, intenzitet
    except:
        return None


def filtriraj_vezbe(vezbe, grupa, intenzitet):
    filtrirane = []

    for v in vezbe:
        if v["grupa"] != grupa:
            continue

        kalorije = v["kalorije_10min"]
        if kalorije < 60 and intenzitet == "slab":
            filtrirane.append(v)
        elif 60 <= kalorije < 100 and intenzitet == "srednji":
            filtrirane.append(v)
        elif kalorije >= 100 and intenzitet == "jak":
            filtrirane.append(v)

    return filtrirane


def kreiraj_plan(vezbe, max_trajanje):
    plan = []
    ukupno_trajanje = 0
    ukupno_kalorije = 0.0

    for v in vezbe:
        if ukupno_trajanje + v["trajanje"] > max_trajanje:
            break

        trajanje = v["trajanje"]
        kalorije_po_minuti = v["kalorije_10min"] / 10
        kalorije_za_trajanje = kalorije_po_minuti * trajanje

        v_copy = v.copy()
        v_copy["kalorije_trajanje"] = kalorije_za_trajanje

        plan.append(v_copy)
        ukupno_trajanje += trajanje
        ukupno_kalorije += kalorije_za_trajanje

    return plan, ukupno_trajanje, ukupno_kalorije


def ispisi_plan(plan, ukupno_trajanje, ukupno_kalorije):
    if not plan:
        print("Nema vezbi po zadatom kriterijumu")
    else:
        for v in plan:
            print(f"{v['naziv']} - {v['trajanje']} min - {v['kalorije_trajanje']:.2f} kcal")
        print(f"Ukupno trajanje: {ukupno_trajanje} min")
        print(f"Ukupno kalorija: {ukupno_kalorije:.2f} kcal")


def main():
    vezbe = ucitaj_vezbe()
    if vezbe is None:
        return

    zelja = ucitaj_zelje()
    if zelja is None:
        return

    max_trajanje, grupa, intenzitet = zelja
    vezbe_filt = filtriraj_vezbe(vezbe, grupa, intenzitet)
    plan, ukupno_trajanje, ukupno_kalorije = kreiraj_plan(vezbe_filt, max_trajanje)
    ispisi_plan(plan, ukupno_trajanje, ukupno_kalorije)


main()
