def podaci():
    validne_vrednosti = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    validne_boje = ['S', 'H', 'D', 'C']
    
    try:
        talon = input().strip().split()
        
        # Validacija talona (mora biti tačno 5 karata)
        if len(talon) != 5:
            return None, None
            
        for karta in talon:
            if len(karta) != 2:
                return None, None
            vrednost, boja = karta[0], karta[1]
            if vrednost not in validne_vrednosti or boja not in validne_boje:
                return None, None

        karte_igraca = []
        while True:
            try:
                linija = input().strip()
                if not linija:
                    break
                    
                delovi = linija.split(",")
                if len(delovi) != 2:
                    continue
                    
                prva_karta = delovi[0].strip()
                druga_karta = delovi[1].strip()
                
                # Validacija karata igrača
                for karta in [prva_karta, druga_karta]:
                    if len(karta) != 2:
                        return None, None
                    vrednost, boja = karta[0], karta[1]
                    if vrednost not in validne_vrednosti or boja not in validne_boje:
                        return None, None
                
                karte_igraca.append((prva_karta, druga_karta))
                
            except EOFError:
                break
                
        return talon, karte_igraca
        
    except (ValueError, IndexError):
        return None, None

def obrada_karata(talon, karte_igraca):
    rezultati = []
    
    for igrac_karte in karte_igraca:
        # Kombinuje sve karte igrača (talon + njegove 2 karte)
        sve_karte = talon + list(igrac_karte)
        
        # Broji pojavljivanja svake vrednosti
        vrednost_brojac = {}
        boja_brojac = {}
        
        for karta in sve_karte:
            vrednost, boja = karta[0], karta[1]
            vrednost_brojac[vrednost] = vrednost_brojac.get(vrednost, 0) + 1
            boja_brojac[boja] = boja_brojac.get(boja, 0) + 1
        
        # Pronalazi najčešću vrednost
        max_broj = max(vrednost_brojac.values())
        najcesca_vrednost = None
        for vrednost, broj in vrednost_brojac.items():
            if broj == max_broj:
                najcesca_vrednost = vrednost
                break
        
        # Proverava da li ima flush (≥5 karata iste boje)
        flush_boja = None
        for boja, broj in boja_brojac.items():
            if broj >= 5:
                flush_boja = boja
                break
        
        rezultati.append({
            "broj": max_broj,
            "vrednost": najcesca_vrednost,
            "flush_boja": flush_boja
        })
    
    return rezultati

def ispis(rezultati):
    for rezultat in rezultati:
        broj = rezultat["broj"]
        vrednost = rezultat["vrednost"]
        flush_boja = rezultat["flush_boja"]
        
        if flush_boja:
            print(f"{broj}-{vrednost} {flush_boja}")
        else:
            print(f"{broj}-{vrednost}")

def main():
    talon, karte_igraca = podaci()
    if talon is None or karte_igraca is None:
        return
    rezultati = obrada_karata(talon, karte_igraca)
    ispis(rezultati)

if __name__ == "__main__":
    main()
