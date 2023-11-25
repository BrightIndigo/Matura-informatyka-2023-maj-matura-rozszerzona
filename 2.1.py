import random

n = random.randint(1, 1000)

liczba_binarna = bin(n)[2:]
print(liczba_binarna)

ostatnia_cyfra = None
liczba_blokow1 = 0
liczba_blokow0 = 0

for i in liczba_binarna:
    if i == '1':
        if ostatnia_cyfra == 0 or ostatnia_cyfra is None:
            liczba_blokow1 += 1
        ostatnia_cyfra = 1
    elif i == '0':
        if ostatnia_cyfra == 1 or ostatnia_cyfra is None:
            liczba_blokow0 += 1
        ostatnia_cyfra = 0

print("liczba bloków 0: ", liczba_blokow0)
print("liczba bloków 1: ", liczba_blokow1)
