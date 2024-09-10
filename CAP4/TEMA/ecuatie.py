"""
Creati un script care sa calculeze valoarea lui x = 3x^2 - 4y + 4 in intervalul 10,20,
unde y = 3x.
Creati o functie pentru calcularea lui x si y.
Sample output:
============= X = 10 ==================
Rezultatul functiei: 184
============= X = 11 ==================
Rezultatul functiei: 235
============= X = 12 ==================
Rezultatul functiei: 292
============= X = 13 ==================
Rezultatul functiei: 355
…
"""
def calculeaza_x(x):
    y = 3 * x
    rezultat = 3 * (x ** 2) - 4 * y + 4
    return rezultat

for x in range(10, 21):
    rezultat = calculeaza_x(x)
    print(f"============= X = {x} ==================")
    print(f"Rezultatul functiei: {rezultat}")
