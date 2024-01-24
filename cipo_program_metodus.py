
from Cipo import Cipo
def peldanyok_listaban():
    peldany1 = Cipo("Nike", 42)
    peldany2 = Cipo("Adidas", 41)
    peldany3 = Cipo("Adidas", 45)

    cipok = []
    cipok.append(peldany1)
    cipok.append(peldany2)
    cipok.append(peldany3)
    return cipok

 


def listakiir(cipok): 
    for i in range(0, len(cipok), 1):
        nev: str = cipok[i].nev
        meret: int = cipok[i].meret
        print(f"{nev} ({meret})")

#Rövid verzió:
listakiir(peldanyok_listaban())


#Ez a hosszú verzió:
       
cipok_lista = peldanyok_listaban()
listakiir(cipok_lista)

def osszegzes_tetele(cipok):
    ossz: int = 0
    for i in range(0, len(cipok), 1):
        ossz += cipok[i].meret

    atlag = ossz / len(cipok)
    print(round(atlag, 3))

osszegzes_tetele(cipok_lista)


def Nagyobb(cipok):
    legnagyobb:int=0
    for i in range(0,len(cipok),1):
      if cipok[i].meret >cipok[legnagyobb].meret:
          legnagyobb=1
    print(cipok[legnagyobb].nev)      
Nagyobb(cipok_lista)        



def nagyobb_adidas(cipok):
    van_nagyobb: bool = False

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True

    if van_nagyobb == True:
        print("Van")
    else:
        print("Nincs")


nagyobb_adidas(cipok_lista)


def db_adidas(cipok):
    db:int=0
    for i in range(0,len(cipok),1):
        if cipok[i].nev =="Adidas":
            db+=1
    print(db)
       


