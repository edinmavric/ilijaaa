def ucitaj_duzine():
    """Učitava dužine spiska za kupovinu i liste cena."""
    try:
        linija = input().strip()
        if not linija:
            return None, None
        
        delovi = linija.split()
        if len(delovi) != 2:
            return None, None
            
        d1, d2 = int(delovi[0]), int(delovi[1])
        
        # Proverava da li su dužine validne
        if d1 < 0 or d2 < 0:
            return None, None
            
        return d1, d2
    except (ValueError, EOFError):
        return None, None

def ucitaj_spisak(n):
    """Učitava spisak proizvoda za kupovinu."""
    if n == 0:
        return []
    
    spisak = []
    for _ in range(n):
        try:
            linija = input().strip()
            if linija:  # dodaje samo neprazne proizvode
                spisak.append(linija)
        except EOFError:
            break
    return spisak

def ucitaj_cene(m):
    """Učitava podatke o cenama proizvoda."""
    if m == 0:
        return []
    
    cene = []
    for _ in range(m):
        try:
            linija = input().strip()
            if not linija:
                continue
                
            delovi = linija.split(',')
            if len(delovi) != 4:
                continue
                
            naziv = delovi[0].strip()
            prodavnica = delovi[1].strip()
            
            # Validacija da nisu prazni stringovi
            if not naziv or not prodavnica:
                continue
            
            try:
                cena = float(delovi[2].strip())
                popust = int(delovi[3].strip())
                
                # Validacija da cena i popust nisu negativni
                if cena < 0 or popust < 0 or popust > 100:
                    continue
            except ValueError:
                continue
                
            cene.append((naziv, prodavnica, cena, popust))
        except EOFError:
            break
    return cene

def napravi_plan(spisak, cene):
    """Kreira plan kupovine na osnovu najnižih cena."""
    plan = []
    ukupna_usteda = 0.0
    
    for proizvod in spisak:
        najbolja_cena = None
        najbolja_prodavnica = None
        najbolja_originalna_cena = None
        
        # Pronalazi najbolju cenu za proizvod
        for naziv, prodavnica, cena, popust in cene:
            if naziv == proizvod:
                cena_sa_popustom = cena * (1.0 - popust / 100.0)
                
                if najbolja_cena is None or cena_sa_popustom < najbolja_cena:
                    najbolja_cena = cena_sa_popustom
                    najbolja_prodavnica = prodavnica
                    najbolja_originalna_cena = cena
        
        if najbolja_cena is not None:
            plan.append((proizvod, najbolja_cena, najbolja_prodavnica))
            usteda_proizvoda = najbolja_originalna_cena - najbolja_cena
            ukupna_usteda += usteda_proizvoda
        else:
            plan.append((proizvod, None, None))
    
    return plan, ukupna_usteda

def ispisi_plan(plan, usteda):
    """Ispisuje plan kupovine i ukupnu uštedu."""
    for naziv, cena, prodavnica in plan:
        if cena is not None:
            print(f"{naziv} - {cena:.2f} ({prodavnica})")
        else:
            print(f"{naziv} - X")
    print(f"Usteda: {usteda:.2f}")

def main():
    """Glavna funkcija programa."""
    duz_sp, duz_cena = ucitaj_duzine()
    if duz_sp is None or duz_cena is None:
        return
    
    spisak = ucitaj_spisak(duz_sp)
    cene = ucitaj_cene(duz_cena)
    plan, usteda = napravi_plan(spisak, cene)
    ispisi_plan(plan, usteda)

if __name__ == "__main__":
    main()
