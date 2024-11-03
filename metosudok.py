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


def masodik_feladat():
    ora=int(input("Kérlek add meg az óraszámot 1-9-ig!"))
    if ora == 0:
        print("Be se jövök!")
    else:
        if ora > 9:
            print("Ez már tényleg túlzás.")
        else:
            if ora == 1:
                print("Még bírjuk 90%-on vagyunk!")
            else:
                if ora == 2:
                    print("Még bírjuk (60%).")
                else:
                    if ora == 3:
                        print("Még bírjuk (60%).")
                    else:
                        if ora == 4:
                            print("Progit tanulunk, töltődünk! 70%.")
                        else:
                            if ora == 5:
                                print("Progit tanulunk, töltődünk! 70%.")
                            else:
                                if ora == 6:
                                     print("Progit tanulunk, töltődünk! 70%.")
                                else: 
                                    if ora == 7:
                                         print("Progit tanulunk, töltődünk! 70%.")
                                    else:
                                        if ora == 8:
                                            print("Lassan nem bírjuk tovább! 50%.")
                                        else:
                                            if ora == 9:
                                                print("Lassan nem bírjuk tovább! 50%.")