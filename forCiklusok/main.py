# %%
import time
from rich.console import Console
from rich.table import Table
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


# %%
print("------- 1. Feladat -------")

N = safeInput("Írjon be egy számot 1 és 10 között", minimum=1, maximum=10)
for i in range(N):
    print(f"{i} az ismert szólás")

# %%
print("------- 2. Feladat -------")

N = safeInput("Írjon be egy számot 1 és 10 között", minimum=1, maximum=10)
for i in range(N):
    print(f"Megmondtam már {i}-szer, hogy semmit sem mondok el kétszer!")

# %%
print("------- 3. Feladat -------")

print(*range(0, 50), sep=", ")
print(*range(182, 213), sep=", ")
print(*range(100, 201, 2), sep=", ")
print(*range(89, 58, -1), sep=", ")

for i in range(1,21):
    print(f"{i} négyzete {i*i}")

for i in range(99, 1, -3):
    print(i)

for i in range(0,51):
    if i % 5 == 0:
        print(i)
for i in range(0,1000):
    print(i, sep=", ", end=".")

print(*range(1000, 0, -3), sep=", ")

# %%
print("------- 4. Feladat -------")

print("*" * 100)

ch = input("->")
db = safeInput("->", sign=1)
print(ch * db)

sz = input("->")
ls = (str("*" * (len(sz) + 4)), "* " + sz + " *", str("*" * (len(sz) + 4)))

for item in ls:
    print(item)

for col in range(8):
    if col % 2 == 0:
        print(" *" * 4, end="") 
    else:
        print("* " * 4, end="")
    print("\n", end="")


# %%
print("------- 5. Feladat -------")

a = safeInput("->")
b = safeInput("->")
c = safeInput("->", minimum=1)

if a < b:
    for i in range(a, b, c):
        print(i)
elif a > b:
    for i in range(b, a, c):
        print(i)

# %%
print("------- 6. Feladat -------")

db = safeInput("->", sign=1)
for i in range(1, db + 1):
    print(i*i, end=", ")

# %%
print("------- 7. Feladat -------")
db = safeInput("->", sign=1)
for i in range(1, db + 1):
    print(i**3, end="\n")

# %%
print("------- 8. Feladat -------")
a = safeInput("->", minimum=0)
b = safeInput("->", minimum=0)

for num in range(min(a, b), max(a, b)):
    print(round(num ** 0.5, 2))

# %%
print("------- 9. Feladat -------")
temp = safeInput("", minimum=0)
fakt = 1
for i in range(1, temp + 1):
    fakt *= i

print(fakt)

# %%
print("------- 10. Feladat -------")

db = safeInput("->", sign=1)
for i in range(1, db + 1):
    print(i*i, end=", ")

# %%
print("------- 11. Feladat -------")
temp = 0
n = safeInput("->", sign=1)
for i in range(n + 1):
    if i % 2 == 1:
        temp += i
print(temp)

# %%
print("------- 12. Feladat -------")
k = safeInput("->", minimum=0)
temp = 0
for i in range(1, k + 1):
    temp += i * i + i
print(temp)

# %%
print("------- 13. Feladat -------")
n = safeInput("->", sign=1)
for i in range(n + 1):
    if i % 3 == 0:
        print(i)

# %%
print("------- 14. Feladat -------")
n = safeInput("->", minimum=0)
temp = []
a, b = 0, 1
for _ in range(n):
    temp.append(a)
    a, b = b, a + b

print(*temp, sep=", ")

# %%
print("------- 15. Feladat -------")

def isPrime(num):
    if num < 2:
        return False
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

n = safeInput("->", minimum=0)
j = 2
for _ in range(n):
    while not isPrime(j):
        j += 1
    print(j)
    j += 1

# %%
print("------- 16. Feladat -------")
console = Console()

meret = 10

table = Table(show_header=True, header_style="bold cyan")

table.add_column("·", justify="center", style="dim")
for i in range(1, meret + 1):
    table.add_column(str(i), justify="right")

for i in range(1, meret + 1):
    sor_adata = [str(i)]
    for j in range(1, meret + 1):
        sor_adata.append(str(i * j))
    table.add_row(*sor_adata)

console.print(table)

# %%
print("------- 17. Feladat -------")

for _ in range(10):
    temp = (randint(0, 10), randint(0,25), randint(0,50), randint(10, 75), randint(-50, 50), randint(-100, -70))

    for item in temp:
        print(" " * (4 - len(str(item))), end="")
        print(item, end=" | ")
    print("", end="\n")

# %%
print("------- 18. Feladat -------")

n = safeInput("írja be a csillagok számát egész számként", sign=1)
"""
for _ in range(n):
    print("*")
"""

for _ in range(n):
    print("* " * n)


# %%
print("------- 19. Feladat -------")

m = safeInput("írja be az y értéket", sign=1)
n = safeInput("írja be az x értéket", sign=1)

for _ in range(m):
    print("*" * n)

# %%
print("------- 20. Feladat -------")

m = safeInput("írja be az y értéket", sign=1)
n = safeInput("írja be az x értéket", sign=1)

for i in range(m, 0, -1):
    print(" " * i, end="")
    print("* " * n, end="\n")

# %%
print("------- 21. Feladat -------")

n = safeInput("írja be a rétegek számát: ", sign=1)
j = 1
for i in range(n, 0, -1):
    text = " " * i + "*" * j
    print(text)
    j += 2


# %%
print("------- 22. Feladat -------")

m = safeInput("írja be az y értéket", sign=1)
n = safeInput("írja be az x értéket", sign=1)

for row in range(m):
    if row == 0 or row == m - 1:
        print("*" * n)
    elif n == 1:
        print("*")
    else:
        print("*" + " " * (n - 2) + "*")

# %%
print("------- 23. Feladat -------")

data = {"g": 0, "b": 0}
for i in range(10):
    a = randint(1, 100)
    b = randint(1, 100)
    ösz = safeInput(f"{a} + {b} = ")
    kül = safeInput(f"{a} - {b} = ")
    isGood = True
    if ösz == a + b:
        print(f"{a} + {b} = {ösz}")
        print("ez sikerült")
    else:
        print(f"{a} + {b} != {ösz}")
        print("ez nem sikerült")
        isGood = False
    if kül == a - b:
        print(f"{a} - {b} = {kül}")
        print("ez sikerült")
    else:
        print(f"{a} - {b} != {kül}")
        print("ez nem sikerült")
        isGood = False
    if isGood:
        print("Ez a feladatsorozat sikerült")
        data["g"] += 1
    else:
        print("Ez a feladatsorozat nem sikerült")
        data["b"] += 1
print(f"10 feladatból {data['b']} rontottál el és {data['g']}")

# %%
print("------- 25. Feladat -------")

n = safeInput("írja be a számot -> ", sign=1)
temp = []

for i in range(1, n + 1):
    if n % i == 0:
        temp.append(i)

print(*temp)


# %%
print("------- 26. Feladat -------")

n = safeInput("írja be a számot -> ", sign=1)
temp = []

for i in range(1, n + 1):
    if n % i == 0:
        temp.append(i)

print(sum(temp))


# %%
print("------- 27. Feladat -------")
n = safeInput("írja be a számot -> ", sign=1)
temp = []

for i in range(1, n + 1):
    if n % i == 0:
        temp.append(i)
        
if sum(temp) == n * 2:
    print("Tökéletes szám")
else:
    print("nem tökéletes szám")


# %%
a = safeInput("írja be a számot -> ")
k = safeInput("írja be a számot -> ")

print(f"hatványérték: {a ** k}")

# %%
text = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

base = text.split(" ")
ls = base.copy()
isSame = False
while not isSame:
    print(*ls)
    ls.append(ls[0])
    ls.remove(ls[0])
    if ls == base:
        isSame = True
    


