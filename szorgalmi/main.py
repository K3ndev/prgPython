# %%
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
# **1\. Feladat: A lepattanó labda útja**
# 
# Ejtünk egy labdát 10 méter magasságból. Minden alkalommal, amikor a labda a földre érkezik és visszapattan, az előző magasságának a 80%-ára emelkedik vissza. Írj programot, amely kiszámolja, hogy hányadik lepattanás után csökken a visszapattanási magasság 1 centiméter alá, és add meg azt is, hogy addig összesen mekkora utat tett meg a labda függőlegesen! A kiírás utolsó sora záródjon két felkiáltójellel

# %%
reb = 0.80
tol = 0.01
d = 10
dh = d
i = 0

while d > tol:
    d *= reb
    i += 1
    dh += d if d <= tol else d * 2

print(f"a labda {i}-szer pattant le. Eközben {dh} utat tett meg!!")


# %% [markdown]
# **2\. Feladat: Baktériumkultúra inváziója**
# 
# Egy biológiai kísérletben egyetlen baktériummal indulunk, és a baktériumok ideális körülmények között minden órában megkétszereződnek. A Petri-csésze legfeljebb 100 000 baktériumot képes befogadni. A kiírt értékek mellett mindig szerepeljen a darabka szó is
# 
# Írj programot, amely kiírja óránként a baktériumok számát, és a végén megadja, hogy hány óra elteltével éri el vagy lépi túl a kultúra a csésze kapacitáshatárát!

# %%
goal = 100000
db = 1
i = 0
while db <= goal:
    print(f"{i}. óra {db} darabka baktérium")
    db *= 2
    i += 1

print(f"A kultúrának {i} óra kellet hogy túllépje a kapacitást így {db} darabka baktérium lett")

# %% [markdown]
# **3\. Feladat: Bolygók együttállása**
# 
# Két bolygó mozog a csillag körül: az „A" bolygó 12 nap, a „B" bolygó pedig 18 nap alatt kerüli meg a csillagot. A ciklusban a napokat számláló változó neve kötelezően nap legyen
# 
# Mindketten egyszerre indulnak el a 0. napon a rajtvonalról. Írj programot, amely kiszámolja, hogy hányadik napon találkoznak újra legkorábban a rajtvonalon!

# %%
p1 = 12
p2 = 18
nap = 1

while nap % p1 != 0 or nap % p2 != 0:
    nap += 1

print(f"{nap}. múlva találkozik a két bolygó")


# %% [markdown]
# **4\. Feladat: Palindrom számok**
# 
# A palindrom számok azok, amelyek hátulról olvasva is pontosan ugyanazok (például 121 vagy 454).
# 
# Írj egy programot, amely bekér egy 100 és 999 közötti egész számot (a bekérést addig ismételjük, amig nem 3 jegyű számot ad meg), és eldönti róla, hogy palindrom-e! _A bekérés parancs szövege pontosan ez legyen: „Szám:"_
# 
# _Írasd ki az összes olyan háromjegyű számot, amely palindrom!_

# %%
def pal(n):
    text = str(n)
    return text == text[::-1]

pList = []
nums = (str(i) for i in range(100, 1000))
for i in nums:
    if pal(i):
        pList.append(i)

print(*pList, sep=", ")

num = safeInput("Szám:", minimum=100, maximum=999)

if pal(num):
    print("Palindrom")
else:
    print("Nem palindrom")



