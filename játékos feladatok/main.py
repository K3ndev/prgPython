# %%
from random import randint

def safeInput(text, t=int, sign=0, minimum=None, maximum=None):
    while True:
        try:
            value = t(input(text))
        except ValueError:
            print(f"Kérem {t}-t adjon meg!")
            continue

        if sign == 1 and value <= 0:
            print("kérem adjon meg pozitív számot")
        elif sign == -1 and value >= 0:
            print("kérem adjon meg negatív számot")
        elif minimum is not None and value < minimum:
            print(f"Az érték legalább {minimum} legyen")
        elif maximum is not None and value > maximum:
            print(f"Az érték legfeljebb {maximum} legyen")
        else:
            return value

# %% [markdown]
# ## 1. KOCKAPÁRBAJ
# 
# ## Könnyű
# 
# Ön és A Gép két dobókockával versenyeznek. Minden fordulóban mindketten dobnak egy-egy kockával. A nagyobbat dobó játékos kap egy pontot, egyenlőség esetén senki sem kap pontot.
# 
# ## Feladatok:
# 
# - 1. Kérd be a fordulók számát!
# 
# - 2. Minden fordulóban generálj két véletlenszámot 1 és 6 között!
# 
# - 3. Írd ki a két dobást és a forduló győztesét!
# 
# - 4. Számold meg Ön és A Gép győzelmeit, valamint a döntetleneket!
# 
# - 5. A játék végén írd ki az összesített eredményt és a végső győztest!

# %%
n = safeInput("írja be a fordulók számát")
a = 0
b = 0

for _ in range(n):
    a_d = randint(1, 6)
    b_d = randint(1,6)
    if a_d > b_d:
        a += 1
        print(f"Anna:{a_d} Béla:{b_d} | Anna nyert ")
    elif a_d == b_d:
        print(f"Anna:{a_d} Béla:{b_d} | Döntetlen ")
    else:
        b += 1
        print(f"Anna:{a_d} Béla:{b_d} | Béla nyert")

if a > b:
    print(f"Anna:{a} Béla:{b} | Anna nyert a végén")
elif a == b:
    print(f"Anna:{a} Béla:{b} | Döntetlen a végén")
else:
    print(f"Anna:{a} Béla:{b} | Béla nyert a végén")

# %% [markdown]
# 
# ## 2. SZÁMKITALÁLÓ JÁTÉK
# 
# ## Könnyű
# 
# A számítógép gondol egy egész számra 1 és 100 között. A játékosnak ki kell találnia. A program minden tipp után segít.
# 
# ## Feladatok:
# 
# - 1. Generálj egy véletlen egész számot 1 és 100 között!
# 
# - 2. Kérj be egy tippet a játékostól!
# 
# - 3. Ha a tipp túl kicsi, írd ki: „Nagyobbra gondoltam!”
# 
# - 4. Ha a tipp túl nagy, írd ki: „Kisebbre gondoltam!”
# 
# - 5. Ismételd az adatbekérést addig, amíg a játékos el nem találja a számot!
# 
# - 6. Számold meg, hány próbálkozásra volt szükség!

# %%
titok = randint(1, 100)
i = 0
for tipp in iter(lambda: safeInput("Tippeljen: "), titok):
    if titok > tipp:
        print("nagyobb")
    elif titok < tipp:
        print("kissebb")
    i += 1

print(f"eltalálta {i}db tippből")
    

# %% [markdown]
# ## 3. KŐ–PAPÍR–OLLÓ BAJNOKSÁG
# 
# ## Könnyű
# 
# A játékos a számítógép ellen játszik. Mindketten követ, papírt vagy ollót választanak.
# 
# ```
# A választások kódjai: 1 = kő, 2 = papír, 3 = olló.
# ```
# 
# ## Feladatok:
# 
# - 1. Kérd be, hány fordulót szeretne játszani a felhasználó!
# 
# - 2. Minden fordulóban kérd be a játékos választását!
# 
# - 3. A számítógép választását véletlenszám-generálással határozd meg!
# 
# - 4. Döntsd el, ki nyerte a fordulót a szokásos szabályok alapján!
# 
# - 5. Minden forduló után írd ki az eredményt!
# 
# - 6. A végén jelenítsd meg a két játékos győzelmeinek és a döntetleneknek a számát!

# %%
n = safeInput("írja be a fordulók számát")
a = 0
b = 0
for _ in range(n):
    a_d = safeInput("A választások kódjai: 1 = kő, 2 = papír, 3 = olló. \n -->", maximum=3, minimum=1)
    b_d = randint(1,6)
    if a_d == b_d:
        print(f"ön:{a_d} Gép:{b_d} | Döntetlen ")
    elif a == 1:
        if b == 3:
            print(print(f"ön:{a_d} Gép:{b_d} | nyert"))
            a += 1
        else:
            print(f"ön:{a_d} Gép:{b_d} | vesztett")
            b += 1
    elif a == 2:
        if b == 1:
            print(print(f"ön:{a_d} Gép:{b_d} | nyert"))
            a += 1
        else:
            print(f"ön:{a_d} Gép:{b_d} | vesztett")
            b += 1
    elif a == 3:
        if b == 2:
            print(print(f"ön:{a_d} Gép:{b_d} | nyert"))
            a += 1
        else:
            print(f"ön:{a_d} Gép:{b_d} | vesztett")
            b += 1
print(f"ön:{a} gép:{b} döntetlen:{n - a - b}")


# %% [markdown]
# ## 4. HÉT SZERENCSÉS
# 
# ## Közepes
# 
# A játékos két kockával dob. Ha a dobott számok összege 7, akkor 10 pontot kap. Ha két egyforma számot dob, akkor 5 pontot kap. Minden más esetben 1 pont jár. A 7-es összeg szabálya elsőbbséget élvez.
# 
# ## Feladatok:
# 
# - 1. Kérd be a dobások számát!
# 
# - 2. Minden dobásnál generálj két véletlenszámot!
# 
# - 3. Számítsd ki a dobások összegét és a megszerzett pontszámot!
# 
# - 4. Írd ki az összes dobás eredményét!
# 
# - 5. Összesítsd a megszerzett pontokat!
# 
# - 6. Számold meg, hányszor sikerült 7-es összeget dobni!
# 
# - 7. Határozd meg az egy dobással szerzett legtöbb pontot!

# %%
n = safeInput("írja be a fordulók számát")
ls = []
for _ in range(n):
    a_d = randint(1, 6)
    b_d = randint(1,6)
    print(f"{a_d} | {b_d}: ", end="")
    if a_d + a_d == 7:
        ls.append(10)
        print(f"{ls[-1]} pont", end="\n" )
    elif a_d == b_d:
        ls.append(5)
    else:
        ls.append(1)
print(f"össz. pont: {sum(ls)} | hetesek: {ls.count(10)} | legnagyobb: {max(ls)}")

# %% [markdown]
# ## 5. SZERENCSEKERÉK
# 
# ## Közepes
# 
# A játékos egy képzeletbeli szerencsekereket pörget. A keréken 10 mező található, és a megszerzett pontok a kipörgetett mezőtől függnek.
# 
# ## Mező Eredmény
# 
# - 1–3 +100 pont
# 
# - 4–6 +200 pont
# 
# - 7–8 −150 pont
# 
# - 9 Pontszám duplázása
# 
# - 10 Pontszám nullázása
# 
# A játékos 500 ponttal indul.
# 
# ## Feladatok:
# 
# - 1. Kérd be a pörgetések számát!
# 
# - 2. Generálj minden pörgetésnél egy véletlen számot 1 és 10 között!
# 
# 
# - 3. Az eltalált mező alapján módosítsd a pontszámot!
# 
# - 4. Minden pörgetés után írd ki a mező számát és az aktuális pontszámot!
# 
# - 5. Számold meg, hányszor nullázódott le a pontszám!
# 
# - 6. A játék végén írd ki a végső pontszámot és a nullázások számát!

# %%
pontszam = 500
nullazasok = 0
darab = safeInput("Pörgetések száma: ", sign=1)
sorszam = 1

while sorszam <= darab:
    mezo = randint(1, 10)

    if mezo == 9:
        pontszam *= 2
        eredmeny = "duplázás"
    elif mezo == 10:
        pontszam = 0
        nullazasok += 1
        eredmeny = "nullázás"
    else:
        if mezo < 4:
            valtozas = 100
        elif mezo < 7:
            valtozas = 200
        else:
            valtozas = -150
        pontszam += valtozas
        eredmeny = f"{valtozas:+} pont"

    print(f"{sorszam}. pörgetés: {mezo} -> {eredmeny}, egyenleg: {pontszam}")
    sorszam += 1

print(f"Végső pontszám: {pontszam} Nullázások száma: {nullazasok}")

# %% [markdown]
# ## 6. PÉNZFELDOBÓ BAJNOKSÁG
# 
# ## Közepes
# 
# A játékos a számítógép ellen fogad arra, hogy egy feldobott pénzérme fej vagy írás lesz. A játékos 1000 Ft-tal kezdi a játékot.
# 
# ## Feladatok:
# 
# - 1. Minden kör elején írd ki a játékos aktuális egyenlegét!
# 
# - 2. Kérd be, hogy fejre (1) vagy írásra (2) fogad!
# 
# - 3. Kérd be a tétet, amely nem lehet nagyobb az aktuális egyenlegnél, és pozitív egész számnak kell lennie!
# 
# - 4. Véletlenszám segítségével szimuláld a pénzfeldobást!
# 
# - 5. Helyes tipp esetén add hozzá, hibás tipp esetén vond le a tétet az egyenlegből!
# 
# - 6. A játék addig tartson, amíg a játékos pénze el nem fogy, vagy a játékos nem jelzi, hogy kiszáll!
# 
# - 7. A végén írd ki a játékos végső egyenlegét és a megnyert körök számát!

# %%
penz = 1000
nyert = 0
jatszik = True

while penz > 0 and jatszik:
    print(f"Egyenleg: {penz} Ft")
    valasztas = safeInput("Fej (1) vagy írás (2): ", minimum=1, maximum=2)
    tet = safeInput("Mekkora a tét? ", sign=1, maximum=penz)
    feldobott = randint(1, 2)

    if feldobott != valasztas:
        penz -= tet
        print(f"A gép nyert. Feldobás: {feldobott}, egyenleg: {penz} Ft")
    else:
        penz += tet
        nyert += 1
        print(f"Ön nyert. Feldobás: {feldobott}, egyenleg: {penz} Ft")

    if penz > 0:
        jatszik = safeInput("Folytatás? (1 igen, 0 kiszáll): ", minimum=0, maximum=1) == 1

print(f"Végső egyenleg: {penz} Ft Megnyert körök: {nyert}")

# %% [markdown]
# ## 7. HUSZONEGY – KOCKÁKKAL
# 
# ## Nehezebb
# 
# A játékos célja, hogy dobókockák segítségével minél közelebb kerüljön a 21 ponthoz, de ne lépje túl azt. Minden dobás során két kockával dob, és a dobott számok összege hozzáadódik az addigi pontszámához.
# 
# ## Feladatok:
# 
# - 1. A játékos kezdetben 0 ponttal rendelkezik.
# 
# - 2. Kérdezd meg, hogy szeretne-e dobni!
# 
# - 3. Ha igen, generálj két véletlenszámot 1 és 6 között!
# 
# - 4. Add hozzá a két dobás összegét a játékos pontszámához!
# 
# - 5. Írd ki a dobott számokat és az aktuális összpontszámot!
# 
# - 6. Ha a pontszám meghaladja a 21-et, a játékos azonnal veszít.
# 
# - 7. Ha pontosan 21 pontot ér el, azonnal nyer.
# 
# - 8. Ha a játékos 21 pont alatt megáll, írja ki a program, hogy hány ponttal maradt el a 21-től!
# 
# - 9. A játék végén írd ki a dobások számát is!
# 

# %%
osszpont = 0
korok = 0
jatszik = True

while jatszik and osszpont < 21:
    jatszik = safeInput("Dobjunk? (1 igen, 0 nem): ", minimum=0, maximum=1) == 1
    if not jatszik:
        break

    dobas1 = randint(1, 6)
    dobas2 = randint(1, 6)
    osszpont += dobas1 + dobas2
    korok += 1
    print(f"Dobás: {dobas1} + {dobas2}, összesen: {osszpont}")

if osszpont > 21:
    print("Túllépted a 21-et, vesztettél!")
elif osszpont == 21:
    print("Elérted a 21-et, nyertél!")
else:
    print(f"Megálltál, {21 - osszpont} pont hiányzott a 21-hez.")

print(f"Dobások száma: {korok}")

# %% [markdown]
# ## 8. KINCSVADÁSZAT – A TITKOS KOORDINÁTA
# 
# ## Nehezebb
# 
# Egy kincs egy képzeletbeli, 10 × 10-es négyzetrács valamelyik mezőjében van elrejtve. Az oszlopokat és a sorokat 1-től 10-ig számozzuk.
# 
# A számítógép véletlenszerűen elhelyezi a kincset. A játékosnak legfeljebb 7 próbálkozása van megtalálni.
# 
# ## Feladatok:
# 
# - 1. Generálj két véletlenszámot 1 és 10 között, amelyek a kincs koordinátáit jelentik!
# 
# - 2. Kérd be a játékostól a keresett mező két koordinátáját!
# 
# - 3. Ha mindkét koordináta helyes, a játékos megtalálta a kincset.
# 
# - 4. Hibás tipp esetén számítsd ki a kincs és a játékos által megadott pont távolságát a Pitagorasz- tétellel!
# 
# 
# - 5. A távolságot két tizedesjegyre formázva írd ki!
# 
# - 6. Ha a távolság legfeljebb 2, írd ki: „Forró!”
# 
# - 7. Ha a távolság 2-nél nagyobb, de legfeljebb 5, írd ki: „Langyos!”
# 
# - 8. Egyéb esetben írd ki: „Hideg!”
# 
# - 9. A játék 7 próbálkozás után, illetve a kincs megtalálásakor érjen véget. A végén jelenjen meg a próbálkozások száma, és sikertelen játék esetén a kincs valódi helye!
# 

# %%
kincs = (randint(1, 10), randint(1, 10))
talalat = False
probalkozas = 0

while probalkozas < 7 and not talalat:
    tipp = (
        safeInput("Oszlop (1-10): ", minimum=1, maximum=10),
        safeInput("Sor (1-10): ", minimum=1, maximum=10)
    )
    probalkozas += 1

    if tipp == kincs:
        talalat = True
        print("Megtaláltad a kincset!")
    else:
        tavolsag = ((kincs[0] - tipp[0]) ** 2 + (kincs[1] - tipp[1]) ** 2) ** 0.5

        if tavolsag <= 2:
            jelzes = "Forró!"
        elif tavolsag <= 5:
            jelzes = "Langyos!"
        else:
            jelzes = "Hideg!"

        print(f"{tavolsag:.2f} távolságra van. {jelzes}")

print(f"Próbálkozások száma: {probalkozas}")
if not talalat:
    print(f"A kincs helye: ({kincs[0]}, {kincs[1]})")


