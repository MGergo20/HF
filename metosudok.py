import random
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


def Marti_allapota():
    nap_neve=str(input("Kérlek add meg a napot, amire kíváncsi vagy!"))
    óra_neve=str(input("Kérlek add meg az órát, amire kíváncsi vagy!"))
    if nap_neve == "hétfő":
        if óra_neve == "programozás":
            print("alszik")
        elif óra_neve == "hittan":
            print("alszik")
        elif óra_neve == "bármi":
            print("alszik")
    elif nap_neve == "kedd":
        if óra_neve == "hittan":
            print("figyel")
        elif óra_neve == "nem hittan":
            print("alszik")
        elif óra_neve == "programozás":
            print("alszik")
    elif nap_neve == "szerda":
        if óra_neve == "programozás":
            print("dolgozik")
        elif óra_neve == "hittan":
            print("nincs info!")
        elif óra_neve == "bármi":
            print("nincs info!")
    elif nap_neve == "csütörtök":
        if óra_neve == "hittan":
            print("figyel")
        elif óra_neve == "bármi":
            print("figyel")
        elif óra_neve == "programozás":
            print("figyel")
    elif nap_neve == "Péntek":
        if óra_neve == "programozás":
            print("félig van jelen!")
        elif óra_neve == "hittan":
            print("félig van jelen!")
        elif óra_neve == "bármi":
            print("félig van jelen!")


def gyokvonas():
    szam:int = -1  
    while szam < 0:  
        bekert_szam = int(input("Kérem, adjon meg egy nem negatív egész számot: "))
        szam = int(bekert_szam)
        if szam < 0:
                print("Hiba: Negatív számnak nincs valós négyzetgyöke!")
        else:
            print("Hiba: Kérjük, érvényes egész számot adjon meg!")
    gyok = szam ** 0.5
    print(f"A {szam} négyzetgyöke: {gyok:.0f}")

def ermedobas():
        eredmeny_lista=[]
        i:int=0
        while(i<10):
            erem:int=int(random.random()*2) +1
            if(erem==1):
                eredmeny_lista.append("Fej")
            elif(erem==2):
                eredmeny_lista.append("írás")
            i+=1
        return eredmeny_lista
def fej_dobasok(eredmeny_lista):
    i:int=0
    fej:int=0

    while(i<len(eredmeny_lista)):
        if(eredmeny_lista[i]=="Fej"):
            fej +=1
        i+=1
    return fej

def szam_elemzes():
    szam = int(input("Adj meg egy számot! "))
    i = 1  
    while i <= szam:
        print(f"Ennyi {i}-es: {szam // i}")  
        i *= 10  


    
        


        


