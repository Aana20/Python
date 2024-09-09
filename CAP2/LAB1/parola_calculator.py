
"""
Parola unui calculator este 7710. Se cere input de la utilizator cu un număr. Afișați
comparatia intre aceste doua numere. Daca este True, înseamnă ca utilizatorul a ghicit
parola.

"""

parola=int(input("Ghiceste parola : "))
parola_initiala=7710

if parola_initiala == parola:
    true=True
    print(f"Rezultatul e: {true}")
else :
    print("Nu ai ghicit parola , mai incearca")