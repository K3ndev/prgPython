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


print("------- 1. Feladat -------")

N = safeInput("Írjon be egy számot 1 és 10 között", minimum=1, maximum=10)
for i in range(N):
    print(f"{i} az ismert szólás")


print("------- 2. Feladat -------")

N = safeInput("Írjon be egy számot 1 és 10 között", minimum=1, maximum=10)
for i in range(N):
    print(f"Megmondtam már {i}-szer, hogy semmit sem mondok el kétszer!")


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

print("------- 4. Feladat -------")

print("*" * 100)

ch = input("->")
db = safeInput("->", sign=1)
print(ch * db)

sz = input("->")
ls = (str("*" * (len(sz) + 4)), "* " + sz + " *", str("*" * (len(sz) + 4)))

for item in ls:
    print(item)
