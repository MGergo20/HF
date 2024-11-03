def elso_feladat():
    szam=int(input("Kérlek adj meg egy számot 200 és 920 között"))
    if szam < 200:
        print("Hiba: a szám kisebb mint 200!")
    else:
        if szam > 920:
            print("Hiba a szám nagyobb mint 920!")   
        else:
            elso_szamjegy = str(szam)[0] 
            print("Az első számjegye:", elso_szamjegy)