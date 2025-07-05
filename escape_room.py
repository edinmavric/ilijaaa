def podaci():
    try:
        # Učitava željene težine
        linija = input().strip()
        if not linija:
            return None, None
            
        tezine = list(map(int, linija.split()))
        
        # Validacija težina (mora biti između 1 i 5)
        for i in tezine:
            if i < 1 or i > 5:
                return None, None

        sobe = []
        while True:
            try:
                linija = input().strip()
                if not linija:
                    break
                    
                delovi = linija.split(",")
                if len(delovi) != 3:
                    continue
                    
                naziv_sobe = delovi[0].strip()
                opseg_tezine = delovi[1].strip()
                broj_tezine = int(delovi[2].strip())
                
                # Parsiranje opsega brojeva igrača
                if "-" not in opseg_tezine:
                    continue
                    
                opseg_delovi = opseg_tezine.split("-")
                if len(opseg_delovi) != 2:
                    continue
                    
                donja_granica = int(opseg_delovi[0].strip())
                gornja_granica = int(opseg_delovi[1].strip())
                
                # Validacija da su brojevi validni
                if donja_granica < 1 or gornja_granica < donja_granica:
                    continue
                    
                if broj_tezine < 1 or broj_tezine > 5:
                    continue
                    
                if not naziv_sobe:
                    continue
                
                sobe.append((naziv_sobe, donja_granica, gornja_granica, broj_tezine))
                
            except (EOFError, ValueError):
                break
                
        return tezine, sobe
        
    except (ValueError, EOFError):
        return None, None

def plan_soba(tezine, sobe):
    broj_takmicara = len(tezine)
    spisak = []
    
    for naziv_sobe, donja_granica, gornja_granica, broj_tezine in sobe:
        # Proverava da li broj takmičara odgovara opsegu sobe
        if donja_granica <= broj_takmicara <= gornja_granica:
            # Proverava da li težina sobe zadovoljava želje svih članova
            # (tężina sobe mora biti >= od željene težine svakog člana)
            if all(broj_tezine >= zeljena_tezina for zeljena_tezina in tezine):
                spisak.append(naziv_sobe)
                
    return sorted(spisak)

def ispis(rezultat):
    for naziv_sobe in rezultat:
        print(naziv_sobe)

def main():
    tezine, sobe = podaci()
    if tezine is None or sobe is None:
        return
    rezultat = plan_soba(tezine, sobe)
    ispis(rezultat)

if __name__ == "__main__":
    main()