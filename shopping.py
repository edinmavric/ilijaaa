def ucitaj_duzine():
    try:
        duzina_spiska, duzina_cena = map(int, input().split())
        return duzina_spiska, duzina_cena
    except:
        exit()


def ucitaj_spisak(duzina):
    spisak = []
    for _ in range(duzina):
        spisak.append(input().strip())
    return spisak


def ucitaj_cene(duzina):
    cene = []
    for _ in range(duzina):
        try:
            linija = input().strip()
            naziv, prodavnica, cena, popust = map(str.strip, linija.split(','))
            cena = float(cena)
            popust = int(popust)
            cene.append((naziv, prodavnica, cena, popust))
        except:
            continue
    return cene


def kreiraj_plan_kupovine(spisak, cene):
    plan = {}
    ukupna_usteda = 0.0

    for proizvod in spisak:
        najbolja_cena = float('inf')
        najbolja_prodavnica = None
        usteda_na_proizvod = 0.0

        for naziv, prodavnica, cena, popust in cene:
            if naziv == proizvod:
                cena_sa_popustom = cena * (1 - popust / 100)
                usteda = cena - cena_sa_popustom
                if cena_sa_popustom < najbolja_cena:
                    najbolja_cena = cena_sa_popustom
                    najbolja_prodavnica = prodavnica
                    usteda_na_proizvod = usteda

        if najbolja_prodavnica:
            plan[proizvod] = (round(najbolja_cena, 2), najbolja_prodavnica)
            ukupna_usteda += usteda_na_proizvod
        else:
            plan[proizvod] = None

    return plan, round(ukupna_usteda, 2)


def ispisi_plan(plan, usteda):
    for proizvod in plan:
        if plan[proizvod]:
            cena, prodavnica = plan[proizvod]
            print(f"{proizvod} - {cena:.2f} ({prodavnica})")
        else:
            print(f"{proizvod} - X")
    print(f"Usteda: {usteda:.2f}")


def main():
    duzina_spiska, duzina_cena = ucitaj_duzine()

    if duzina_spiska <= 0 or duzina_cena <= 0:
        return

    spisak = ucitaj_spisak(duzina_spiska)
    cene = ucitaj_cene(duzina_cena)

    plan, usteda = kreiraj_plan_kupovine(spisak, cene)
    ispisi_plan(plan, usteda)


if __name__ == "__main__":
    main()
